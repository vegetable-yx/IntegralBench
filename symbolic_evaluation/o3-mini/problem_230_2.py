import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the constant terms
pi = mp.pi
sqrt2 = mp.sqrt(2)

# Compute the argument for the logarithm: (1 + sqrt(2))
log_arg = 1 + sqrt2

# Compute the natural logarithm: ln(1 + sqrt(2))
ln_val = mp.log(log_arg)

# Calculate the powers of the logarithm
ln_sq = ln_val ** 2
ln_cu = ln_val ** 3

# Calculate the numerator: π^3 - 12π(ln(1+√2))^2 + 8(ln(1+√2))^3
term1 = pi ** 3
term2 = 12 * pi * ln_sq
term3 = 8 * ln_cu
numerator = term1 - term2 + term3

# Divide by 48 to get the result
result = numerator / 48

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))