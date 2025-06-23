import mpmath as mp

# Set precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Calculate 3π using mpmath's pi constant
three_pi = 3 * mp.pi

# Divide by 16 to get the final result
result = three_pi / 16

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))