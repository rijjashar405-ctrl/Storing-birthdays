# Create a dictionary with some birthdays
birthdays = {
    "Ali": "12/03/2010",
    "Sara": "25/07/2011"
}

# Ask user for a name
name = input("Enter a name: ")

# Check and print birthday
if name in birthdays:
    print(name + "'s birthday is " + birthdays[name])
else:
    print("Sorry, birthday not found.")