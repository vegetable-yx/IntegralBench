import mpmath as mp

# Set the precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate the first part: pi * (1/sqrt(2) - 1/2)
sqrt2 = mp.sqrt(2)  # Compute square root of 2
term1 = mp.mpf(1) / sqrt2  # 1/sqrt(2)
term2 = term1 - mp.mpf('0.5')  # (1/sqrt(2) - 1/2)
part1 = mp.pi * term2  # pi multiplied by the difference

# Calculate the second part: (pi/4) * ln((3 + 2*sqrt(2))/4
inner_num = 3 + 2 * sqrt2  # Numerator: 3 + 2*sqrt(2)
fraction = inner_num / 4  # Divide by 4: (3 + 2*sqrt(2))/4
log_val = mp.log(fraction)  # Natural logarithm of the fraction
part2 = (mp.pi / 4) * log_val  # (pi/4) multiplied by the logarithm

# Combine the parts: result = part1 - part2
result = part1 - part2

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))