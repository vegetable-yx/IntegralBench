import mpmath as mp

mp.dps = 15  # Set decimal places for internal calculations

# Calculate π²
pi_squared = mp.pi ** 2

# Calculate natural logarithm of 2
ln2 = mp.log(2)

# Multiply π² with ln2
product = pi_squared * ln2

# Divide by 16 to get final result
result = product / 16

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))