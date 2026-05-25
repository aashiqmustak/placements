rate = 5 ;
time = 5 ;
principal = 1000 ;

r = rate / 100 ;

finalAmount = principal * (1 + r) ** time ;
compoundInterest = finalAmount - principal ;

print("Compound Interest = ",compoundInterest)
