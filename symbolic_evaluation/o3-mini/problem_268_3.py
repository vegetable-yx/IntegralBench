import mpmath as mp

# Set internal decimal places for high precision calculation
mp.dps = 15

# Calculate pi^4
pi_fourth = mp.pi**4

# Calculate first term: pi^4 / 64
term1 = pi_fourth / 64

# Compute zeta(3) - Riemann zeta function at 3
zeta3 = mp.zeta(3)

# Calculate second term: (7 * pi * zeta(3)) / 16
term2 = (7 * mp.pi * zeta3) / 16

# Sum the two terms
result = term1 + term2

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))