import mpmath as mp
mp.dps = 15  # Set internal decimal precision

# Calculate 3π using mpmath's high-precision pi constant
three_pi = 3 * mp.pi

# Divide the result by 8 to get the final value
result = three_pi / 8

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))