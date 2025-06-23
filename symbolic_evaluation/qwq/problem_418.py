import mpmath as mp

# Set precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Calculate π squared
pi_squared = mp.pi ** 2

# Compute π²/6 term
pi_squared_over_6 = pi_squared / 6

# Subtract 1 from the result
result = pi_squared_over_6 - 1

# Print the final result with 10 decimal places
print(mp.nstr(result, n=10))