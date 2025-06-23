import mpmath as mp
# Set decimal precision for calculations
mp.dps = 15

# Calculate π using mpmath's constant
pi_value = mp.pi

# Compute π/4 using exact analytical expression
result = pi_value / 4

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))