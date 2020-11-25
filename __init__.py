from mycroft import MycroftSkill, intent_file_handler


class ControlSmartMirror(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('mirror.smart.control.intent')
    def handle_mirror_smart_control(self, message):
        self.speak_dialog('mirror.smart.control')


def create_skill():
    return ControlSmartMirror()

