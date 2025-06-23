import mpmath as mp

# Set decimal places for internal calculations
mp.dps = 15

# Define constants and intermediate values
sqrt2 = mp.sqrt(2)  # Square root of 2
log_term = mp.log(1 + sqrt2)  # Natural log of (1 + sqrt(2))
log_sq = log_term ** 2  # Square of the log term

# First term: (π/8) * [ln(1+√2)]^2
term1 = (mp.pi / 8) * log_sq

# Arguments for the dilogarithms
arg1 = (1 - 1/sqrt2) / 2  # (1 - 1/√2) / 2
arg2 = (1 + 1/sqrt2) / 2  # (1 + 1/√2) / 2

# Compute the dilogarithms (polylog of order 2)
dilog1 = mp.polylog(2, arg1)
dilog2 = mp.polylog(2, arg2)

# Second term: (1/8) * (dilog1 - dilog2)
term2 = (1/8) * (dilog1 - dilog2)

# Sum both terms
result = term1 + term2

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))