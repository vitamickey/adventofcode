datafile = open("input_day1.txt","r")

tempcallist = []
tempsum = 0
sumlist = []

for line in datafile:
    line = line.strip('\n')
    if line.isdigit():
        tempcallist.append(int(line))
    else:
        tempsum = sum(tempcallist)
        sumlist.append(tempsum)
        tempcallist = []

orderedlist = sorted(sumlist,reverse=True)[:3]
print(orderedlist)
sumtopthree = sum(orderedlist)

print("The amount of Calories being carried by the top three elves is", sumtopthree, "Calories.")

datafile.close()