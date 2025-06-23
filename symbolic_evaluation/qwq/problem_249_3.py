import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate square root of 5
sqrt5 = mp.sqrt(5)

# Compute the numerator component (sqrt(5) - 2)
sqrt_minus_2 = sqrt5 - 2

# Multiply by pi to get the full numerator
pi_times_component = mp.pi * sqrt_minus_2

# Divide by 2 to get final result
result = pi_times_component / 2

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))