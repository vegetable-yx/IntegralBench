import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate 3 times pi using mpmath constant
three_pi = 3 * mp.pi

# Print the result with exactly 10 decimal places
print(mp.nstr(three_pi, n=10))