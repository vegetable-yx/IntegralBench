import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Define constants and intermediate values
sqrt2 = mp.sqrt(2)  # √2
one_over_sqrt2 = 1 / sqrt2  # 1/√2
one_minus_one_over_sqrt2 = 1 - one_over_sqrt2  # 1 - 1/√2
log_arg = (1 + sqrt2) / 2  # (1 + √2)/2

# Compute polylog terms
li3_term1 = mp.polylog(3, one_over_sqrt2)  # Li₃(1/√2)
li3_term2 = mp.polylog(3, one_minus_one_over_sqrt2)  # Li₃(1 - 1/√2)
li2_term = mp.polylog(2, one_minus_one_over_sqrt2)  # Li₂(1 - 1/√2)

# Compute logarithmic term and its square
ln_val = mp.log(log_arg)  # ln((1 + √2)/2)
ln_squared = ln_val ** 2  # [ln((1 + √2)/2)]²

# Compute the product term: ln((1+√2)/2) * Li₂(1 - 1/√2)
product_term = ln_val * li2_term

# Compute the pi term: (π/8) * [ln((1+√2)/2)]²
pi_term = (mp.pi / 8) * ln_squared

# Combine terms inside the braces
inner_expr = li3_term1 - li3_term2 + product_term - pi_term

# Multiply by √2 to get final result
result = sqrt2 * inner_expr

# Print result with 10 decimal places
print(mp.nstr(result, n=10))