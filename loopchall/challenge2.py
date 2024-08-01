#!/usr/bin/env python3
"""RZFeeser | PEllis
    Learning about Looping with Dictionaries"""



fruitcompanies= [{"name":"Zesty","employees":["Bryan", "Colin", "Erik", "Emily", "Phillip"]},
                 {"name":"Ripely","employees":["Kishor", "Leia", "Maria", "Jason"]},
                 {"name":"FruitBee","employees":["Rod", "Jarrad", "Paije", "Dom"]},
                 {"name":"JuiceGrove","employees":["Tim", "Travis", "Thomas"]}]

# Write a for loop that returns all the employees

for x in fruitcompanies[2]["employees"]:
    print(x)

# Ask a user to choose a company. Return the employees that belong to that group.

choice= input("Choose a company: Zesty, Ripely, FruitBee, JuiceGrove\n>")

for company in fruitcompanies:
    if choice == company["name"]:
        print(company["employees"])

main ()
