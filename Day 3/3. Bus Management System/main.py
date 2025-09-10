'''
3. Bus Management System
Problem Statement
You are tasked with designing a Bus Management System for a transport company. The system
should manage buses, drivers, routes, and passengers efficiently.
The goal is to sim
'''

from driver import Driver
from passenger import Passenger
from route import Route
from bus import Bus

# driver
driver_john = Driver("Arjun", "D101", "LIC123")

# bus
bus101 = Bus(101, 40)

# Assigning driver
bus101.assign_driver(driver_john)

# route
route1 = Route("R1", "Downtown", "Uptown", ["Central Park", "Main Square"])
bus101.assign_route(route1)

# passengers
reshh = Passenger("Reshh", "T001", "Central Park")
mika = Passenger("Mika", "T002", "Main Square")
nilla = Passenger("Nilla", "T003", "Uptown")

# Adding passengers
bus101.add_passenger(reshh)
bus101.add_passenger(mika)
bus101.add_passenger(nilla)

# Start trip
bus101.start_trip()

# Passengers leave at stops
bus101.remove_passenger("Reshh")
bus101.remove_passenger("Mika")

# End trip
bus101.end_trip()

# Display final status
bus101.display_status()
