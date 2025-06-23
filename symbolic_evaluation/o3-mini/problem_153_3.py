import mpmath as mp

# Set internal decimal places for sufficient precision
mp.dps = 15

# Compute constants
sqrt2 = mp.sqrt(2)
inv_sqrt2 = 1 / sqrt2  # 1/sqrt(2)

# Arguments for the dilogarithm functions
arg1 = 1 - inv_sqrt2  # 1 - 1/sqrt(2)
arg2 = 1 + inv_sqrt2  # 1 + 1/sqrt(2)

# Compute the dilogarithms
Li2_1 = mp.polylog(2, arg1)  # Li₂(1 - 1/√2)
Li2_2 = mp.polylog(2, arg2)  # Li₂(1 + 1/√2)

# First term: (1/8)[Li₂(1-1/√2) - Li₂(1+1/√2)]
term1 = (Li2_1 - Li2_2) / 8

# Argument for the logarithm: (√2 + 1)/2
log_arg = (sqrt2 + 1) / 2
log_val = mp.log(log_arg)  # Natural logarithm of the argument
log_sq = log_val ** 2      # Squared logarithm

# Second term: (π/8) * [ln((√2+1)/2)]²
term2 = (mp.pi / 8) * log_sq

# Sum the terms for the final result
result = term1 + term2

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))