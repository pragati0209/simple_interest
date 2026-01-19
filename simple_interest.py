def simple_interest(principal, rate, time):
    si = (principal * rate * time) / 100
    return si
def main():
    principal = 500000
    rate = 2    
    time = 2     
    print("Principal:", principal)
    print("Rate:", rate)
    print("Time:", time)
    result = simple_interest(principal, rate, time)
    print("Simple Interest:", result)

if __name__ == "__main__":
    main()
