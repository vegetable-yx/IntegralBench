import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Base value
base = 2

# Positive exponent: 2/3
exponent = mp.mpf(2) / 3

# Compute base raised to the exponent (2^(2/3))
base_raised = base ** exponent

# Take the reciprocal to get 2^(-2/3)
result = 1 / base_raised

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))