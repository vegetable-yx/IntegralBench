import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the argument: 253 divided by 3
argument = mp.mpf(253) / mp.mpf(3)

# Compute natural logarithm of the argument
result = mp.log(argument)

# Print result to exactly 10 decimal places
print(mp.nstr(result, n=10))