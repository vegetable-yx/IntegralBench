import mpmath as mp

# Set the precision to 15 decimal places for internal calculations
mp.dps = 15

# The analytical expression is the constant integer 5040
# Directly assign the value as an mpmath floating-point number
result = mp.mpf(5040)

# Print the result formatted to 10 decimal places
print(mp.nstr(result, n=10))