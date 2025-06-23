import mpmath as mp

# Set decimal places for internal calculations
mp.dps = 15

# Calculate intermediate values
sqrt2 = mp.sqrt(2)  # Compute square root of 2
log_arg = 1 + sqrt2  # Argument for the logarithm
log_val = mp.log(log_arg)  # Compute ln(1 + sqrt(2))

# First term: (π/8) * [ln(1+√2)]^2
term1 = (mp.pi / 8) * (log_val ** 2)

# Arguments for the dilogarithm functions
arg1 = (sqrt2 - 1) ** 2  # (√2 - 1)^2
arg2 = 2 * sqrt2 - 2     # 2√2 - 2

# Compute dilogarithm values
li2_arg1 = mp.polylog(2, arg1)  # Li₂((√2 - 1)^2)
li2_arg2 = mp.polylog(2, arg2)  # Li₂(2√2 - 2)

# Second term: (1/4) * [Li₂((√2 - 1)^2) - Li₂(2√2 - 2)]
term2 = (1/4) * (li2_arg1 - li2_arg2)

# Combine terms for final result
result = term1 + term2

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))