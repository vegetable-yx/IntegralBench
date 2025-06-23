import mpmath as mp

# Set internal decimal precision to 15 for calculations
mp.dps = 15

# Define the constant 2
two = mp.mpf(2)

# Compute the expression: 2 + π
result = two + mp.pi

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))