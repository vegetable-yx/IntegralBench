import mpmath as mp

# Set decimal places for internal precision
mp.dps = 15

# Calculate intermediate values
sqrt24 = mp.sqrt(24)  # Compute square root of 24
denominator = 5 + sqrt24  # Denominator for b parameter
b_val = 1 / denominator  # b parameter: 1/(5 + sqrt(24))
a_val = mp.mpf(0.5)  # a parameter: 1/2
c_val = a_val + b_val  # c parameter: a + b

# Evaluate hypergeometric function 2F1(a, b; c; z) with z = -1
hyp_val = mp.hyp2f1(a_val, b_val, c_val, -1)

# Compute final result: (π/8) * hypergeometric value
result = (mp.pi / 8) * hyp_val

# Print result to 10 decimal places
print(mp.nstr(result, n=10))