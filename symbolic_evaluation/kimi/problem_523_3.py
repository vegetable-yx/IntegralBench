import mpmath as mp

# Set internal decimal places for high precision
mp.dps = 15

# We are computing the natural logarithm of 2
# Assign the argument 2 to a variable
x = mp.mpf(2)

# Compute natural logarithm using mp.log
result = mp.log(x)

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))