from datetime import datetime

# TODO: Add code here my code

class Transaction:
    SELL:int = 1
    SUPPLY:int = 2
    def __init__(self,type: int, copies:int):
        self.type = type
        self.copies = copies
        self.date = datetime.now()