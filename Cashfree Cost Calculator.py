'''

Designed by Monish
https://techmaniac.in

'''
print("Cashfree Payment Charge Calculator ")
x=float(input("Enter amount "))
y=1.75/100*x
print("Payment Gateway Charge = ",y)
z=18/100*y
print("GST For Payment Gateway Charge = ",z)
print("Total Charges = ",y+z)
print("Amount Received to Bank Account = ",x-(y+z))
print("To receive ",x," Amount must be set to ",x+(y+z))

