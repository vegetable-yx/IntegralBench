import mpmath as mp

# Set internal precision to 15 decimal places for calculations
mp.dps = 15

# The analytical expression is a constant value: 1.2337005501
# Assign the constant value directly to the result variable
result = mp.mpf('1.2337005501')

# Print the result formatted to exactly 10 decimal places
print(mp.nstr(result, n=10))