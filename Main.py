import random

totalStreaks = 0
n = 0
dieSides = 0
flipNumber = 0
streakLengths = 0
sets = 0

def coinFlips(sides, number):
    flips = []
    i = 0
    while i < number:
        flip = random.randint(0, (sides - 1))
        flips.append(flip)
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
while True:
    print("How many sides should the die have?")
    while True:
        try:
            dieSides = int(input())
            break
        except ValueError:
            print('please enter an integer.')
    if dieSides == 2:
        while True:
            try:
                print("How many coin flips per set?")
                flipNumber = int(input())
                break
            except ValueError:
                print('please enter an integer.')
    elif dieSides == 1:
        while True:
            try:
                print("How many times do you want to repeat 1?")
                flipNumber = int(input())
                break
            except ValueError:
                print('please enter an integer.')
    else:
        while True:
            try:
                print("How many die rolls per set?")
                flipNumber = int(input())
                break
            except ValueError:
                print('please enter an integer.')
    while True:
        try:
            print("How long should the streak be?")
            streakLengths = int(input())
            break
        except ValueError:
            print('please enter an integer.')

    while True:
        try:
            print("How many sets?")
            sets = int(input())
            break
        except ValueError:
            print('please enter an integer.')
    break

while n < sets:
    lists = coinFlips(dieSides, flipNumber)
    repeat = checkRepeats(lists, streakLengths)
    if repeat > 0:
        totalStreaks += 1
    else:
        pass
    n += 1

print("The number of", flipNumber, "roll sets with a streak of ", streakLengths, " or more is:", totalStreaks)
percentage = totalStreaks/sets
print("The percentage of sets with a streak of", streakLengths, "or more is:", (percentage * 100), "%")