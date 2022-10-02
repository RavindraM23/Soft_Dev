import csv

with open("occupations.csv", "r") as f:
  f_read = csv.reader(f)
  for line in f_read:
    print(line)