#Bond Calculator - calculates Macaulay, Modified, Convexity, Price
#Zubin Meyer

#declare and assign all of the required inputs from the user
#firstd is for firstderiv weighted cashflows
#secondd is for secondderiv weighted cashflows
#bondcashflow is normal cashflow to calculate price
firstd=0
secondd=0
bondcashflow=0
P=float(input("Please enter principal value: "))
n=int(input("Please enter number of years to maturity: "))
C=float(input("Please enter the coupon (as a %): "))
y=float(input("Please enter the yield (as a %): "))
compound=input("Please enter A/a for annual, S/s for semiannual, Q/q for quarterly: ")


#adjust the coupon and yield to be in dollar and decimal values respectively
C=C*P/100
y/=100


#depending on frequency of bond annual/semiannual/quarterly do the proper adjustments
if compound=="S" or compound =="s":
    n*=2; C/=2; y/=2;
elif compound=="Q" or compound=="q":
    n*=4; C/=4; y/=4;


#calculate the cashflows from the bond and weighted cashflows
for i in range (1,n+1):
    bondcashflow+=(C/((1+y)**i))
    firstd+=((i*C)/((1+y)**i))
    secondd+=(((i+1)*i*C)/((1+y)**(i+2)))
  
  
#calculate the principal repayment
flumpsum=(n*P)/((1+y)**n)
slumpsum=(n+1)*n*P/((1+y)**(n+2))


#get numerator and denominator (price) in order
firstd+=flumpsum
secondd+=slumpsum
price=bondcashflow+(flumpsum/n)


#calculate macaulay and convexity
macdur=firstd/price
convexity=secondd/price


#adjust macdur and convexity based on frequency of interest payment
if compound=="S" or compound=="s":
    macdur/=2; convexity/=4;
elif compound=="Q" or compound=="q":
    macdur/=4; convexity/=16;


#calculate modified duration with proper macaulay
moddur=macdur/(1+y)


#show all measures
print("\nPrice of Bond: $", price)
print("Macaulay Duration in Years: ", macdur)
print("Modified Duration in Years: ", moddur)
print("Convexity in Years: ", convexity)
print("Dollar Convexity Measure: ", convexity*price)



