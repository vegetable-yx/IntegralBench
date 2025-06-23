import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate ln(2) using mpmath
ln2 = mp.log(2)

# Compute the term (π - 4*ln(2))
pi_minus_4ln2 = mp.pi - 4 * ln2

# Multiply by π to get numerator: π*(π - 4*ln(2))
numerator = mp.pi * pi_minus_4ln2

# Divide by 16 to get the final result
result = numerator / 16

# Print the result formatted to 10 decimal places
print(mp.nstr(result, n=10))