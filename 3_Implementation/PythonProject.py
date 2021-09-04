# importing regular expression Syntax
import re
# importing the modules
from datetime import date
import self as self
from dateutil.relativedelta import relativedelta
# importing the modules


# base class
class Product:
    name = ""

    # printing the class in the constructor
    def __init__(self):
        print("super class Product by Grocery Raja")

    # getExpDate() returns the expiry date of product
    # since every product has different expiry date
    # therefore this method is overridden by child classes
    def getExpDate():
        # gives exp date
        print("Expiry date")
        pass


# derived class 1
class Snack(Product):
    # months
    shelfLife = 6
    price = 0

    # constructor - initializing variables
    def __init__(self, name, price):
        self.name = name
        self.price = price

    # prints the Snack product details
    def printDetails(self):
        print("name : " + self.name)
        print("price : " + str(self.price))
        print("shelf life : " + str(self.shelfLife) + " months")

    # calculates the expiry date using relativedelta library and returns
    def getExpDate(self, pkdDate):
        expDate = pkdDate + relativedelta(months=self.shelfLife)
        return expDate


# derived class 2
class Beverage(Product):
    # 2 years
    shelfLife = 2
    price = 0

    # constructor - initializing variables
    def __init__(self, name, price):
        self.name = name
        self.price = price

    # prints the Beverage product details
    def printDetails(self):
        print("name : " + self.name)
        print("price : " + str(self.price))
        print("shelf life : " + str(self.shelfLife) + " years")

    # calculates the expiry date using relativedelta
    # library and returns
    def getExpDate(self, pkdDate):
        expDate = pkdDate + relativedelta(years=self.shelfLife)
        return expDate


# derived class 3
class Staples(Product):
    # 1 year
    shelfLife = 1
    price = 0

    # constructor - initializing variables
    def __init__(self, name, price):
        self.name = name
        self.price = price

    # prints the Staples product details
    def printDetails(self):
        print("name : " + self.name)
        print("price : " + str(self.price))
        print("shelf life : " + str(self.shelfLife) + " year")

    # calculates the expiry date using relativedelta
    # library and returns
    def getExpDate(self, pkdDate):
        expDate = pkdDate + relativedelta(years=self.shelfLife)
        return expDate

'''
#  Class for Data Encapsulation
class ProductID:
    def __init__(self):
        self.__Product_Snacks = 500700200


# Creating a derived class for data Encapsulation
class Hidden(ProductID):
    def __init__(self):
        # Calling constructor of
        # ProductID
        ProductID.__init__(self)
        print("Calling private member of base class: ")
        print(self.__Product_Snacks)

# Driver code
obj1 = ProductID()
print(obj1.Product_Snacks)
'''
print("----------------------------------------------------------------------Welcome to Grocery Raja store-------------------------------------------------------------------------")
# Usage of Regex expression
print("*** To Differentiate and See that only Email is shown if anything by mistake is been writen shouldn't be seen using regex ***" )
Hello = '''nayaksambit99@gmail.com SNOil.01'''
pattern = r'[a-z]+[0-9]*[a-z]*@[a-z]+\.com'
match = re.finditer(pattern, Hello)
for m in match:
    print(m)
print("\n$$$ Review of Customer converted from Paragraph to Sentence  using regex $$$\n")
product_review = ''' Oh my goodness... You know, this place has very good groceries at reasonable price for all items 
like Cookies, Chips , Oil Coffee and so on. I have saved a lot both time and money by shopping through Grocery Raja.'''

sentence_pattern = re.compile(r'(.*?\.)(\s|$)', re.DOTALL)
matches = sentence_pattern.findall(product_review)
sentences = [match[0] for match in matches]

word_pattern = re.compile(r"([\w\-']+)([\s,.])?")
for sentence in sentences:
    matches = word_pattern.findall(sentence)
    words = [match[0] for match in matches]
    print(words)

# Usage of Polymorphism For Advertisement and Initial scheme for customers
class Advertisment:
    def __init__(self, name, Date):
        self.name = name
        self.Date = Date

    def info(self):
        print(f"20% off on Rice and 40% off on Nestle Coffee {self.name}. This offer is available for {self.Date} hours on 25th December .")

    def make_Publicity(self):
        print("\n~!!! Mega Sale by Grocery Raja !!!~\n")

class Features:
    def __init__(self, name,Date):
        self.name = name
        self.Date = Date

    def info(self):
        print(f" Features of this Store online Shopping,UPI,PAYTM,GPAY,PHONE PAY, ACCEPTED {self.name}.Starts from {self.Date} December of this month.")
    def make_Publicity(self):
        print("~## To Promote Cashless Transaction ##~")


AD1 = Advertisment("Only via ordering Online", 2.5)
FE1 = Features("10 Percent Extra off Via (cashless Transaction)", 20)

for Store in (AD1, FE1):
    Store.make_Publicity()
    Store.info()
    Store.make_Publicity()

class Price_exception(Exception):
    def __init__(self,message ="Price is not Valid"):
        super().__init__(self.message)

def main():
    print("\nDerived Classes for Snacks\n")
    print("Enter an Input value more than 0 or will show Error because of Invalid Price of Snacks")
    price1=int(input())
    if price1<=0:
        raise Price_exception()
    else:
        s = Snack('cookies', price1)
        s.printDetails()
        print(s.name + " will expire on " + str(s.getExpDate(date(2019, 10, 3))))
    # yyyy-mm-dd
    p = Product()
    print("\nDerived Classes for Staples\n")
    print("Enter an Input value more than 0 or will show Error because of Invalid Price of Staples")
    price1 = int(input())
    if price1 <= 0:
        raise Price_exception()
    else:
        st = Staples('rice', price1)
        st.printDetails()
        print(st.name + " will expire on " + str(st.getExpDate(date(2020, 1, 23))))
    print("\nDerived Classes for Beverages\n")
    print("Enter an Input value more than 0 or will show Error because of Invalid Price of Staples")
    price1 = int(input())
    if price1 <= 0:
        raise Price_exception()
    else:
        b = Beverage('coffee', price1)
        b.printDetails()
        print(b.name + " will expire on " + str(b.getExpDate(date(2018, 12, 17))))
if __name__ == '__main__':
    main()
