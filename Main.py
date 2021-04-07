import random

totalStreaks = 0
n = 0

def coinFlips(number):
    flips = []
    i = 0
    while i < number:
        flip = random.randint(0, 1)
        if flip == 0:
            flips.append('H')
        if flip == 1:
            flips.append('T')
        i += 1
    return flips

def checkRepeats(list, streakLength):
    repeats = 0
    streak = 0
    for i in range(len(list)):
        if i == 0:
            pass
        elif list[i] == list[i-1]:
           streak += 1
        else:
            streak = 0
        if streak == (streakLength - 1):
            streak = 0
            repeats += 1
    return repeats

print("How many coin flips per set?")
flipNumber = int(input())
print("How long should the streak be?")
streakLengths = int(input())
print("How many sets?")
sets = int(input())

while n < sets:
    lists = coinFlips(flipNumber)
    repeat = checkRepeats(lists, streakLengths)
    if repeat > 0:
        totalStreaks += 1
    else:
        pass
    n += 1

print("The number of", flipNumber, "flip sets with a streak of ", streakLengths, " or more is:", totalStreaks)
percentage = totalStreaks/sets
print("The percentage of sets with a streak of", streakLengths, "or more is:", (percentage * 100), "%")