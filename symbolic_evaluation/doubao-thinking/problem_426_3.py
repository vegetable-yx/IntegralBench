import mpmath as mp

# Set internal precision to 15 decimal places for accurate computation
mp.dps = 15

# Compute π/4
pi_over_4 = mp.pi / 4

# Compute natural logarithm of 3
ln_3 = mp.log(3)

# Sum the two parts: π/4 + ln(3)
result = pi_over_4 + ln_3

# Print the final result to exactly 10 decimal places
print(mp.nstr(result, n=10))