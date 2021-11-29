#make classes
class Customer:
    def __init__(self, name, address):
        self.name = name
        self.address = address


class Order:
    quantity:list[OrderDetail]
    taxStatus:list[OrderDetail]
    def __init__(self, date, status):
        self.date = date
        self.status = status
        self.quantity=[]
        self.taxStatus=[]
# make lists for class data member
        self.subTotalList = []
        self.taxList = []
        self.weightList = []
#append class member values to list
#append class member values belonging to each object(calcsubtotal/calctax/calcweight etc) to list of that object
    def calcSubTotal(self, detail):
        self.subTotalList.append(detail.calcSubTotal())
        return sum(self.subTotalList)

    def calcTax(self, detail):
        self.taxList.append(detail.calcTax())
        return sum(self.taxList)

    def calcTotal(self):
        return self.calcSubTotal() - self.calcTax()

    def calcWeight(self, detail):
        self.weightList.append(detail.calcWeight())
        return sum(self.weightList)

    def calcWeightMoney(self):
        return sum(self.weightList)


class OrderDetail:
    def __init__(self, quantity, taxStatus):
        self.quantity = quantity
        self.taxStatus = taxStatus
#check if item is out of stock/ if not out of stock, return subtotal for item
    def calcSubTotal(self, item):
        if self.taxStatus=="out of stock" or self.quantity > item.inStock():
            return "There's not enough item in stock"
        else:
            return self.quantity * item.getPriceForQuantity()

    def calcWeight(self, item):
        return item.shippingWeight * self.quantity

    def calcTax(self, item):
        return item.getTax() * self.calcSubTotal(item) * self.quantity/100


class Item:
    def __init__(self, shippingWeight, description):
        self.shippingWeight = shippingWeight
        self.description = description
#enter format of input: iteminstock,price,tax for each item.
    def getPriceForQuantity(self):
        a = self.description
        a = a.split(",")
        return (a[1])

    def getTax(self):
        a = self.description
        a = a.split(",")
        return (a[2])

    def inStock(self):
        a = self.description
        a = a.split(",")
        return (a[0])

#check if customer can pay and return the transaction change
class Payment:
    def __int__(self, amount):
        self.amount = amount

    def payMoney(self, order):
        a = self.amount
        b = order.calcTotal()
        if a < b:
            print("Your fund is insufficient")
        else:
            print("Thank you for your patronage! Here's the change:", b - a)


class Cash(Payment):
    def __init__(self, amount, cashTendered):
        super().__init__(amount)
        self.cashTendered = cashTendered
    def outputcashtendered(self):
        return self.cashTendered

#check customer card authorization for class check and credit and return statement
class Check(Payment):
    def __init__(self, amount, name, bankID):
        super().__init__(amount)
        self.name = name
        self.bankID = bankID

    def authorized(self):
        check_author = input("authorized(press x)/ not authorized (press y)")
        if check_author == "x":
            return 0
        else:
            return 1

    def pay(self):
        if self.authorized() == 0:
            super().pay()
        else:
            print("invalid user")


class Credit(Payment):
    def __init__(self, amount, number, type, expDate):
        super().__init__(amount)
        self.number = number
        self.type = type
        self.expDate = expDate

    def authorized(self):
        pass

    def pay(self):
        pass


