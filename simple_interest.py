# Simple Interest Calculator

def calculate_simple_interest(principal, rate, time):
    """Calculate Simple Interest"""
    return (principal * rate * time) / 100

if __name__ == "__main__":
    p = float(input("Enter Principal amount: "))
    r = float(input("Enter Rate of interest: "))
    t = float(input("Enter Time (in years): "))

    si = calculate_simple_interest(p, r, t)
    print(f"Simple Interest = {si}")
