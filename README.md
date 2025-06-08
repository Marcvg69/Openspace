# OpenSpace-Organizer

## Project Background
The **OpenSpace-Organizer** is a Python program designed to help employees in an open office space **randomly assign seating arrangements** each day. This is part of a company initiative to foster better team interaction by seating colleagues in different spots every day. The program reads a list of colleagues from a **CSV file**, randomly assigns them to **tables with seats**, and outputs the results in an Excel file.

## Features
- **Random seat assignment**: Automatically assigns colleagues to tables.
- **Dynamic table and seat management**: Handles overflow by creating additional tables if necessary.
- **CSV Integration**: Reads colleague data from a CSV file and writes the seating arrangement back to an Excel file called seating_arrangement.xlsx
- **Interactive display**: Displays the seating arrangement on the console and indicates Empty seats left at the table

## Libraries Used
- **pandas**: For reading/writing CSV and Excel files.
- **openpyxl**: For Excel file handling.
- **random**: For random seat assignment.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/hajersmiai/Bauman9_Open_Space/
    ```

2. Install required dependencies:

    ```bash
    pip install pandas openpyxl
    ```

## Usage

1. Prepare the `colleagues.csv` file containing the list of names.
2. Run the program using the command:

    ```bash
    python3 main.py colleagues.csv   #(or pass any other file name as an argument)
    ```

3. The seating arrangement will be displayed in the terminal, and the result will be saved in `seating_arrangement.xlsx`.

## File Structure
- **`utils/`**: Contains Python modules (`table.py`, `openspace.py`, `utils.py`).
- **`colleagues.csv`**: Input file containing colleague names. #and other files for testing
- **`main.py`**: Main script to run the program.

## Python Version
- **Python Version**: 3.10 (or other version you are using)

## Special Instructions
- Add any special instructions, configurations, or setup procedures here...
## Contribution
- **Marc**: Worked on seat/table classes, OpenSpace logic, and main integration.
- **Hajer**: Focused on CSV file reading, storing results, and testing.

## License
This project is licensed under the MIT License.
