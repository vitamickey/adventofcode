datafile = open("input_day1.txt","r")

tempcallist = []
tempsum = 0
mostsum = 0

for line in datafile:
    line = line.strip('\n')
    if line.isdigit():
        tempcallist.append(int(line))
    else:
        tempsum = sum(tempcallist)
        if tempsum > mostsum:
            mostsum = tempsum
        else:
            None
        tempcallist = []

print("The most Calories being carried by a single elf is", mostsum, "Calories.")

datafile.close()