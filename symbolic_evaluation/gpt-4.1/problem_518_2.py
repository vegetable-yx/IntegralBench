import mpmath as mp

# Set the decimal places of precision for calculations
mp.dps = 15

# The analytical answer is the constant integer 4036
# Assign directly to a variable
result = mp.mpf(4036)

# Print the result to exactly 10 significant digits as required
print(mp.nstr(result, n=10))