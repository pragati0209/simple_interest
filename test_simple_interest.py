def simple_interest(principal, rate, time):
    si = (principal * rate * time) / 100
    return si
p = 500000
r = 2
t = 2
result = simple_interest(p, r, t)
print("Simple Interest", result)

assert result == 20000.0
