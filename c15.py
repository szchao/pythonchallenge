import calendar

for year in range(1006, 1997, 10):
	if (year%4==0 and year%100!=0) or (year%400 ==0): 
		if calendar.weekday(year, 1, 26) == 0:
			print(year)
