import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate π using mpmath's constant
pi_value = mp.pi

# Compute (π + 2) part
pi_plus_2 = pi_value + 2

# Multiply by 4
numerator = 4 * pi_plus_2

# Divide by π to get final result
result = numerator / pi_value

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))