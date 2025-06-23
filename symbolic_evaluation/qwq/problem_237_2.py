import mpmath as mp

mp.dps = 15  # Set decimal precision for calculations

# Calculate 3π/2 using mpmath's pi constant
pi_term = mp.pi
result = (3 * pi_term) / 2

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))