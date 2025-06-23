import mpmath as mp

# Set precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Calculate natural logarithm of 2
ln2 = mp.log(2)

# Multiply by pi
pi_times_ln2 = mp.pi * ln2

# Divide by 8 to get final result
result = pi_times_ln2 / 8

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))