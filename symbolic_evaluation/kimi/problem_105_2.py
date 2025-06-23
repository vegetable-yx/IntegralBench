import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate the coefficient 5/8
coefficient = mp.mpf(5)/8

# Multiply by pi constant from mpmath
result = coefficient * mp.pi

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))