
#values
hours = input('total of hours worked: ')
pay_per_hour = 700
pay_overtime = 350

#hours paid normally
if int(hours) <= 8:
    netpay = ((int(hours) * pay_per_hour))
    print(netpay)
#hours paid overtime included
else:
    netpay = ((int(hours) - 8) * pay_overtime) + (8 * pay_per_hour)
    print("Net pay:", netpay,"$")