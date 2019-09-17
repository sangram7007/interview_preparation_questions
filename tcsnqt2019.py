# write a program to input the date and showing the days in a month in the year in alphabatical character.
# ex: input = 10/08/2019 output= August has 31 days.


date = input("enter the desired date")
split_date = date.split("/")
month = split_date[1]
all_month = dict(january=31, february=28, march=31, april=30, may=31, june=30, july=31, august=31,
                 september=30, october=31, november=30, december=31)
month_number = dict(january='01', february='02', march='03', april='04', may='05', june='06',
                    july='07', august='08', september='09', october='10', november='11', december='12')

list_type_month_name = [k for k, v in month_number.items() if v == month]  # gives a list type of key
month_name = list_type_month_name[0]                                      # gives the value from the list
print(month_name)

list_type_month_days = [v for k, v in all_month.items() if k == month_name]    # gives a list type of value
month_days = list_type_month_days[0]                                           # gives the value from the list
print(month_days)

print(f'Your desired output is : {month_name} has {month_days} days')


