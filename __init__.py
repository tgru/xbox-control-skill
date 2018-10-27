from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_handler

from netdisco.smartglass import XboxSmartGlass

import requests

class XboxControl(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

        self.api_addr       = self.settings.get('api_addr')
        self.api_port       = self.settings.get('api_port')
        self.xbox_addr      = self.settings.get('xbox_addr')
        self.xbox_live_id   = self.settings.get('xbox_live_id')

    @intent_handler(IntentBuilder('').require('switch.state').require('state.on').require('device'))
    def handle_power_on_xbox(self, message):
        try:
            self.power_on()
        except requests.exceptions.RequestException as e:
            self.log.exception(e)
            self.speak_dialog('failed.to.power.on')

    @intent_handler(IntentBuilder('').require('switch.state').require('state.off').require('device'))
    def handle_power_off_xbox(self, message):
        try:
            self.power_off()
        except requests.exceptions.RequestException as e:
            self.log.exception(e)
            self.speak_dialog('failed.to.power.off')

    @intent_handler(IntentBuilder('').require('device').require('play').require('track'))
    def handle_play(self, message):
        try:
            self.play()
        except requests.exceptions.RequestException as e:
            self.log.exception(e)
            self.speak_dialog('failed')

    @intent_handler(IntentBuilder('').require('device').require('pause'))
    def handle_pause(self, message):
        try:
            self.pause()
        except requests.exceptions.RequestException as e:
            self.log.exception(e)
            self.speak_dialog('failed')

    @intent_handler(IntentBuilder('').require('device').require('stop'))
    def handle_stop(self, message):
        try:
            self.stop()
        except requests.exceptions.RequestException as e:
            self.log.exception(e)
            self.speak_dialog('failed')

    @intent_handler(IntentBuilder('').require('device').require('next').require('track'))
    def handle_next_track(self, message):
        try:
            self.next_track()
        except requests.exceptions.RequestException as e:
            self.log.exception(e)
            self.speak_dialog('failed')

    @intent_handler(IntentBuilder('').require('device').require('previous').require('track'))
    def handle_prev_track(self, message):
        try:
            self.prev_track()
        except requests.exceptions.RequestException as e:
            self.log.exception(e)
            self.speak_dialog('failed')

    @intent_handler(IntentBuilder('').require('device').require('find'))
    def handle_find_xbox(self, message):
        self.speak_dialog('find.xbox')
        try:
            devices = self.find_xbox()
        except Exception as e:
            self.log.exception(e)
            self.speak_dialog('failed')

        if len(devices) == 0:
            self.speak_dialog('found.no.xbox')
        elif len(devices) == 1:
            self.speak(devices[0])
            self.speak_dialog('found.one.xbox')
            self.settings['xbox_addr'] = devices[0]['ip']
            self.settings['xbox_live_id'] = devices[0]['liveid']
        else:
            self.speak_dialog('found.multiple.xbox')

    def _url(self, path):
        return self.api_addr + ':' + str(self.api_port) + path   

    def power_on(self):
        ret = requests.get(
            self._url(
                "/device/{}/poweron".format(self.xbox_live_id)
            )
        )

    def connect(self):
        device_list = requests.get(
            self._url( "/device")
        )

        ret = requests.get(
            self._url(
                "/device/{}/connect".format(self.xbox_live_id)
            )
        )

    def power_off(self):
        self.connect()
        ret = requests.get(
            self._url(
                "/device/{}/poweroff".format(self.xbox_live_id)
            )
        )

    def play(self):
        self.connect()
        ret = requests.get(
            self._url(
                "/device/{}/media/play".format(self.xbox_live_id)
            )
        )

    def pause(self):
        self.connect()
        ret = requests.get(
            self._url(
                "/device/{}/media/pause".format(self.xbox_live_id)
            )
        )

    def stop(self):
        self.connect()
        ret = requests.get(
            self._url(
                "/device/{}/media/stop".format(self.xbox_live_id)
            )
        )

    def next_track(self):
        self.connect()
        ret = requests.get(
            self._url(
                "/device/{}/media/next_track".format(self.xbox_live_id)
            )
        )

    def prev_track(self):
        self.connect()
        ret = requests.get(
            self._url(
                "/device/{}/media/prev_track".format(self.xbox_live_id)
            )
        )

    def find_xbox(self):
        netdis = XboxSmartGlass()
        netdis.update()

        # Only propagate xbox one devices
        entries = list(filter( lambda entry: entry[1]['device_type'] == 1, netdis.entries))

        xbox_list = []

        for entry in entries:
            ip = entry[0]

            if len(ip) == 0:
                continue

            ret = requests.get(self._url("/device?addr={}".format(ip)))
            liveid = next(iter(ret.json()['devices']))

            if len(liveid) == 0:
                continue

            xbox_list.append(dict([('ip', ip), ('liveid', liveid)]))

        return xbox_list

def create_skill():
    return XboxControl()