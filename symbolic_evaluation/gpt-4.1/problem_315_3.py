import mpmath as mp

# Set decimal places for internal calculations
mp.dps = 15

# Calculate zeta(3)
zeta3 = mp.zeta(3)

# Calculate pi^2
pi_sq = mp.pi**2

# Calculate pi^4
pi_fourth = mp.pi**4

# Calculate natural logarithm of 2
ln2 = mp.log(2)

# Compute term1: (7/2) * zeta(3)
term1 = (7/2) * zeta3

# Compute term2: (pi^2 / 6) * ln(2) [will subtract later]
term2 = (pi_sq / 6) * ln2

# Compute term3: pi^4 / 90
term3 = pi_fourth / 90

# Combine terms: term1 - term2 + term3
result = term1 - term2 + term3

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))