import mpmath as mp

# Set internal decimal places for high precision
mp.dps = 15

# Get the constant π
pi_value = mp.pi

# Compute π divided by 2
result = pi_value / 2

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))