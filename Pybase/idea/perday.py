year = int(input())
month = int(input())
day = int(input())

daylist = [31,28,31,
           30,31,30,
           31,31,30,
           31,30,31]

tatalDays = 0;

isRun = year % 4 ==0 and year % 400 != 0 or year % 400 == 0

for i in range(month-1):
    tatalDays += daylist[i]

tatalDays += day

if isRun:
    tatalDays += 1

print(tatalDays)