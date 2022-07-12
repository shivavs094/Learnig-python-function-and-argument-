tupl= ('s','h','i','v','a')
tup=(22,55,66,44,99)
DT= dict.fromkeys(tupl)
DT['s']=45
DT['h']=12.5
DT['i']=24
DT['v']=33
DT['a']=55
DT.update({'CS':22})
DT.update({'v':22})
DT.pop('s')
DT.clear()
print(DT)