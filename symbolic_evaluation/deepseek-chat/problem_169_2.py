import mpmath as mp

# Set internal decimal precision to 15 for accurate computation
mp.dps = 15

# Compute π/2: the fundamental constant π divided by 2
pi_val = mp.pi  # Get the value of π
result = pi_val / 2  # Divide π by 2 to get the result

# Print the result formatted to exactly 10 decimal places
print(mp.nstr(result, n=10))