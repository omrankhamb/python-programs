class Car:
    def __init__(self):
        print("Inside Car Garage")

    def Engine(self):
        print("2000 HorsePwer")

    def __del__(self):
        print("Inside Car Destructor")

class Truck:
    def __init__(self):
        print("Inside Truck Garage")

    def Engine(self):
        print("4000 HorsePower Engine")

    def __del__(self):
        print("Inside Truck destructor")

class Demo(Truck,Car):
    def __init__(self):
        Car.__init__(self)
        Truck.__init__(self)
        print("Inside Demo Constructor")
    
    def __del__(self):
        print("Inside Demo Destructor")
        Car.__del__(self)
        Truck.__del__(self)
    
    
dobj = Demo()

        
        
    

