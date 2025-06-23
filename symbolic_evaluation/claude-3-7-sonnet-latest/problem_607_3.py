import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define the constant 2 with high precision
x = mp.mpf(2)

# Compute natural logarithm of 2
result = mp.log(x)

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))