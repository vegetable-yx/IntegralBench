import mpmath as mp

# Set internal decimal places for precision
mp.dps = 15

# Define the argument in radians
x = mp.mpf(1)

# Calculate sine of the argument
result = mp.sin(x)

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))