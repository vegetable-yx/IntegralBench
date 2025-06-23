import mpmath as mp

# Set internal decimal places for high precision calculation
mp.dps = 15

# Compute π/4
pi_over_4 = mp.pi / 4

# Compute natural logarithm of 3
ln_3 = mp.log(3)

# Sum the two components
result = pi_over_4 + ln_3

# Print final result to exactly 10 decimal places
print(mp.nstr(result, n=10))