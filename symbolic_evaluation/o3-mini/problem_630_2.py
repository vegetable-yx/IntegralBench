import mpmath as mp

# Set internal decimal precision to 15 for intermediate calculations
mp.dps = 15

# Calculate the constant square root of 3
sqrt3 = mp.sqrt(3)

# Compute the complex arguments for the first pair of dilogarithms
z1 = 1j * sqrt3    # i * sqrt(3)
z2 = -1j * sqrt3   # -i * sqrt(3)

# Compute the complex arguments for the second pair of dilogarithms
z3 = 1j / sqrt3    # i / sqrt(3)
z4 = -1j / sqrt3   # -i / sqrt(3)

# Evaluate dilogarithms for the first pair and compute their difference
dilog_diff1 = mp.polylog(2, z1) - mp.polylog(2, z2)
# Extract the imaginary part of the first difference
imag_part1 = mp.im(dilog_diff1)

# Evaluate dilogarithms for the second pair and compute their difference
dilog_diff2 = mp.polylog(2, z3) - mp.polylog(2, z4)
# Extract the imaginary part of the second difference
imag_part2 = mp.im(dilog_diff2)

# Compute the numerator: (Im[Li2(i√3)-Li2(-i√3)] - Im[Li2(i/√3)-Li2(-i/√3)])
numerator = imag_part1 - imag_part2

# Compute the denominator: 2 * sqrt(3)
denominator = 2 * sqrt3

# Calculate the final result
result = numerator / denominator

# Print the result rounded to 10 decimal places
print(mp.nstr(result, n=10))