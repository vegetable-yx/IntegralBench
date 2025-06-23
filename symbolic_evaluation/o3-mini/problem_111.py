import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate frequently used constants and intermediate values
sqrt2 = mp.sqrt(2)  # Square root of 2
one_over_sqrt2 = 1 / sqrt2  # 1/sqrt(2)
t_arg = (sqrt2 + 1) / (sqrt2 - 1)  # Argument for logarithmic terms: (√2+1)/(√2-1)
log_t = mp.log(t_arg)  # Natural logarithm of t_arg

# Compute polylogarithmic terms
li3_pos = mp.polylog(3, one_over_sqrt2)  # Li₃(1/√2)
li3_neg = mp.polylog(3, -one_over_sqrt2)  # Li₃(-1/√2)
li2_pos = mp.polylog(2, one_over_sqrt2)  # Li₂(1/√2)

# Compute pi^3
pi_cubed = mp.pi ** 3

# Compute the logarithmic squared term
log_sq = log_t ** 2  # [ln((√2+1)/(√2-1))]^2

# Assemble the expression inside the brackets
inner_expr = (
    16 * li3_pos
    - 16 * li3_neg
    - 8 * log_t * li2_pos
    - pi_cubed
    - 6 * mp.pi * log_sq
)

# Multiply by the constant factor: √2 / 24
result = (sqrt2 / 24) * inner_expr

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))