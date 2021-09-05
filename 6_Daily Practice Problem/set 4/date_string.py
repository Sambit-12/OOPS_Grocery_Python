dates= "45/08/2018"
days=[31,28,31,30,31,30,31,31,30,31,30,31]
dd = 10*int(dates[0]) + int(dates[1])
mm = 10*int(dates[3]) + int(dates[4])
if dd> days[mm]:
    dd=dd- days[mm]
    mm+=1

print(dd,"/",mm,"/ "+dates[6:10])