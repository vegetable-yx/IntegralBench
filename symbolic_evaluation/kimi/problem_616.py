import mpmath as mp

# Set decimal places for internal precision
mp.dps = 15

# Calculate pi
pi_val = mp.pi

# Calculate natural logarithm of 2
ln2_val = mp.log(2)

# Multiply pi and ln(2)
product = pi_val * ln2_val

# Divide by 2 to get the final result
result = product / 2

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))