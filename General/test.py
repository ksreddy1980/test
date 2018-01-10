import pandas as pd




# Clearing the non numeric data in the quantity column
data.quantity = pd.to_numeric(data.quantity, errors = 'coerence')

#converting the column data into int type int

data.quantity =  data.quantity.astype(int)

#converting the time stamp column to Datetime

data.p_date = pd.to_datetime(data.p_date)

#converting the date into day of the week

data.weekdays = pd.Series(data.p_date.dt.weekday)



#converting the dates to Weekdays

weekday_names = ['Monday','Tuesday', 'Wednesday','Thursday', 'Friday','Saturday', 'Sunday']

weekday_dict = { key : weekday_names[key] for key in range(7)}


def day_of_week(day):
    return weekday_dict[day]
data.weekdays = data.weekdays.apply(day_of_week)



