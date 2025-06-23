import mpmath as mp

# Set internal decimal precision to 15 for intermediate calculations
mp.dps = 15

# Compute pi^3
pi_cubed = mp.pi ** 3

# Calculate the first term: (5 * pi^3) / 24
term1 = (5 * pi_cubed) / 24

# Compute zeta(3)
zeta3 = mp.zeta(3)

# Calculate the second term: 2 * zeta(3)
term2 = 2 * zeta3

# Combine the terms: term1 - term2
result = term1 - term2

# Print the final result to 10 decimal places
print(mp.nstr(result, n=10))