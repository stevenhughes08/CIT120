# As a user I should be shown the number of tickets left remaining, so I can understand the importance of buying now.

# Output how many tickets are remaining user the tickets_remaining variable

TICKET_PRICE = 10
tickets_remaining = 100

# Run this code until tickets are sold out.
while tickets_remaining >= 1:
        print("There are {} tickets remaining.".format(tickets_remaining))

        # Gather the user's name and assign it to a new variable
        name = input("What is your name? ")

        # Prompt the user by name and ask how many tickets they would like.
        desired_tickets = input(
            "Hello {} how many tickets would you like to buy? ".format(name))
        desired_tickets = int(desired_tickets)
    except ValueError:
        print("Oh no {} we ran into an error. Please try again.")
        # Handles errors for invalid user entry or more tickets than avaialable

    else:
        # Calcualte the price (number of tickets multiplied by the price) and assign it to a variable.
        total_due = desired_tickets * TICKET_PRICE
        # Output the price to the screen.
        print("That will cost ${}".format(total_due))

        # Prompt user if they want to proceed. Y/N

        should_proceed = input("Do you want to proceed? Y/N ")

        # If they want to proceed
        if should_proceed.lower() == "y":
            # Gather Credit card info and process it.
            print("SOLD! ")
            tickets_remaining -= desired_tickets
        # print out to the screen "SOLD!" to confirm purchase.
        else:
            print("{} you twit! I can't believe you came all this way not to buy tickets!".format(name))

        # and the decrement the tickets remaining by the number of tickets purchased
        # Otherwise...

        # Thank them by name

        # Print Sold out when there are no tickets remaining.
else:
    print("Sorry all sold out!")
