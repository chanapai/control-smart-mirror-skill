from mycroft import MycroftSkill, intent_file_handler


class ControlSmartMirror(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

"""
    @intent_file_handler('mirror.smart.control.intent')
    def handle_mirror_smart_control(self, message):
        self.speak_dialog('mirror.smart.control')"""

    @intent_handler('turn.on.intent')
    def handle_turn_on_intent(self, message):
        self.log.debug("Turn on intent on entity: "+message.data.get("entity"))
        #module = message.data.get("entity")
       

    @intent_handler('turn.off.intent')
    def handle_turn_off_intent(self, message):
         self.log.debug("Turn of intent on entity: "+message.data.get("entity"))
        # module = message.data.get("entity")

    
def create_skill():
    return ControlSmartMirror()

