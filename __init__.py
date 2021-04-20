from mycroft import MycroftSkill, intent_file_handler
import sqlite3
from sqlite3 import Error


class CheckBalance(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('balance.check.intent')
    def handle_balance_check(self, message):
        database1 = "cubic.sql"

        # create a database connection
        conn = sqlite3.connect(database1)
        
        cur = conn.cursor()
        
        answer = "no"
        while (answer == "no"):
            n = int(self.get_response('What is your Customer I.D?'))

            cur.execute("SELECT * FROM Customer WHERE CustomerID = ?", (n,))
            cust = cur.fetchone()

            answer = self.ask_yesno('You are requesting the account balance for {}. Is this you? (yes/no)'.format(cust[2]))
    
        

        self.speak('Your balance is ${}.'.format(cust[3]))
        answer = self.ask_yesno('Would you like to add money to your account? (yes/no)')

        if answer == "yes" 
            balance = float(self.get_response("How much money would you like to add?"))
            balance += cust[3]
            cur.execute("UPDATE Customer SET Balance = ? WHERE CustomerID = ?", (balance, n,))
        else
            self.speak("Have a great day!")

        conn.close()


def create_skill():
    return CheckBalance()

