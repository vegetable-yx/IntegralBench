import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate common constants
sqrt3 = mp.sqrt(3)  # sqrt(3)
one_over_sqrt3 = 1 / sqrt3  # 1/sqrt(3)

# Compute the logarithmic term: ln(3)
ln3 = mp.log(3)

# Compute the constant term: π/3
pi_over_3 = mp.pi / 3

# Compute the logarithmic part: ln(3) * π/3
log_term = ln3 * pi_over_3

# Compute the dilogarithm terms
# Li₂(-√3)
dilog1 = mp.polylog(2, -sqrt3)
# Li₂(-1/√3)
dilog2 = mp.polylog(2, -one_over_sqrt3)

# Combine the terms inside the parentheses: log_term - dilog1 + dilog2
inner_expr = log_term - dilog1 + dilog2

# Multiply by 1/sqrt(3) to get the final result
result = one_over_sqrt3 * inner_expr

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))