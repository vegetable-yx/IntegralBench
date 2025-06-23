import mpmath as mp

mp.dps = 15  # Set internal precision

sum_result = mp.mpf(0)
n = 0
tolerance = mp.mpf('1e-15')

while True:
    # Calculate sign term (-1)^n
    sign = (-1) ** n
    
    # Compute denominator components
    factorial_term = mp.factorial(n) ** 2
    four_power = 4 ** n
    denominator = (2 * n + 1) * four_power * factorial_term
    
    # Calculate current term in the series
    term = sign / denominator
    
    # Add term to the cumulative sum
    sum_result += term
    
    # Check if term is below tolerance to break loop
    if mp.fabs(term) < tolerance:
        break
    
    n += 1

# Multiply by sqrt(2) and pi to get final result
result = mp.sqrt(2) * mp.pi * sum_result

# Print result to 10 decimal places
print(mp.nstr(result, n=10))