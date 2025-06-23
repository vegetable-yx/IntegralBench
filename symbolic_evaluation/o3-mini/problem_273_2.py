import mpmath as mp

# Set internal decimal precision to 15 for calculations
mp.dps = 15

# Compute term1: π²/96
term1 = mp.pi**2 / 96

# Compute the argument for the logarithm: (√2 - 1)/(√2 + 1)
sqrt2 = mp.sqrt(2)
log_arg = (sqrt2 - 1) / (sqrt2 + 1)

# Compute term2: (1/64) * [ln(log_arg)]²
log_val = mp.log(log_arg)
term2 = (1/64) * (log_val**2)

# Compute the arguments for the dilogarithms
a = 1 - sqrt2  # 1 - √2 (negative)
b = 1 + sqrt2  # 1 + √2 (positive)

# Compute term3: (1/32) * [Li₂(a) - Li₂(b)]
dilog1 = mp.polylog(2, a)
dilog2 = mp.polylog(2, b)
term3 = (1/32) * (dilog1 - dilog2)

# Sum all terms to get the final result
result = term1 + term2 + term3

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))