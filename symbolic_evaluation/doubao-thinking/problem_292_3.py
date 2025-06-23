import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate π^3
pi_cubed = mp.pi ** 3

# Calculate π^2
pi_squared = mp.pi ** 2

# Calculate Catalan's constant G
G = mp.catalan

# Compute first term: π³/8
term1 = pi_cubed / 8

# Compute second term: (π² * G)/2
term2 = (pi_squared * G) / 2

# Sum both terms for final result
result = term1 + term2

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))