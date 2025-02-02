class Coffee:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name 
    
    @name.setter
    def name(self, name): #change these to 'value' if not working
        if isinstance(name, str) and len(name) >= 3 and not hasattr(self, 'name'): #checks type is string and NOT hasattr always returns false after init
            self._name = name
        else:
            raise Exception('name already exists or shorter than 3 characters')
        
    def orders(self):
        return [order for order in Order.all if order.coffee == self] #aids num of orders per coffee by selecting all orders of same type
    
    def customers(self):
        return list(set([order.customer for order in Order.all if order.coffee == self])) #list set to make unique cusomters
    
    def num_orders(self):
        return len(self.orders())
    
    def average_price(self):
        return sum([order.price for order in self.orders()]) / len([order.price for order in self.orders()])

class Customer:

    @classmethod
    def most_aficionado(cls, coffee):
        cust_spend = {}
        for customer in coffee.customers():
            cust_spend[customer] = sum([order.price for order in coffee.orders() if order.customer == customer])
        return max(cust_spend, key=cust_spend.get)

    def __init__(self, name):
        self.name = name


    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and (1 <= len(name) <= 15): # again change name to value if fails
            self._name = name
        else:
            raise Exception('name is not a string or too long/short')
        
    def orders(self):
        return [order for order in Order.all if order.customer == self]
    
    def coffees(self):
        return list(set([order.coffee for order in Order.all if order.customer == self]))
    
    def create_order(self, coffee, price):
        return Order(self, coffee, price)
    
class Order:

    all = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order.all.append(self) #alt self.__class__.all.append(self)

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, price):
        if type(price) == float and (1.0 <= price <= 10.0) and not hasattr(self, 'price'):
            self._price = price
        else:
            raise Exception('invalid price')
        
    @property
    def customer(self):
        return self._customer
    
    @customer.setter
    def customer(self, customer):
        if isinstance(customer, Customer):
            self._customer = customer
        else:
            raise Exception("invalid customer")
        
    @property
    def coffee(self):
        return self._coffee
    
    @coffee.setter
    def coffee(self, coffee):
        if isinstance(coffee, Coffee):
            self._coffee = coffee
        else:
            raise Exception("invalid coffee")