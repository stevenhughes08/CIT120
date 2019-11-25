MAX_AVERAGES = 8
averages = []

for i in range(MAX_AVERAGES):
    averageString = input("Enter a Batting Average: ")
    battingAverage = float(averageString)
    averages.append(battingAverage)
    print(averages)

minAverage = averages[0]
maxAverage = averages[0]
total = averages[0]
neg_val = averages.pop(0)
print(averages)

for index, average in enumerate(averages, start=1):
    minAverage = min(averages)
    maxAverage = max(averages)
    averages.append(neg_val)
    print(averages)
    total = sum(averages)
    # print(total)
    average = total / MAX_AVERAGES
    print("Minimum batting average is ", minAverage)
    print("Maximum batting average is ", maxAverage)
    print("Average batting average is ", average)
    break

# inputs .299, .157, .242, .203, .198, .333, .270, .190.
# The minimum batting average should be .157
# the maximum batting average should be .333.
# The average should be .2365.
