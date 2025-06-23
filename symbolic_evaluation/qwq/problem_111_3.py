import mpmath as mp
mp.dps = 15

# Calculate π squared
pi_squared = mp.pi ** 2

# Compute π² divided by 6
term1 = pi_squared / 6

# Subtract 1 from π²/6
term2 = term1 - 1

# Calculate square root of 2π
sqrt_2pi = mp.sqrt(2 * mp.pi)

# Multiply components for final result
result = sqrt_2pi * term2

print(mp.nstr(result, n=10))