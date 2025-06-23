import mpmath as mp

# Set internal precision to 15 decimal places for accurate computation
mp.dps = 15

# Calculate natural logarithm of 2
ln2 = mp.log(2)

# Multiply pi by ln(2)
pi_times_ln2 = mp.pi * ln2

# Divide by 2 to get the final result
result = pi_times_ln2 / 2

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))