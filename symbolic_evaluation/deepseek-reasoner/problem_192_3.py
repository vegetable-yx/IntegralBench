import mpmath as mp
mp.dps = 15  # Set decimal precision for intermediate calculations

# Calculate pi cubed
pi_cubed = mp.pi ** 3

# Divide by 32 to get the final result
result = pi_cubed / 32

# Print result with 10 decimal places
print(mp.nstr(result, n=10))