import mpmath as mp

# Set internal decimal precision to 15 for calculations
mp.dps = 15

# Calculate pi/4: a fundamental constant representing 45 degrees in radians
result = mp.pi / 4

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))