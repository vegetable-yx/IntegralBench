import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Get the value of π
pi_val = mp.pi

# Compute π raised to the 4th power
pi_power4 = pi_val ** 4

# Multiply by 7 to get the final result
result = 7 * pi_power4

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))