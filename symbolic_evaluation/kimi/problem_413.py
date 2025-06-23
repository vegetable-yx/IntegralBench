import mpmath as mp

# Set internal decimal precision to 15 for accurate computation
mp.dps = 15

# Multiply the constant 506 by the mathematical constant pi
result = 506 * mp.pi

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))