import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute π/4
pi_over_four = mp.pi / 4

# Compute natural logarithm of 3
ln_three = mp.log(3)

# Sum the two terms
result = pi_over_four + ln_three

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))