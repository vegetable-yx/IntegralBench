import mpmath as mp
mp.dps = 15  # Set internal decimal precision to 15 digits

# Calculate 4π using direct multiplication
multiplier = mp.mpf(4)
pi_constant = mp.pi
result = multiplier * pi_constant

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))