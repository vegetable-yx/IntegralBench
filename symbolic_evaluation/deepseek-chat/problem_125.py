import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate ln(2) using mpmath
ln2 = mp.log(2)

# Compute the term (1 - 2 * ln(2))
inner_expr = 1 - 2 * ln2

# Calculate the constant fraction 128/525
fraction = mp.mpf(128) / mp.mpf(525)

# Multiply the fraction by the inner expression
result = fraction * inner_expr

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))