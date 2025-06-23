import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate π/4 term
pi_term = mp.pi / 4

# Calculate natural logarithm of 2
ln2 = mp.log(2)

# Calculate (ln 2)/2 term
ln2_term = ln2 / 2

# Combine all components
result = pi_term - 1 + ln2_term

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))