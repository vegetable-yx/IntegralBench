import mpmath as mp

# Set the decimal precision to 15 for internal calculations
mp.dps = 15

# Calculate 506 * π using mpmath's constant for pi
result = 506 * mp.pi

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))