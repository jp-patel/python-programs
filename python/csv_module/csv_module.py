import csv


# how to read a csv file

with open('read.csv', 'r') as file:
    reader = csv.reader(file)
    print("Reading from read.csv...")
    for row in reader:
        print(row)
print()


# how to write a csv file
import csv
with open('write.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["SN", "Movie", "Protagonist"])
    writer.writerow([1, "Lord of the Rings", "Frodo Baggins"])
    writer.writerow([2, "Harry Potter", "Harry Potter"])
print("Content has been written to write.csv")
print()
