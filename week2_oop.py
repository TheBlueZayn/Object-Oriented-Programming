import collections

# Create class: Transaction
class Transaction:
    # create a class attribute
    all = []
    dates = []
    names = []
    debit = []
    credit = []
    

    num_of_tran = 0

    # Define initiation, add instance attributes
    # Validate data types
    def __init__(self, date: str, name: str, reference: str, debit: float, credit: float):


        # Run validations to the received arguments
        assert debit >= 0, f"Debit {debit} is not greater than or equal to zero!"
        assert credit >= 0, f"Credit {credit} is not greater than or equal to zero!"
        

        # Assign to self, objects
        self.date = date
        self.name = name
        self.reference = reference
        self.debit = debit
        self.credit = credit
        

        
        # Add all transactions
        Transaction.all.append(self)
        Transaction.dates.append(self.date)
        Transaction.names.append(self.name)
        Transaction.debit.append(self.debit)
        Transaction.credit.append(self.credit)

        #increment
        Transaction.num_of_tran += 1

    # Define methods
    @classmethod
    def freq_transactions(cls):
        frequency = collections.Counter(Transaction.names)
        return list(frequency)[0]

    @staticmethod
    def total_count():
        return Transaction.num_of_tran


    def start_date():
        return Transaction.dates[0]

    def end_date():
        return Transaction.dates[-1]    

    
    def credit_count():
        total_credit = sum(c for c in Transaction.credit)  
        return total_credit 

    
    def debit_count():
        total_debit = sum(c for c in Transaction.debit)  
        return total_debit  

    def net_profit():
        total_credit = sum(c for c in Transaction.credit) 
        total_debit = sum(c for c in Transaction.debit) 
        net = (total_credit - total_debit)
        return "The net profit is: {}".format(net)


    
    def __repr__(self):
        return f"{self.__class__.__name__}('{self.date}', '{self.name}', '{self.reference}', '{self.debit}', '{self.credit}')" 




        


