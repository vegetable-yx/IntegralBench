import mpmath as mp

# Set internal decimal precision to 15 digits for calculations
mp.dps = 15

# Calculate the constant expression: -3 * π
result = -3 * mp.pi

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))