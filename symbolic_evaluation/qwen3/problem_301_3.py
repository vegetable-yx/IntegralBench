import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate π^2
pi_squared = mp.pi ** 2

# Calculate the first term: π²/12
term1 = pi_squared / 12

# Calculate natural logarithm of 2
ln2 = mp.log(2)

# Calculate (ln2)^2
ln2_squared = ln2 ** 2

# Calculate the second term: (ln2)^2 / 2
term2 = ln2_squared / 2

# Compute final result by subtracting terms
result = term1 - term2

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))