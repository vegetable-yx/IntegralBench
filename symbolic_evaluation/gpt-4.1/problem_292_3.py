import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate pi value
pi_val = mp.pi

# Compute pi cubed
pi_cubed = pi_val ** 3

# Divide by 8 to get final result
result = pi_cubed / 8

# Print result rounded to exactly 10 decimal places
print(mp.nstr(result, n=10))