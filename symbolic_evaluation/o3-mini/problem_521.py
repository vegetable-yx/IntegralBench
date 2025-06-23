import mpmath as mp

# Set internal decimal places for high precision calculation
mp.dps = 15

# Define the constant value 3
x = mp.mpf(3)

# Compute the natural logarithm of 3
result = mp.log(x)

# Print the result formatted to 10 decimal places
print(mp.nstr(result, n=10))