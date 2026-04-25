# Storing birthdays in 5 different variables

birthday1 = "Ali - 12/03/2010"
birthday2 = "Sara - 25/07/2011"
birthday3 = "Ahmed - 10/01/2009"
birthday4 = "Ayesha - 05/09/2012"
birthday5 = "Hassan - 18/11/2010"

# Asking user for input
name = input("Enter a name to search: ")

# Checking manually
if name == "Ali":
    print(birthday1)
elif name == "Sara":
    print(birthday2)
elif name == "Ahmed":
    print(birthday3)
elif name == "Ayesha":
    print(birthday4)
elif name == "Hassan":
    print(birthday5)
else:
    print("Birthday not found.")