import mpmath as mp

# Set internal decimal places for high precision
mp.dps = 15

# Define the argument for sine function (1 radian)
x = mp.mpf(1)

# Compute sine of 1 radian
result = mp.sin(x)

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))