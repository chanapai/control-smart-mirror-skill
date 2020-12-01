from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_handler

class ControlSmartMirror(MycroftSkill):
    def __init__(self):
        super().__init__()
        self.learning = True

    def initialize(self):
        my_setting = self.settings.get('my_setting')
    """
    @intent_file_handler('mirror.smart.control.intent')
    def handle_mirror_smart_control(self, message):
        self.speak_dialog('mirror.smart.control')"""

    '''@intent_handler('hide.intent')
    def handle_turn_on_intent(self, message):
        #self.log.debug("Turn on intent on entity: "+message.data.get("entity"))
        self.speak_dialog("done.dialog")
        #module = message.data.get("entity")
    '''

    @intent_handler('show.intent')
    def handle_turn_off_intent(self, message):
         #self.log.debug("Turn of intent on entity: "+message.data.get("entity"))
         self.speak_dialog("done.dialog")
        # module = message.data.get("entity")


    @intent_handler(IntentBuilder('HelloSmartMirror').require('HelloSmartMirror'))
    def handle_hello_smart_mirror_intent(self, message):
        self.speak_dialog("done.dialog")


    def stop(self):
        pass

def create_skill():
    return ControlSmartMirror()

