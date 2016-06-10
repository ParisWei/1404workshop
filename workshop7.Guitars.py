from Guitars import Guitars
guitars = []
print("My guitars!")

name = input("Name:")
while name !="":
    year = int(input("Year:"))
    cost = float(input("Cost: $"))
    print("{} ({}) : ${:,.2f} added".format(name, year, cost))
    guitars.append(Guitars(name, year, cost))
    name = input("Name:")
guitars.append(Guitars("Gibson L-5 CES", 1922, 16035.40))
guitars.append(Guitars("Line 6 JTV-59", 2010, 1512.9))
print("These are my guitars:")

for i, guitar in enumerate(guitars):
    if guitar.is_vintage():
        vintage_string = "(Vintage)"
    else:
        vintage_string = ""
    print("Guitar {}: {:>20} ({}), worth ${:10,.2f} {}".format(i + 1, guitar.name, guitar.year, guitar.cost, vintage_string))
