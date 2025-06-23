import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate hyperbolic cosine of 6
cosh_6 = mp.cosh(6)

# Compute numerator: cosh(6) - 1
numerator = cosh_6 - 1

# Divide by 3 to get final result
result = numerator / 3

# Print result with 10 decimal places
print(mp.nstr(result, n=10))