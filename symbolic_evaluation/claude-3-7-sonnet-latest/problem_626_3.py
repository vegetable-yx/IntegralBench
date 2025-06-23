import mpmath as mp

# Set internal precision to 15 decimal places for accurate computation
mp.dps = 15

# Define the constant 2 as an mpmath floating-point number
x = mp.mpf(2)

# Compute the natural logarithm of 2
result = mp.log(x)

# Print the result formatted to 10 decimal places
print(mp.nstr(result, n=10))