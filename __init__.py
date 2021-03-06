from mycroft import MycroftSkill, intent_file_handler
import sqlite3
from sqlite3 import Error
from mycroft.util.parse import *

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
            cust = []

            validId = 0
            while (validId == 0):
                n = int(self.get_response('What is your Customer I.D?').replace(" ", ""))

                cur.execute("SELECT * FROM Customer WHERE CustomerID = ?", (n,))
                cust = cur.fetchone()

                if(cust != None):
                    validId = 1
                else:
                    proceed = self.ask_yesno("Customer I.D. is not valid. Would you like to try again? (yes/no)")

                    if proceed == "no":
                        self.speak("Have a great day!")
                        return

            answer = self.ask_yesno('You are requesting the account balance for {}. Is this you? (yes/no)'.format(cust[2]))
    
        
        self.speak('Your balance is ${}.'.format(cust[3]))
        addmoney = self.ask_yesno('Would you like to add money to your account? (yes/no)')

        if addmoney == "yes": 
            amount = round((float(self.get_response("How much money would you like to add?")[1:])),2)
            
            balance = round((amount + cust[3]), 2)

            cur.execute("UPDATE Customer SET Balance = ? WHERE CustomerID = ?", (balance, n,))
            conn.commit()

            self.speak('Your balance is now ${}.'.format(balance))

        self.speak("Have a great day!")

        conn.close()


def create_skill():
    return CheckBalance()

