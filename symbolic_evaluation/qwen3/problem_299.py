import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Compute Gamma(1/4)
gamma_1_4 = mp.gamma(mp.mpf(1)/4)

# Square the Gamma(1/4) value
gamma_sq = gamma_1_4 ** 2

# Compute the square root of 2*pi
sqrt_2pi = mp.sqrt(2 * mp.pi)

# Calculate the first part of the expression (Gamma^2 / sqrt(2π))
gamma_part = gamma_sq / sqrt_2pi

# Compute π/2 and ln(2)
pi_half = mp.pi / 2
ln2 = mp.log(2)

# Sum π/2 and ln(2)
sum_part = pi_half + ln2

# Multiply both parts to get the final result
result = gamma_part * sum_part

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))