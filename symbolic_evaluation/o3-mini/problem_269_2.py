import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Precompute frequently used constants
sqrt3 = mp.sqrt(3)
pi = mp.pi

# Compute the logarithmic argument: (sqrt(3) + 1)/2
log_arg = (sqrt3 + 1) / 2

# Compute the logarithm: ln((sqrt(3) + 1)/2)
ln_term = mp.log(log_arg)

# Compute part1: 8 * sqrt(3) * ln_term
part1 = 8 * sqrt3 * ln_term

# Compute part2: pi * (16 - 6*sqrt(3) - 16*ln_term
part2 = pi * (16 - 6*sqrt3 - 16*ln_term)

# Compute the complex argument for dilogarithm: (1 + i*sqrt(3))/2
z_arg = (1 + 1j * sqrt3) / 2

# Compute dilogarithm value (complex number)
dilog_val = mp.polylog(2, z_arg)

# Extract imaginary part of the dilogarithm
imag_part = dilog_val.imag

# Compute part3: 16 * imag_part
part3 = 16 * imag_part

# Sum all parts
total = part1 + part2 + part3

# Final result: total divided by 48
result = total / 48

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))