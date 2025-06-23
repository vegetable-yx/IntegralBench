import mpmath as mp

# Set internal decimal precision to 15 for intermediate calculations
mp.dps = 15

# Calculate the coefficient: 315 divided by 8
coefficient = mp.mpf(315) / mp.mpf(8)

# Compute ζ(5) - the Riemann zeta function at 5
zeta5 = mp.zeta(5)

# Multiply coefficient by ζ(5) to get final result
result = coefficient * zeta5

# Print the result rounded to 10 decimal places
print(mp.nstr(result, n=10))