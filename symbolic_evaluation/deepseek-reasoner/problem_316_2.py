import mpmath as mp
# Set precision to 15 decimal places
mp.dps = 15

# Calculate natural logarithm of 2
ln2 = mp.log(2)

# Get the value of pi
pi_value = mp.pi

# Multiply pi by ln(2) to get the final result
result = pi_value * ln2

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))