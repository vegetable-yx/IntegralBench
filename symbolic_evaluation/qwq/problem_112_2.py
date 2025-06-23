import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate π using mpmath's constant
pi = mp.pi

# Compute π^(3/2)
pi_power = mp.power(pi, 1.5)

# Calculate square root of 2
sqrt_2 = mp.sqrt(2)

# Compute denominator: 2 * sqrt(2)
denominator = 2 * sqrt_2

# Final result calculation
result = pi_power / denominator

# Print result with 10 decimal places
print(mp.nstr(result, n=10))