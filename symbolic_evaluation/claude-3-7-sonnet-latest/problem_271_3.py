import mpmath as mp

# Set internal decimal places for computation
mp.dps = 15

# Calculate π to the fourth power
pi4 = mp.pi**4

# Calculate π to the third power
pi3 = mp.pi**3

# Compute the numerator: 2π^4 - 3π^3
numerator = 2 * pi4 - 3 * pi3

# Divide the numerator by 192 to get the final result
result = numerator / 192

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))