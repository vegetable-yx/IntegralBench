import mpmath as mp
mp.dps = 15  # Set decimal places for internal calculations

# Calculate pi using mpmath's constant
pi_value = mp.pi

# Compute pi cubed
pi_cubed = mp.power(pi_value, 3)

# Divide by 16 to get the final result
result = mp.fdiv(pi_cubed, 16)

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))