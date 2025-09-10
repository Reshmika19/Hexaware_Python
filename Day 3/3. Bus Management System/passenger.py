class Passenger:
    def __init__(self, name, ticket_number, destination):
        self.name = name
        self.ticket_number = ticket_number
        self.destination = destination

    def display_details(self):
        print(f"Passenger: {self.name}, Ticket: {self.ticket_number}, Destination: {self.destination}")
