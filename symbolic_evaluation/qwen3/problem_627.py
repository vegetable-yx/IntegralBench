import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate π/4
pi_over_4 = mp.pi / 4

# Calculate natural logarithm of 2
ln2 = mp.log(2)

# Calculate (ln 2)/2
ln2_over_2 = ln2 / 2

# Combine the terms: π/4 + (ln 2)/2 - 1
result = pi_over_4 + ln2_over_2 - 1

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))