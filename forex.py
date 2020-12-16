
class Forex:
    
    def __init__(self, curr_from, curr_to, amt):
        """Setup params of currency and amt for Forex class"""
        self.curr_from = curr_from
        self.curr_to = curr_to
        self.amt = amt
    

    def check_valid_curr(self, curr):
        """check if currency is 3 LETTERS"""
        
        try:
            if (len(curr) == 3):
                return True
            else:
                return False
        #how to test for except?
        except:
            print("currency is not 3 chars long")
            

    # def check_amt(self, amt){
    #     """check if amt has the correct decimal places. return T/F"""
    #     deci_amt = Decimal(str(amt)) % 1

    # }


