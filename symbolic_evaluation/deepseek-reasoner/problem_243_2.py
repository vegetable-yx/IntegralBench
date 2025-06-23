import mpmath as mp

mp.dps = 15  # Set internal precision

# Calculate π^4
pi_power4 = mp.pi**4

# Calculate square root of 3
sqrt3 = mp.sqrt(3)

# Compute denominator: 216 * sqrt(3)
denominator = 216 * sqrt3

# Compute numerator: 7 * π^4
numerator = 7 * pi_power4

# Final calculation: (7π^4) / (216√3)
result = numerator / denominator

# Print result with 10 decimal places
print(mp.nstr(result, n=10))