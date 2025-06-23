import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the value of pi
pi_value = mp.pi

# Add 2 to pi
numerator = pi_value + 2

# Divide the numerator by 8
fraction = numerator / 8

# Apply the negative sign
result = -fraction

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))