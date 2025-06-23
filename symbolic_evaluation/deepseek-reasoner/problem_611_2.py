import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate square root of 3
sqrt3 = mp.sqrt(3)

# Compute first logarithmic term: ln(2 + sqrt(3))
term1 = mp.log(2 + sqrt3)

# Compute second logarithmic term: ln(sqrt(3))
term2 = mp.log(sqrt3)

# Calculate final result by subtracting terms
result = term1 - term2

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))