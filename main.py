from car import Car
from EV import EV

car1=Car("Toyota","Camry",2020)
#car2=Car("Honda","Civic",2019)
ev1=EV("Tesla","Model S",2022,100)
print(car1.brand)
car1.set_owner("Alice")
print(car1.get_owner())
print(ev1.brand)
ev1.set_owner("Charlie")
print(ev1.get_owner())
ev1.charge_battery()
car1.start_engine()
car1.show_info()
ev1.start_engine()
ev1.show_info()

cars=[car1,ev1]

for car in cars:
    car.start_engine()
    car.show_info()



