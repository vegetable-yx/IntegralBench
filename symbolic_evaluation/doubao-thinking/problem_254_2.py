import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate -3π directly using mpmath's constant
result = -3 * mp.pi

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))