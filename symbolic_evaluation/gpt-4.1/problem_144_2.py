import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

def compute_integral1():
    sum_part = mp.mpf(0)
    k = 0
    while True:
        # Term for I1 series: 1/(k! * (k+1)!)
        term = 1 / (mp.factorial(k) * mp.factorial(k + 1))
        # Integral of sin^(2k+3)θ from 0 to π/2
        integral = (mp.sqrt(mp.pi)/2) * mp.gamma(k + 2) / mp.gamma(k + 2.5)
        term *= integral
        sum_part += term
        # Check if term is negligible
        if mp.mag(term) < -50:
            break
        k += 1
    return 0.5 * sum_part  # Multiply by 1/2 from the original expression

def compute_integral2():
    sum_part = mp.mpf(0)
    k = 0
    while True:
        # Term for I2 series: 1/(k! * (k+2)!)
        term = 1 / (mp.factorial(k) * mp.factorial(k + 2))
        # Integral of sin^(2k+3)θ from 0 to π/2
        integral = (mp.sqrt(mp.pi)/2) * mp.gamma(k + 2) / mp.gamma(k + 2.5)
        term *= integral
        sum_part += term
        if mp.mag(term) < -50:
            break
        k += 1
    return -0.5 * sum_part  # Multiply by -1/2 from the original expression

def compute_integral3():
    sum_part = mp.mpf(0)
    k = 0
    while True:
        # Term for I3 series: 1/(k! * (k+3)!)
        term = 1 / (mp.factorial(k) * mp.factorial(k + 3))
        # Integral of sin^(2k+3)θ from 0 to π/2
        integral = (mp.sqrt(mp.pi)/2) * mp.gamma(k + 2) / mp.gamma(k + 2.5)
        term *= integral
        sum_part += term
        if mp.mag(term) < -50:
            break
        k += 1
    return 0.25 * sum_part  # Multiply by 1/4 from the original expression

# Compute each integral part
result = compute_integral1() + compute_integral2() + compute_integral3()

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))