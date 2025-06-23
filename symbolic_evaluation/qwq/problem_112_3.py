import mpmath as mp

# Set precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Calculate π using mpmath's constant
pi_value = mp.pi

# Compute π cubed
pi_cubed = pi_value ** 3

# Calculate the square root of 2
sqrt_2 = mp.sqrt(2)

# Compute denominator: 8 * √2
denominator = 8 * sqrt_2

# Final result calculation: π³ / (8√2)
result = pi_cubed / denominator

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))