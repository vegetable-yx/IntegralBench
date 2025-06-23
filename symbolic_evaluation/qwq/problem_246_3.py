import mpmath as mp
mp.dps = 15

# Calculate numerator components
factorial_7 = mp.factorial(7)  # Compute 7! = 5040
pi_power = mp.pi ** 4          # Compute π^4

# Calculate denominator components
two_power_8 = mp.mpf(2)**8     # Compute 2^8 = 256
eight_power_4 = mp.mpf(8)**4   # Compute 8^4 = 4096

# Combine components
numerator = factorial_7 * pi_power
denominator = two_power_8 * eight_power_4

# Final calculation
result = numerator / denominator

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))