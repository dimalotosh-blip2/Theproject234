class Vehicle:
    
    pass

class Car(Vehicle):
    pass


my_car = Car()

print(isinstance(my_car, Car))  
print(isinstance(my_car, Vehicle))  
print(isinstance(my_car, int))    
