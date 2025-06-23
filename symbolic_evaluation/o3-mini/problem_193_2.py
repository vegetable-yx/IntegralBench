import mpmath as mp

# Set decimal places for internal precision
mp.dps = 15

# Compute constant: sqrt(2)
sqrt2 = mp.sqrt(2)

# Compute logarithm: ln(1 + sqrt(2))
ln_val = mp.log(1 + sqrt2)

# Compute the two arguments for polylogarithms
a = 0.5 - 1/(2*sqrt2)
b = 0.5 + 1/(2*sqrt2)

# Compute the sum of dilogarithms (Li2) at a and b
dilog_sum = mp.polylog(2, a) + mp.polylog(2, b)

# Compute the sum of trilogarithms (Li3) at a and b
trilog_sum = mp.polylog(3, a) + mp.polylog(3, b)

# Compute the three terms in the main expression
term1 = mp.pi * (ln_val ** 3)
term2 = -6 * ln_val * dilog_sum
term3 = 6 * trilog_sum

# Combine terms and divide by 8
total = term1 + term2 + term3
result = total / 8

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))