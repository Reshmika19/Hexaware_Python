class Route:
    def __init__(self, route_number, start_location, end_location, stops=None):
        self.route_number = route_number
        self.start_location = start_location
        self.end_location = end_location
        self.stops = stops if stops else []
        self.bus = None

    def assign_bus(self, bus):
        self.bus = bus
        print(f"Bus #{bus.bus_number} assigned to Route {self.route_number} ({self.start_location} → {self.end_location})")

    def display_route(self):
        print(f"Route {self.route_number}: {self.start_location} → {self.end_location}")
        if self.stops:
            print("Stops:", ", ".join(self.stops))
