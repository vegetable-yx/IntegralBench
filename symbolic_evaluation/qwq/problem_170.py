import mpmath as mp

# Set precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Calculate natural logarithm of 2
ln2 = mp.log(2)

# Square the logarithm value
ln2_squared = ln2 ** 2

# Multiply by pi
pi_times_ln2_sq = mp.pi * ln2_squared

# Divide by 8 to get final result
result = pi_times_ln2_sq / 8

# Print result with 10 decimal places
print(mp.nstr(result, n=10))