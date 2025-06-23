import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate π^2/6
pi_squared_over_6 = mp.pi**2 / 6

# Calculate (ln 2)^2
ln2 = mp.log(2)
ln2_squared = ln2**2

# Compute final result by subtraction
result = pi_squared_over_6 - ln2_squared

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))