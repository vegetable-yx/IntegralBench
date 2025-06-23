import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define constants and intermediate values
sqrt3 = mp.sqrt(3)  # Compute square root of 3

# Calculate argument for logarithm: (sqrt(3) + 1)/2
log_arg = (sqrt3 + 1) / 2

# Calculate the argument for polylog terms: (sqrt(3) - 1)/2
poly_arg = (sqrt3 - 1) / 2

# Compute the first part: (π/12) * ln((sqrt(3)+1)/2)
part1 = (mp.pi / 12) * mp.log(log_arg)

# Compute the dilogarithm terms
dilog1 = mp.polylog(2, -poly_arg)  # Li₂(-(√3-1)/2)
dilog2 = mp.polylog(2, poly_arg)    # Li₂((√3-1)/2)

# Compute the second part: (1/24) * [Li₂(-(√3-1)/2) - Li₂((√3-1)/2)]
part2 = (1/24) * (dilog1 - dilog2)

# Sum both parts for final result
result = part1 + part2

# Print result to exactly 10 decimal places
print(mp.nstr(result, n=10))