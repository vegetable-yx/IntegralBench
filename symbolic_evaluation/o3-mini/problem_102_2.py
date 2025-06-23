import mpmath as mp

# Set internal decimal precision to 15 for intermediate calculations
mp.dps = 15

# Define frequently used constant: square root of 3
sqrt3 = mp.sqrt(3)

# Simplify the logarithm argument: (sqrt(3) + 1)/(sqrt(3) - 1) = 2 + sqrt(3)
log_arg = 2 + sqrt3

# Compute Part 1: (π/12) * ln(2 + sqrt(3))
part1 = (mp.pi / 12) * mp.log(log_arg)

# Compute arguments for the dilogarithm terms
arg1 = 1 - sqrt3/2  # ≈ 0.134
arg2 = 1 + sqrt3/2  # ≈ 1.866

# Calculate dilogarithms
dilog1 = mp.polylog(2, arg1)
dilog2 = mp.polylog(2, arg2)

# Compute the difference between dilogarithms
dilog_diff = dilog1 - dilog2

# Compute Part 2: [1/(4√3)] * (dilog_diff)
part2 = (1 / (4 * sqrt3)) * dilog_diff

# Combine parts to get the final result
result = part1 - part2

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))