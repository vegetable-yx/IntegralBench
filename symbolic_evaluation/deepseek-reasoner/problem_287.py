import mpmath as mp

# Set decimal precision for calculations
mp.dps = 15

# Calculate π using mpmath's constant
pi = mp.pi

# Compute π cubed
pi_cubed = mp.power(pi, 3)

# Divide by 32 to get final result
result = pi_cubed / 32

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))