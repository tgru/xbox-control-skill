from mycroft import MycroftSkill, intent_file_handler


class XboxControl(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('control.xbox.intent')
    def handle_control_xbox(self, message):
        self.speak_dialog('control.xbox')


def create_skill():
    return XboxControl()

