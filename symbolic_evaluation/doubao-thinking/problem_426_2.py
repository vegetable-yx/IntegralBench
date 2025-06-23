import mpmath as mp

# Set internal decimal places to 15 for sufficient precision
mp.dps = 15

# Compute pi/4
pi_over_4 = mp.pi / 4

# Compute natural logarithm of 3
ln_3 = mp.log(3)

# Sum the two terms
result = pi_over_4 + ln_3

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))