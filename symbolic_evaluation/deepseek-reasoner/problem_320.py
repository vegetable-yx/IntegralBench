import mpmath as mp
# Set decimal precision for calculations
mp.dps = 15

# Compute the value of pi divided by 2
result = mp.pi / 2

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))