import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate π cubed divided by 24
pi_cubed = mp.power(mp.pi, 3)
part1 = pi_cubed / 24

# Calculate (ln 2) squared
ln2 = mp.log(2)
ln2_sq = mp.power(ln2, 2)

# Calculate the second term: (3 * π * (ln2)^2) / 8
part2 = (3 * mp.pi * ln2_sq) / 8

# Combine the parts: result = part1 - part2
result = part1 - part2

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))