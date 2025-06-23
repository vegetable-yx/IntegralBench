import mpmath as mp

# Set internal decimal precision to 15 for calculations
mp.dps = 15

# Assign the mathematical constant e (base of natural logarithm)
result = mp.e

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))