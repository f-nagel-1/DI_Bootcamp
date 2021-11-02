class Something():

    """Some documentation to explain."""
    def __init__(self):
        pass

    def __abs__(self):
        print("gives absolute number")

    def __int__(self):
        print("turns it into an integar")

    def __input__(self):
        print("prompts for input")

newInstance = Something()

print(newInstance.__doc__)
print(Something.__doc__)

Something().__abs__()
Something().__int__()
newInstance.__input__()

######
class Currency():
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount
    
    def __str__(self):
        print(self.amount + " " + self.currency)

    def __int__(self):
        print(self.amount)

    def __repr__(self):
        print(self.amount + " " + self.currency)

c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)