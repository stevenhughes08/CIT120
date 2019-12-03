# Flowers.py - This program reads names of flowers and whether they are grown in shade or sun from an input
# file and prints the information to the user's screen.
# Input:  flowers.dat.
# Output: Names of flowers and the words sun or shade.

# Open input file


# def is_even(e):
#     if (e % 2) == 0:
#         return e


# def is_odd(d):
#     if (d % 2) != 0:
#         return d


f = open('.\\flowers.dat')
flowers = f.readlines()
f.close()

#print(flowers[0] + " grows in the " + flowers[1])
# Write while loop her

i = 0
while i < (len(flowers)):
    print(flowers[0 + i] + " grows in the " + flowers[1 + i])
    i = i + 2
# for v in range(0, len(flowers)):
#     if v % 2:
#         var.append(str(flowers[v]))
#     else:
#         var2.append(str(flowers[v]))


# Print flower name using the following format
# print(var + " grows in the " + var2)
