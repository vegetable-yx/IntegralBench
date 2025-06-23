import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate the numerical value of 5/8
coefficient = mp.mpf(5)/8

# Multiply by pi constant from mpmath
result = coefficient * mp.pi

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))