class Bus:
    def __init__(self, bus_number, capacity):
        self.bus_number = bus_number
        self.capacity = capacity
        self.driver = None
        self.route = None
        self.__passengers = []  

    def assign_driver(self, driver):
        self.driver = driver
        print(f"Driver {driver.name} assigned to Bus {self.bus_number}")

    def assign_route(self, route):
        self.route = route
        route.assign_bus(self)

    def add_passenger(self, passenger):
        if len(self.__passengers) < self.capacity:
            self.__passengers.append(passenger)
            print(f"Passenger {passenger.name} boarded Bus {self.bus_number}")
        else:
            print(f"Bus {self.bus_number} is full. Cannot add {passenger.name}.")

    def remove_passenger(self, passenger_name):
        for p in self.__passengers:
            if p.name == passenger_name:
                self.__passengers.remove(p)
                print(f"Passenger {p.name} left Bus {self.bus_number}")
                return
        print(f"Passenger {passenger_name} not found on Bus {self.bus_number}")

    def start_trip(self):
        if not self.driver:
            print(f"Bus {self.bus_number} cannot start trip: No driver assigned.")
            return
        if not self.route:
            print(f"Bus {self.bus_number} cannot start trip: No route assigned.")
            return
        print(f"Bus {self.bus_number} starting trip with Driver {self.driver.name} on Route {self.route.route_number}.")
        self.display_status()

    def end_trip(self):
        print(f"Bus {self.bus_number} trip ended. Clearing passengers.")
        self.__passengers.clear()

    def display_status(self):
        print(f"\n--------- Bus {self.bus_number} Status ---------")
        if self.driver:
            print(f"Driver: {self.driver.name}")
        else:
            print("No driver assigned.")
        if self.route:
            print(f"Route: {self.route.start_location} → {self.route.end_location}")
        else:
            print("No route assigned.")
        print(f"Passengers ({len(self.__passengers)}/{self.capacity}): {[p.name for p in self.__passengers]}")
        print(f"Seats available: {self.capacity - len(self.__passengers)}")
