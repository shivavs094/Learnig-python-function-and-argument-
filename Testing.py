MRP=1125.556
discount=0
bought_sales=True

if MRP>=1000 and bought_sales:
    discount=22.35


total=MRP-MRP*discount/100

print('the amount of diccount:',.__round__(2)(MRP*discount/100))
print ('the amount of bought:',int(total))
