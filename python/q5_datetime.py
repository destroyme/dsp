# Hint:  use Google to find python function
import datetime

####a) 
date_start = '01-02-2013'  
date_stop = '07-28-2015'   

start = datetime.datetime.strptime(date_start, '%m-%d-%Y')
stop  = datetime.datetime.strptime(date_stop , '%m-%d-%Y')
a_total = stop - start
a_days = a_total.days
print(a_days)

####b)  
date_start = '12312013'  
date_stop = '05282015'  

start = datetime.datetime.strptime(date_start, '%m%d%Y')
stop  = datetime.datetime.strptime(date_stop , '%m%d%Y')
a_total = stop - start
a_days = a_total.days
print(a_days)

####c)  
date_start = '15-Jan-1994'  
date_stop = '14-Jul-2015'  

start = datetime.datetime.strptime(date_start, '%d-%b-%Y')
stop  = datetime.datetime.strptime(date_stop , '%d-%b-%Y')
a_total = stop - start
a_days = a_total.days
print(a_days)

