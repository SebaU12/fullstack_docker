import calendar

def generate_limits(year, month):
    limit_day = calendar.monthrange(year, month)
    limit_1 = str(year)+ "-" + str(month) + "-01" 
    limit_2 = str(year)+ "-" + str(month) + "-" + str(limit_day[1]) 
    return limit_1, limit_2 

print(generate_limits(2022, 11))
