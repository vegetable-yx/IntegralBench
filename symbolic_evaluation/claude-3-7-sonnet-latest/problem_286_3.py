import mpmath as mp

# Set internal decimal places of precision for calculations
mp.dps = 15

# Calculate pi squared divided by 8
pi_squared = mp.pi ** 2
term1 = pi_squared / 8

# Calculate natural logarithm of 2
ln2 = mp.log(2)

# Calculate pi times ln(2) divided by 4
term2 = (mp.pi * ln2) / 4

# Combine terms: result = term1 - term2
result = term1 - term2

# Print the final result to 10 decimal places
print(mp.nstr(result, n=10))