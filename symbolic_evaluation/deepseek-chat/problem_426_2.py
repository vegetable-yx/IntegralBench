import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate π/4
pi_over_4 = mp.pi / 4

# Calculate natural logarithm of 3
ln_3 = mp.log(3)

# Sum the two components
result = pi_over_4 + ln_3

# Print result to exactly 10 decimal places
print(mp.nstr(result, n=10))