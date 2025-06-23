import mpmath as mp

# Set precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Calculate square root of 5
sqrt5 = mp.sqrt(5)

# Compute (sqrt(5) - 2)
numerator_part = sqrt5 - 2

# Multiply by pi
pi_times_part = mp.pi * numerator_part

# Divide by 2 to get final result
result = pi_times_part / 2

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))