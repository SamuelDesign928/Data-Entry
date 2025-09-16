# Data Entry

"""
Create a program that retrieves the membership details for a Rock Climbing Club. The program should take a range of details
and then repeat them back, with headings, for confirmation.
Once confirmed, the program stores these details; else it clears them and allows a new input.
Extensions:
1. Allow entry of more than one membership
2. Store membership details to a file
3. Retrieve details from a file
4. Allow searching for stored users
"""

"""
a, ask if returning user or new
    if new:
        i) ask input for headings
        ii) confirm input for headings
        -> if no: return to main menu
        iii) store details in csv file under new ID
b, if returning:
    i) retreave data?
    -> ask ID and show
    -> option to download
    ii) delete data?
    -> all coloumns in ID row is wiped

headings: ID, Name, start date
"""

import csv
from datetime import datetime
from tkinter import filedialog

def new_user():
    fnames = ["ID","Name","StartDate"]
    dt = datetime.now()
    year = dt.strftime("%Y"); month = dt.strftime("%m")
    ID = 0
    
    with open("RockClimbing Membership.csv", 'r') as csvfile:
        ID_reader = csv.DictReader(csvfile)
        rows = list(ID_reader)
        last_row = rows[-1]
        ID = int(last_row["ID"]) + 1

    NAME = input("> Enter Your Name: ").strip().upper()
    if NAME == "Q": quit()
    SDATE = f"{month} - {year}"
    membership = {
        "ID":ID,
         "Name":NAME,
         "StartDate":SDATE
         }
    

    while True:
        print(f"> Is | {membership["Name"]}, {membership["StartDate"]} | Correct?")
        correct = input("> (Y/N): ").strip().upper()
        if correct == "Q": quit()
        if correct == "N" or correct == "NO":
            return "> Cancelling Action"
        elif correct != "Y" and correct != "YES": print("> Invalid Input")
        break

    with open("RockClimbing Membership.csv", mode='a', newline='') as csvfile:
        membership_writer = csv.DictWriter(csvfile, fieldnames=fnames, delimiter=',')
        membership_writer.writerow(membership)
    
    print(f"> Memebership Added | Your ID is {ID}")


def old_user():

    while True:
        ans = input("> Do you wish to retrieve data [R] | or delete data [D] | Quit [Q]: ").strip().upper()
        if ans == "Q": quit()
        if ans not in ["R", "D"]: print("> Invalid Input")
        else: break

    ans_ID = input("> Enter your ID: ").strip()
    if ans_ID == "Q": quit()

    with open("RockClimbing Membership.csv", 'r', newline='') as csvfile:
        ID_reader = csv.DictReader(csvfile)
        rows = list(ID_reader)
        fieldnames = ID_reader.fieldnames

    for row in rows:
        if row[fieldnames[0]] == ans_ID:
            if ans == "D":
                for key in fieldnames[1:]:
                    row[key] = "DEL"
                print(f"> Data for ID {ans_ID} deleted")
                break

            print("> Retrieved Data:")
            print(row)
            file_path = filedialog.asksaveasfilename(
                defaultextension="RockClimbing Membership.csv",
                filetypes=[("CSV files", "*.csv")],
                title="Save CSV File"
            )
            if file_path:
                with open(file_path, 'w', newline='') as savefile:
                    writer = csv.DictWriter(savefile, fieldnames=fieldnames)
                    writer.writeheader()
                    writer.writerow(row)
                print(f"> Data saved to {file_path}")
            break
    else:
        print("> ID not found.")
        return

    if ans == "D":
        with open("RockClimbing Membership.csv", 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)


def main():
    response = ""
    print("<press q to quit>")
    while True:
        response = input("> Are you a new member? Y/N: ").strip().upper()    
        match response:
            case "Q":
                quit()
            case "Y" | "YES":
                new_user()
            case "N" | "NO":
                old_user()
            case _:
                print("> Invalid Answer. Try Y or N")



main()