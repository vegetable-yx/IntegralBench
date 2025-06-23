import mpmath as mp

# Set internal decimal places for high precision
mp.dps = 15

# Compute constants
sqrt2 = mp.sqrt(2)  # Square root of 2
a = 1 / sqrt2       # 1/sqrt(2)
b = -a              # -1/sqrt(2)

# Compute logarithmic term: ln(1 + sqrt(2))
log_term = mp.log(1 + sqrt2)

# Compute polylog(3) values
Li3_a = mp.polylog(3, a)  # Li_3(1/sqrt(2))
Li3_b = mp.polylog(3, b)  # Li_3(-1/sqrt(2))

# Compute polylog(2) values
Li2_a = mp.polylog(2, a)  # Li_2(1/sqrt(2))
Li2_b = mp.polylog(2, b)  # Li_2(-1/sqrt(2))

# Compute the expression components
term1 = 4 * (Li3_a - Li3_b)
term2 = log_term * (Li2_b - Li2_a)

# Sum the components
result = term1 + term2

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))