def ci(p, r,t):
    Amount = p * (pow((1 + r /100), t))
    CI = Amount - p
    print("Compound interest is Rs.", CI)

p = float(input("Enter the principle amount: "))
r = float(input("Enter the rate of interest: "))
t = float(input("Enter the time period: "))

ci(p, r, t)

