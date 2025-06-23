import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate pi constant
pi_val = mp.pi

# Calculate natural logarithm of 2
ln2_val = mp.log(2)

# Multiply pi and ln(2)
product = pi_val * ln2_val

# Divide by 8
quotient = product / 8

# Apply the negative sign
result = -quotient

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))