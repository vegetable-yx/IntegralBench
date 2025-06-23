import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Compute pi squared divided by 8
pi_squared = mp.pi ** 2
term1 = pi_squared / 8

# Compute pi times natural log of 2
pi_times_ln2 = mp.pi * mp.log(2)
term2 = pi_times_ln2 / 4

# Combine the terms: term1 minus term2
result = term1 - term2

# Print the final result with exactly 10 decimal places
print(mp.nstr(result, n=10))