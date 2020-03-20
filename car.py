class Dog():    #Dog class
    def __init__(self,name,age):    #建立__init__方法，並且放入三個參數；self是必要的且必須放在其他參數前面
        self.name = name    #將實例來存取的變數稱之屬性
        self.age =age
    
    def eat(self):  #eat method
        print(self.name + " is eating")

    def sleep(self):    #sleep method
        print(self.name + " is sleeping")

dog1 = Dog("snoopy",15)     #建立dog1 instance
print("My dog's name is " + dog1.name + " and it's " + str(dog1.age) + " years old.")   #dog1實例中的name屬性與Dog類別中的self.name的屬性相同

dog1.eat()  #寫入實例的name和要呼叫的方法
dog1.sleep()

#父類別
class Car():
    def __init__(self,year,brand,color):
        self.year = year
        self.brand = brand
        self.color = color
        self.miles = 0
    
    def get_name(self):
        print(str(self.year)+" "+self.brand)

    def get_miles(self):
        print("Your "+self.brand+" has "+str(self.miles)+" miles on it")

    def update_mile(self,newmile):
        self.miles = newmile

    def add_mile(self,addmile):
        self.miles += addmile

    def fill_gas(self):
        print("This car need a gas tank")

#子類別
class ElectricCar(Car):
    def __init__(self,year,brand,color):
        super().__init__(year,brand,color) #呼叫父類別的__init__方法，讓子類別含有父類別的屬性    
        self.battery_size = 100
    
    def get_battery(self):
        print("Your "+self.brand+" has "+str(self.battery_size)+" - KWh battery")
    
    def fill_gas(self):
        print("This car doesn't need a gas tank")
car1=Car("10","Ferrari","red")
car1.miles = 100
car1.get_miles()
car1.update_mile(150)
car1.get_miles()
car1.add_mile(10)
car1.get_miles()

ecar=ElectricCar(2018,"Porsche","yellow")
ecar.get_name()
ecar.get_battery()
ecar.fill_gas()