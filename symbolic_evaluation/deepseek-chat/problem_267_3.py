import mpmath as mp

# Set internal decimal places for high precision calculation
mp.dps = 15

# Compute the trilogarithm Li_3 at 1/4
li3_value = mp.polylog(3, mp.mpf(1)/4)

# Multiply by pi/8
result = (mp.pi / 8) * li3_value

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))