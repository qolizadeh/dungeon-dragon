
import psycopg2

class Item:
    # attribute

    # constructor
    def __init__(self, name, count, price):
        self.name = name
        self.count = count
        self.price = price

    # properties
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if isinstance(value, str):
            if value.isalpha():
                self.__name = value
            else:
                raise ValueError("value must be alphabet.")
        else:
            raise TypeError("value must be str data type.")

    @property
    def count(self):
        return self.__count

    @count.setter
    def count(self, value):
        if isinstance(value, int):
            self.__count = value
        else:
            raise TypeError("value must be int data type.")

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if isinstance(value, int):
            self.__price = value
        else:
            raise TypeError("value must be int data type.")

    # method
    def show(self):
        dic = {}
        dic['shop'] = {}
        dic['shop'][self.name] = {}
        dic['shop'][self.name]['count'] = self.count
        dic['shop'][self.name]['price'] = self.price
        
        return dic

    # magic method
    def __add__(self, other):
        total = self.__count + other
        self.__count = total
        return total

    def __iadd__(self, other):
        if isinstance(other, int):
            self.__count = self.__count + other
            return self
        else:
            raise TypeError("other must be int data type.")

    # casting
    def __str__(self):
        return '{} {} {}'.format(self.__name, self.__count, self.price)

    def __int__(self):
        return self.__count

    def __float__(self):
        return float(self.__count)

    # representation of an object
    def __repr__(self):
        return '({}, {}, {})'.format(self.__name, self.__count,self.__price)

##############################################################################
##############################################################################

class Items:
    def __init__(self):
        self.__items = list()

    def add(self, item):
        if isinstance(item, Item):
            self.__items.append(item)
        else:
            raise TypeError("value must be Item class.")
        pass

    def WritetoFile(self, item):
        if isinstance(item, Item):
            with open("out.txt","a") as myfile:
                myfile.write(str(item)+"\n")
        else:
            raise TypeError("value must be Item class.")
        pass

    def WritetoDb(self, item):
        if isinstance(item, Item):
            con = psycopg2.connect("host='localhost' dbname='postgres' user='postgres' password='123456'")
            cur = con.cursor()
            cur.execute("SELECT * from SHOPPINGLIST")
            if (cur.fetchone()):
                pass
            else:
                cur.execute("CREATE TABLE SHOPPINGLIST(Id SERIAL,Name VARCHAR(20),Count INT,Price INT)")
            cur.execute("INSERT INTO SHOPPINGLIST (Name,Count,Price) VALUES ('{}',{},{})".
                        format(item.name,item.count,item.price))
            con.commit()
        else:
            raise TypeError("value must be Item class.")
        pass

    def show(self):
        return self.__items

    def __iter__(self):
        yield from self.__items

    def __contains__(self, item):
        for i in self:
            if item.name == i.name and item.count == i.count:
                return True
        return False

    def __add__(self, other):
        self.add(other)
        return self

    def __len__(self):
        return len(self.__items)

    def __str__(self):
        return str(self.__items)

##############################################################################
##############################################################################


while True:
    str_write = str(input("Write to Database(DB) or File(F):"))
    if (str_write.lower() == "db" or str_write == "f"):
        break
    else:
        print("String is not valid.")
        continue

items = Items()

while True:
    name = str(input("Enter name(Enter \"EXIT\" for Exit and Enter \"SHOW\" for Show json):"))
    if (name.lower() == "exit"):
        break
    elif (name.lower() == "show"):
        print(items)
    else:
        count = int(input("Enter count:"))
        price = int(input("Enter price:"))

        item = Item(name, count, price)
        items.add(item)
        #print(item)
        #print(items)

        if (str_write.lower() == "f"):
            items.WritetoFile(item)
        elif (str_write.lower() == "db"):
            items.WritetoDb(item)
        else:
            pass