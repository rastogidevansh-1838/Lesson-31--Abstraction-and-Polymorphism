class BMW():
    def max_speed(Self):
        print("The max speed of this car is 300kmph.")
    def fuel_type(Self):
        print("This is a petrol vehicle.")
class Ferrari():
    def max_speed(Self):
        print("The max speed of this car is 280kmph.")
    def fuel_type(Self):
        print("This is a EV vehicle.")
vehicle_BMW = BMW()
vehicle_Ferrari = Ferrari()
for vehicle in(vehicle_BMW, vehicle_Ferrari):
    vehicle.max_speed()
    vehicle.fuel_type()