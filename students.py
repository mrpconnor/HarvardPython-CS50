import csv

name = input("Whats my name?")
home = input("Whats your home?")

with open("students.csv", "a") as file:
    writer = csv.writer(file)
    writer.writerow([name, home])