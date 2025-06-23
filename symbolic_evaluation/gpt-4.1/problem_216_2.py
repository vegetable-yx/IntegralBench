import mpmath as mp

# Set internal decimal places for high precision calculation
mp.dps = 15

# Calculate 2 times pi
two_pi = 2 * mp.pi

# Compute square root of (2 * pi)
result = mp.sqrt(two_pi)

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))