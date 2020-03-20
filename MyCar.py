from car import Car,ElectricCar #import特定模組
import car  #import整個car模組

car1=Car(2018,"toyota","white")
car1.get_name()
car1.update_mile(90)
car1.get_miles()

ecar=ElectricCar(2019,"BMW","blue")
ecar.get_name()
ecar.get_battery()

car1=car.Car(30,"ford","black")
car1.get_name()