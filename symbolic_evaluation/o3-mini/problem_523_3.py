import mpmath as mp

# Set internal precision to 15 decimal places for accurate computation
mp.dps = 15

# Define the constant value for which we compute the natural logarithm
x = mp.mpf(2)

# Compute the natural logarithm of 2 using mpmath's log function
result = mp.log(x)

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))