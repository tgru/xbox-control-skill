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
        self.power_on()

    def _url(self, path):
        return self.api_addr + ':' + str(self.api_port) + path   

    def power_on(self):
        ret = requests.get(
            self._url(
                "/device/{}/poweron".format(self.xbox_live_id)
            )
        )

def create_skill():
    return XboxControl()

