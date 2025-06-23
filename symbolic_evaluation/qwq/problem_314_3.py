import mpmath as mp

mp.dps = 15  # Set internal precision

sum_result = mp.mpf(0)
n = 0
epsilon = mp.mpf(1e-15)  # Convergence threshold

while True:
    # Calculate denominator components
    four_power = mp.power(4, n)
    denominator_term = mp.power(2*n + 1, 3)
    
    # Compute current series term
    term = mp.mpf(1) / (four_power * denominator_term)
    
    # Add term to cumulative sum
    sum_result += term
    
    # Check for convergence
    if mp.fabs(term) < epsilon:
        break
    
    n += 1

# Apply final negation from the formula
result = -sum_result

# Print with 10 decimal precision
print(mp.nstr(result, n=10))