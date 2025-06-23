import mpmath as mp

# Set internal decimal places for precision
mp.dps = 15

# Compute pi and natural logarithm of 2
pi_val = mp.pi
ln2_val = mp.ln(2)

# Calculate term1: pi^3 / 48
term1 = (pi_val ** 3) / 48

# Calculate term2: (pi / 4) * (ln(2))^2
term2 = (pi_val / 4) * (ln2_val ** 2)

# Subtract term2 from term1 to get the result
result = term1 - term2

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))