# RockClimbing Membership App

## Overview
This script helps manage the membership records for a rock climbing club. It allows for two primary functionalities:
1. **New User Registration**: Adds a new member to the CSV file with their ID, Name, and Start Date.
2. **Old User Data Retrieval or Deletion**: Retrieves or deletes existing user data based on their ID.

## Requirements
- Python 3.x
- `tkinter` for file dialog (installed by default with Python)
- A CSV file named `RockClimbing Membership.csv` that must already have the appropriate headers.

## CSV Format
The CSV file should have the following headers in the first row:
This is required for the script to work properly. The script assumes that the `ID` column is numeric and is incremented automatically with each new member. 
The attached csv file has the correct format

### Example CSV format:
```csv
ID, Name, StartDate
