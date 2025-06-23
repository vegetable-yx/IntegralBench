import mpmath as mp

# Set internal decimal places for precision
mp.dps = 15

# Compute term1: π/8
term1 = mp.pi / 8

# Compute the argument for the logarithm: (3 + 2√3)/(3 - 2√3)
sqrt3 = mp.sqrt(3)
numerator = 3 + 2 * sqrt3
denominator = 3 - 2 * sqrt3
log_arg = numerator / denominator

# Compute term2: - (√3 / 4) * ln(log_arg)
term2 = - (sqrt3 / 4) * mp.log(log_arg)

# Compute the complex arguments for the dilogarithms
z1 = 0.5 - 0.5j * sqrt3  # 1/2 - i√3/2
z2 = 0.5 + 0.5j * sqrt3  # 1/2 + i√3/2

# Compute the dilogarithms for both complex points
dilog1 = mp.polylog(2, z1)
dilog2 = mp.polylog(2, z2)

# Compute term3: (1/8) * [Li2(z1) + Li2(z2)]
term3 = (dilog1 + dilog2) / 8

# Sum all terms to get the final result
result = term1 + term2 + term3

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))