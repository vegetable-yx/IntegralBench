import mpmath as mp
mp.dps = 15

sum_result = mp.mpf(0)
n = 0
while True:
    # Calculate components for the current term
    exponent = mp.mpf(n)
    base_power = mp.power(4, exponent)  # 4^n
    denominator_term = 2*exponent + 1      # (2n+1)
    cubed_denominator = mp.power(denominator_term, 3)  # (2n+1)^3
    
    # Compute current term and add to sum
    term = 1 / (base_power * cubed_denominator)
    sum_result += term
    
    # Break loop when term becomes smaller than 1e-20
    if mp.fabs(term) < 1e-20:
        break
    n += 1

# Apply the series negation and print result
result = -sum_result
print(mp.nstr(result, n=10))