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
                n = int(self.get_response('What is your Customer I.D?'))

                cur.execute("SELECT * FROM Customer WHERE CustomerID = ?", (n,))
                cust = cur.fetchone()

                if(cust != None):
                    validId = 1
                else:
                    self.speak("Customer I.D. is not valid. Try again")

            answer = self.ask_yesno('You are requesting the account balance for {}. Is this you? (yes/no)'.format(cust[2]))
    
        
        self.speak('Your balance is ${}.'.format(cust[3]))
        addmoney = self.ask_yesno('Would you like to add money to your account? (yes/no)')

        if addmoney == "yes": 
            #amount = float(self.get_response("How much money would you like to add?"))
            #balance = amount + cust[3]
            amount = self.get_response("How much money would you like to add?")
            numlist = extract_numbers(amount)

            if len(numlist) == 2:
                dollars = str(int(numlist[0])) + "." + str(int(numlist[1]))
            else:
                dollars = str(numlist[0])

            balance = float(dollars) + cust[3]

            cur.execute("UPDATE Customer SET Balance = ? WHERE CustomerID = ?", (balance, n,))
            conn.commit()
            self.speak('Your balance is now ${}.'.format(balance))
        self.speak("Have a great day!")

        conn.close()


def create_skill():
    return CheckBalance()

