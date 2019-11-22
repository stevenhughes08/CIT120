head1 = "Number: "
head2 = "Multiplied by 2: "
head3 = "Multiplied by 10:  "
NUM_LOOPS = 10  # Constant used to control loop.

print("0 through 10 multiplied by 2 and by 10" + "\n")

numberCounter = 0
# while numberCounter < NUM_LOOPS:
#     for i in range(0, 10):
#         numberCounter = str(i + 1)
#         print(head1 + numberCounter)
#     for i in range(0, 10):
#         numberCounter = str(i + 1)
#         numberCounter = numberCounter * 2
#         print(head2 + str(numberCounter))
#     for i in range(0, 10):
#         numberCounter = str(i + 1)
#         numberCounter = numberCounter * 10
#         print(head3 + numberCounter)
# while numberCounter < numberCounter:
#     print(head1 + numberCounter)
#     print(head2 + numberCounter * 2)
#     print(head3 + numberCounter * 10)
#     numberCounter = str(numberCounter + 1)


while numberCounter <= NUM_LOOPS:
    for i in range(0, 10):
        print(head1 + str(numberCounter))
        print(head2 + str(numberCounter * 2))
        print(head3 + str(numberCounter * 10))
        numberCounter = i + 1
