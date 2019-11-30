# MichiganCities.py - This program prints a message for invalid cities in Michigan.
# Input:  Interactive
# Output:  Error message or nothing

# Initialized list of cities
citiesInMichigan = ["Acme", "Albion", "Detroit", "Watervliet",
                    "Coloma", "Saginaw", "Richland", "Glenn", "Midland", "Brooklyn"]

# Get user input
inCity = input("Enter name of city: ")

city = inCity


# Write your test statement here to see if there is a match.
# for city in citiesInMichigan:
#     print("City Found.")
# else:
#     print("Not a city in Michigan")

if city in citiesInMichigan:
    print("City found.")


if city not in citiesInMichigan:
    print("Not a city in Michigan")

                                                            # If the city is found, print "City found."

# Otherwise, "Not a city in Michigan" message should be printed.
