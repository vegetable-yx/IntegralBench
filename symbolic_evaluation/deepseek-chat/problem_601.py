import mpmath as mp

# Set internal decimal precision to 15 digits for calculations
mp.dps = 15

# Calculate the natural logarithm of 2
ln2 = mp.log(2)

# Multiply pi by ln(2)
result = mp.pi * ln2

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))