import mpmath as mp

# Set internal decimal precision to 15 for accurate calculations
mp.dps = 15

# Calculate the exponent part: 2 raised to the power of 4/3
exponent_result = mp.power(2, 4/mp.mpf('3'))

# Multiply by the coefficient 1/4
result = exponent_result / 4

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))