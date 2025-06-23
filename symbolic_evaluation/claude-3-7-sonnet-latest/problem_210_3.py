import mpmath as mp

# Set the internal precision to 15 decimal places
mp.dps = 15

# Calculate pi (π)
pi_val = mp.pi

# Compute pi cubed: π^3
pi_cubed = pi_val ** 3

# Calculate the natural logarithm of 2: ln(2)
ln2 = mp.log(2)

# Multiply π^3 by ln(2)
numerator = pi_cubed * ln2

# Divide by 8 to get the final result
result = numerator / 8

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))