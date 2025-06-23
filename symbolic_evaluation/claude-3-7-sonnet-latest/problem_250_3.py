import mpmath as mp

# Set internal decimal precision to 15 for accurate computations
mp.dps = 15

# Calculate the value of pi/2
result = mp.pi / 2

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))