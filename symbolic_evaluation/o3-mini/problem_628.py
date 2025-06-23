import mpmath as mp

# Set internal decimal precision to 15 for calculations
mp.dps = 15

# Calculate the constant pi
pi_val = mp.pi

# Calculate the numerator: pi + 2
numerator = pi_val + 2

# Divide the numerator by 8
fraction = numerator / 8

# Apply the negative sign to get the final result
result = -fraction

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))