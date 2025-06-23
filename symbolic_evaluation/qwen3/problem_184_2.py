import mpmath as mp

mp.dps = 15  # Set internal precision

# Calculate natural logarithm of 3
ln3 = mp.log(3)

# Multiply by the logarithm result
pi_ln3 = mp.pi * ln3

# Divide by 8 to get final result
result = pi_ln3 / 8

# Print result with 10 decimal places
print(mp.nstr(result, n=10))