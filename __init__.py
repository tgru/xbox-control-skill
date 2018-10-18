from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_handler

class XboxControl(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_handler(IntentBuilder('').require('device').require('switch.state').require('state.on'))
    def handle_control_xbox(self, message):
        self.power_on()

    def power_on(self):
        self.speak_dialog('not.implemented.yet')

def create_skill():
    return XboxControl()

