import mpmath as mp

# Set internal decimal precision to 15 for intermediate calculations
mp.dps = 15

# Compute π/4
term1 = mp.pi / 4

# Compute (1/2) * ln(2)
term2 = 0.5 * mp.log(2)

# Combine all terms: π/4 + (1/2)*ln(2) - 1
result = term1 + term2 - 1

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))