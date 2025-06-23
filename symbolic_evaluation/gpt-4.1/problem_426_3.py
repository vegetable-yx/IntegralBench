import mpmath as mp

# Set internal decimal precision to 15 for calculations
mp.dps = 15

# Calculate π/4
pi_over_four = mp.pi / 4

# Calculate natural logarithm of 3
ln_three = mp.log(3)

# Sum the two components
result = pi_over_four + ln_three

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))