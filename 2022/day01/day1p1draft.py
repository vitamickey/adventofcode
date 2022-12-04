datafile = open("input_day1ex.txt","r")

tempelf = 0
tempcalsum = 0
tempcallist = []
mostelf = 0
mostcalsum = 0

for line in datafile:
    line = line.strip('\n')
    print(line)
    if line.isdigit():
        print("True")
        tempcallist.append(int(line))
        print(tempcallist)
    else:
        print("False")
        tempelf += 1
        print(tempelf)
        tempcalsum = sum(tempcallist)
        print(tempcalsum)
        if tempcalsum > mostcalsum:
            mostelf = tempelf
            print(mostelf)
            mostcalsum = tempcalsum
            print(mostcalsum)
        else:
            None
        tempcallist = []

# iterate through txt file to create list, find sum, and determine if it's the largest
# for each list, if tempcals > mostcals, mostelf = tempelf
# loop through file until all lists found

print(mostelf)
print(mostcalsum)

print("The most Calories being carried by a single elf is", mostcalsum, " Calories.")

datafile.close()