import mpmath as mp

# Set precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Calculate components of the expression
sqrt_part = mp.sqrt(2)          # Compute √2
log_argument = 2 + sqrt_part    # Compute (2 + √2)
log_value = mp.log(log_argument) # Calculate ln(2 + √2)
pi_half = mp.pi / 2             # Precompute π/2

# Combine components for final result
result = pi_half * log_value

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))