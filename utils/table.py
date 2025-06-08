# Define a Seat class to represent an individual seat at a table
class Seat:
    def __init__(self):
        # Each seat starts out as free and has no occupant
        self.free = True
        self.occupant = None
    
    def set_occupant(self, name):
        # Assign an occupant to the seat only if it is free
        if self.free:
            self.occupant = name
            self.free = False  # Mark the seat as occupied
    
    def remove_occupant(self):
        # Remove the current occupant from the seat
        occupant = self.occupant
        self.occupant = None
        self.free = True  # Mark the seat as free again
        return occupant  # Return the name of the person who was removed

# Define a Table class to manage a collection of seats
class Table:
    def __init__(self, capacity: int):
        self.capacity = capacity  # Total number of seats at the table
        # Create a list of Seat objects based on the given capacity
        self.seats = [Seat() for _ in range(capacity)]
    
    def has_free_spot(self) -> bool:
        # Check if any seat is still free (i.e., not yet occupied)
        return any(seat.free for seat in self.seats)
    
    def assign_seat(self, name: str):
        # Try to assign a person to the first available free seat
        for seat in self.seats:
            if seat.free:
                seat.set_occupant(name)
                return True  # Successfully assigned
        return False  # No free seat was found
    
    def capacity_left(self) -> int:
        # Count how many seats are still free
        return sum(1 for seat in self.seats if seat.free)
