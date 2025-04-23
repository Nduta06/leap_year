class SimpleClass:
    ...
"""
class Person:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname

    def printname(self):
        print(self.fname,self.lname)


person_p1= Person("John","Doe")
person_p1.printname()


person_p2 = Person("Patience","Nduta")
person_p2.printname()


class Classey:
    varia=2


    def method(self ):
        print(self.varia)


object_one =Classey()
object_two = Classey()

object_one.varia = 3
object_two.varia = 5

print(object_one.varia)



class Transport:
    def __init__(self, air, water):
#init is the first function created when a class is being initiated. Self is used to access parameters.
      self.air = air
      self.water = water

Transport_t1 = Transport("Beluga","Hovercraft")
Transport_t2 = Transport("Jet","Boat")

print(Transport_t1.air, Transport_t1.water)
print(Transport_t2.air, Transport_t2.water)

"""


class ShoppingCart:
    def __init__(self):
        self.items = []
    def add_item(self,item_name,quantity):
        item =(item_name,quantity)
        self.items.append(item)

    def remove_item(self,item_name):
        for item in self.items:
            if item[0] == item_name:
                self.items.remove(item)
                break

    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item[1]
        return total

cart = ShoppingCart()

print("Current items in cart:")
cart.add_item("kiwi",100)
cart.add_item("Papaya",200)
cart.add_item("Orange",78)


for item in cart.items:
    print(item[0], "-" ,item[1])


total_quantity = cart.calculate_total()
print("Total Quantity : ",total_quantity)



