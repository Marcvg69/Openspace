import random
from typing import List
from utils.table import Table  # Importing the Table class from the table.py file

class OpenSpace:
    def __init__(self, number_of_tables: int, seats_per_table: int):
        """
        Initialize the OpenSpace with a specified number of tables and seats per table.
        Each table is an instance of the Table class.
        """
        self.tables = [Table(seats_per_table) for _ in range(number_of_tables)]

    def organize(self, names: List[str]):
        """
        Randomly assign people (names) to seats in the available tables.

        Steps:
        1. Shuffle the list of names to ensure random distribution.
        2. Iterate through each name.
        3. For each name, try to assign them to a seat in the first available table.
        4. Break the inner loop once a seat is successfully assigned.
        """
        random.shuffle(names)  # Randomize the order of people
        for name in names:
            for table in self.tables:
                if table.assign_seat(name):  # Attempt to assign the person to a seat
                    break  # Stop checking other tables once assigned

    def display(self):
        """
        Print out the seating arrangement in a readable format.

        For each table:
        - Print the table number.
        - Print each seat's occupant, or "Empty" if no one is assigned.
        """
        for i, table in enumerate(self.tables, 1):  # Start numbering from 1
            print(f"Table {i}:")
            for seat in table.seats:
                occupant = seat.occupant if seat.occupant else "Empty"
                print(f"  - {occupant}")

    def store(self, filename: str):
        """
        Store the current seating arrangement into an Excel file.

        Steps:
        1. Create a list of dictionaries representing table number, seat number, and occupant.
        2. Convert the list into a Pandas DataFrame.
        3. Save the DataFrame to an Excel file with the specified filename.
        """
        import pandas as pd
        data = []  # This will hold all seating data
        for table_idx, table in enumerate(self.tables, 1):  # Start table numbering from 1
            for seat_idx, seat in enumerate(table.seats, 1):  # Start seat numbering from 1
                data.append({
                    "Table": table_idx,
                    "Seat": seat_idx,
                    "Occupant": seat.occupant or "Empty"
                })
        
        df = pd.DataFrame(data)  # Convert list of dicts to a DataFrame
        df.to_excel(filename, index=False)  # Export the DataFrame to an Excel file

