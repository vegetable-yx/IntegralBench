import mpmath as mp
mp.dps = 15

# Calculate π/4
pi_over_4 = mp.pi / 4

# Calculate natural logarithm of 3
ln_3 = mp.log(3)

# Sum the two terms
result = pi_over_4 + ln_3

print(mp.nstr(result, n=10))