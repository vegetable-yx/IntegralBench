import mpmath as mp

# Set internal decimal places for precision
mp.dps = 15

# Calculate π
pi = mp.pi

# Compute π^3
pi_cubed = mp.power(pi, 3)

# Compute ln(2)
ln2 = mp.log(2)

# Calculate the first part: (π^3 / 48) * (1 - ln(2))
factor1 = pi_cubed / 48
factor2 = 1 - ln2
term1 = factor1 * factor2

# Compute ζ(3) - Riemann zeta function at 3
zeta3 = mp.zeta(3)

# Calculate the second part: (π / 8) * ζ(3)
term2 = (pi / 8) * zeta3

# Sum both terms
result = term1 + term2

# Print the final result to 10 decimal places
print(mp.nstr(result, n=10))