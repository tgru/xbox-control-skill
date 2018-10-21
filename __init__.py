from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_handler

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

    @intent_handler(IntentBuilder('').require('device').require('play'))
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

def create_skill():
    return XboxControl()

