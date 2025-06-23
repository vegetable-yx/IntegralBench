import mpmath as mp

# Set precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Calculate sqrt(2)
sqrt_2 = mp.sqrt(2)

# Compute (sqrt(2) - 1)
sqrt_minus_1 = sqrt_2 - 1

# Multiply by pi
pi_times_sqrt_diff = mp.pi * sqrt_minus_1

# Divide by 4 to get final result
result = pi_times_sqrt_diff / 4

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))