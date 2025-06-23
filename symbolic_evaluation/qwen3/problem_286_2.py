import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Compute sqrt(2)
sqrt2 = mp.sqrt(2)

# Compute ln(1 + sqrt(2))
ln_term = mp.log(1 + sqrt2)

# Calculate the first part: (π/8) * [ln(1 + sqrt(2))]^2
part1 = (mp.pi / 8) * (ln_term ** 2)

# Calculate the second part: [ln(1 + sqrt(2))/4] * (sqrt(2) - 1)
part2 = (ln_term / 4) * (sqrt2 - 1)

# Combine both parts to get the final result
result = part1 - part2

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))