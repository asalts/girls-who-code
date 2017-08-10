class vehicle:

    def __init__(self, name):
        self.name = name
        self.wheels = 0
        self.ignition = False
        self.passengers = []
        self.wipersOn = False

    def add_passenger(self, passenger):
        self.passengers.append(passenger)

def main():
    car = vehicle("Prius")
    print(car.name)
    car.add_passenger("Gabby")
    car.add_passenger("Devki")
    for seat in car.passengers:
        print(("{} is great!").format(seat))
    if car.wipersOn == False:
        print ("The windshield wipers are off.")

main()
