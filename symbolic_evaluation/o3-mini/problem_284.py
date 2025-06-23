import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute frequently used constant: sqrt(2)
sqrt2 = mp.sqrt(2)

# Calculate the logarithm term: ln(1 + sqrt(2))
log_term = mp.log(1 + sqrt2)

# Compute first part: (π/8) * [ln(1 + sqrt(2))]^2
part1 = (mp.pi / 8) * (log_term ** 2)

# Compute arguments for dilogarithms
arg1 = 1 - sqrt2   # 1 - sqrt(2) ≈ -0.4142
arg2 = sqrt2 - 1   # sqrt(2) - 1 ≈ 0.4142

# Calculate dilogarithms: Li₂(1 - sqrt(2)) and Li₂(sqrt(2) - 1)
dilog1 = mp.polylog(2, arg1)
dilog2 = mp.polylog(2, arg2)

# Compute second part: (1/4) * [Li₂(1 - sqrt(2)) - Li₂(sqrt(2) - 1)]
part2 = (1/4) * (dilog1 - dilog2)

# Sum both parts to get final result
result = part1 + part2

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))