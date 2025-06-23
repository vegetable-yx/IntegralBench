import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate π using mpmath's built-in constant
pi_value = mp.pi

# Compute π^3
pi_cubed = pi_value ** 3

# Calculate first term: π³/48
term1 = pi_cubed / 48

# Calculate second term: π/8
term2 = pi_value / 8

# Combine terms for final result
result = term1 - term2

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))