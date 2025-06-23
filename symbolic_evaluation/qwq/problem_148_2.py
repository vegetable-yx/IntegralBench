import mpmath as mp
mp.dps = 15

# Calculate square root of π
sqrt_pi = mp.sqrt(mp.pi)

# Compute π^(3/2) as π * sqrt(π)
pi_power_3_2 = mp.pi * sqrt_pi

# Calculate numerator (9 * π^(3/2))
numerator = 9 * pi_power_3_2

# Calculate denominator (8 * sqrt(2))
denominator = 8 * mp.sqrt(2)

# Compute final result by dividing numerator by denominator
result = numerator / denominator

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))