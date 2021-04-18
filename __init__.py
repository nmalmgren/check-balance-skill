from mycroft import MycroftSkill, intent_file_handler
import sqlite3
from sqlite3 import Error


class CheckBalance(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('balance.check.intent')
    def handle_balance_check(self, message):
        #database1 = "cubic.sql"

        # create a database connection
        #conn = sqlite3.connect(database1)
        
        #cur = conn.cursor()

        #n = int(self.get_response('What is your Customer ID?'))

        #cur.execute("SELECT * FROM Customer WHERE CustomerID = ?", n,))
        #cust = cur.fetchone()

        #self.speak('Your balance is ${}.'.format(cust[3]))

        self.speak_dialog('balance.check')
        #conn.close()


def create_skill():
    return CheckBalance()

