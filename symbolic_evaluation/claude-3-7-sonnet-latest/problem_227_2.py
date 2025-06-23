import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Define common constants and values
pi = mp.pi
ln2 = mp.log(2)  # Natural logarithm of 2
zeta3 = mp.zeta(3)  # Riemann zeta function at 3
zeta4 = mp.zeta(4)  # Riemann zeta function at 4

# Compute each term of the expression separately
# Term 1: (pi^3 / 24) * (ln(2))^2
term1 = (pi**3 / 24) * (ln2**2)

# Term 2: (pi / 4) * (ln(2))^3
term2 = (pi / 4) * (ln2**3)

# Term 3: (3*pi/4) * ln(2) * zeta(3)
term3 = (3 * pi / 4) * ln2 * zeta3

# Term 4: (21*pi/8) * zeta(4)
term4 = (21 * pi / 8) * zeta4

# Combine terms: term1 - term2 + term3 - term4
result = term1 - term2 + term3 - term4

# Print the final result to 10 decimal places
print(mp.nstr(result, n=10))