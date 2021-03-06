# Object Oriented Programming

class Fib():
    """A Fibonacci number.

    >>> start = Fib()
    >>> start
    0
    >>> start.next()
    1
    >>> start.next().next()
    1
    >>> start.next().next().next()
    2
    >>> start.next().next().next().next()
    3
    >>> start.next().next().next().next().next()
    5
    >>> start.next().next().next().next().next().next()
    8
    >>> start.next().next().next().next().next().next() # Ensure start isn't changed
    8
    """

    def __init__(self, value=0):
        self.value = value

    def next(self):
        "*** YOUR CODE HERE ***"
        if self.value == 0: # Base case
            self.future = 1

        cur, fut = self.future, self.value + self.future

        new_fib = Fib(value=cur)
        new_fib.future = fut
        
        return new_fib

    def __repr__(self):
        return str(self.value)

class VendingMachine:
    """A vending machine that vends some product for some price.

    >>> v = VendingMachine('candy', 10)
    >>> v.vend()
    'Machine is out of stock.'
    >>> v.deposit(15)
    'Machine is out of stock. Here is your $15.'
    >>> v.restock(2)
    'Current candy stock: 2'
    >>> v.vend()
    'You must deposit $10 more.'
    >>> v.deposit(7)
    'Current balance: $7'
    >>> v.vend()
    'You must deposit $3 more.'
    >>> v.deposit(5)
    'Current balance: $12'
    >>> v.vend()
    'Here is your candy and $2 change.'
    >>> v.deposit(10)
    'Current balance: $10'
    >>> v.vend()
    'Here is your candy.'
    >>> v.deposit(15)
    'Machine is out of stock. Here is your $15.'

    >>> w = VendingMachine('soda', 2)
    >>> w.restock(3)
    'Current soda stock: 3'
    >>> w.restock(3)
    'Current soda stock: 6'
    >>> w.deposit(2)
    'Current balance: $2'
    >>> w.vend()
    'Here is your soda.'
    """
    "*** YOUR CODE HERE ***"
    remaining = 0
    balance = 0

    def __init__(self, item, price):
        self.item = item
        self.price = price

    def vend(self):
        if self.remaining:
            if self.balance == self.price:
                self.balance -= self.price
                self.remaining -= 1
                return 'Here is your {0}.'.format(self.item)
            elif self.balance > self.price:
                change = self.balance - self.price
                self.balance = 0
                self.remaining -= 1
                return 'Here is your {0} and ${1} change.'.format(self.item, change)
            else:
                return 'You must deposit ${0} more.'.format(self.price - self.balance)
        else:
            return 'Machine is out of stock.'

    def deposit(self, amount):
        if self.remaining:
            self.balance += amount
            return 'Current balance: ${0}'.format(self.balance)
        else:
            return 'Machine is out of stock. Here is your ${0}.'.format(amount)

    def restock(self, item_count):
        self.remaining += item_count
        return 'Current {0} stock: {1}'.format(self.item, self.remaining)