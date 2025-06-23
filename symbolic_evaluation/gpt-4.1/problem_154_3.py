import mpmath as mp

# Set internal precision to 15 decimal places for accurate computation
mp.dps = 15

# Compute the natural logarithm of 2
ln2 = mp.log(2)

# Square the logarithm of 2
ln2_squared = ln2 ** 2

# Multiply by pi
pi_times_ln2_sq = mp.pi * ln2_squared

# Divide by 8 to get the final result
result = pi_times_ln2_sq / 8

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))