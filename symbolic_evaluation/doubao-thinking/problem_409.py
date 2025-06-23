import mpmath as mp

# Set internal decimal precision to 15 for accurate computation
mp.dps = 15

# Calculate the natural logarithm of 2 using mpmath's log function
result = mp.log(2)

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))