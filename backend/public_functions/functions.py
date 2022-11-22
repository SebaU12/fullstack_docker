import calendar

def generate_limits(year, month):
    limit_day = calendar.monthrange(year, month)
    limit_1 = str(year)+ "-" + str(month) + "-01" 
    limit_2 = str(year)+ "-" + str(month) + "-" + str(limit_day[1]) 
    return limit_1, limit_2 

def sum_values_json(data, label, form=True): 
    if(form == True):
        x = data.get_json()
        valor = 0
        for i in range (len(x)): 
            valor += float(x[i][label])
        return valor
    else : 
        valor = 0
        for i in range (len(data)): 
            valor += float(data[i][label])
        return valor


