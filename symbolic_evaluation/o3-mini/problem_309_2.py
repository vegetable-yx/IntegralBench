import mpmath as mp

# Set internal precision to 15 decimal places for accurate computation
mp.dps = 15

# Calculate π and √2
pi = mp.pi
sqrt2 = mp.sqrt(2)

# Compute the constant factor: (π * √2) / 4
constant_factor = pi * sqrt2 / 4

# Compute the difference of digamma functions: ψ(3/4) - ψ(1/4)
digamma_diff = mp.digamma(3/4) - mp.digamma(1/4)

# Multiply constant_factor by digamma_diff
part1 = constant_factor * digamma_diff

# Compute the logarithm term: ln((1 + √2) / 2)
log_arg = (1 + sqrt2) / 2
log_term = mp.log(log_arg)

# Multiply logarithm term by π
part2 = pi * log_term

# Sum the two parts for the final result
result = part1 + part2

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))