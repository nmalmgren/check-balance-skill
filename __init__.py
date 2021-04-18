from mycroft import MycroftSkill, intent_file_handler


class CheckBalance(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('balance.check.intent')
    def handle_balance_check(self, message):
        self.speak_dialog('balance.check')


def create_skill():
    return CheckBalance()

