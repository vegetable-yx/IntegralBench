import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate π/2 using mpmath's constant
pi_half = mp.pi / 2

# Compute natural logarithm of π/2 using mpmath's log function
result = mp.log(pi_half)

# Print result with 10 decimal places using nstr formatting
print(mp.nstr(result, n=10))