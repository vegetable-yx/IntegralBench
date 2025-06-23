import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate pi (π)
pi_value = mp.pi

# Calculate natural logarithm of 3
ln3 = mp.log(3)

# Multiply pi by ln(3)
product = pi_value * ln3

# Divide by 4 to get the final result
result = product / 4

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))