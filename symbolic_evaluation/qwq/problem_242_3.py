import mpmath as mp

# Set precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Calculate π using mpmath's constant
pi_value = mp.pi

# Compute π cubed
pi_cubed = pi_value ** 3

# Multiply by 7
numerator = 7 * pi_cubed

# Divide by 64 to get final result
result = numerator / 64

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))