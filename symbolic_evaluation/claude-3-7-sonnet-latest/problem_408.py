import mpmath as mp

# Set internal decimal precision to 15 digits for calculations
mp.dps = 15

# Calculate the logarithm term: ln(5/3)
log_term = mp.log(mp.mpf('5') / mp.mpf('3'))

# Multiply the logarithm by 1/8
part1 = log_term / mp.mpf('8')

# Compute the constant term: -1/20
part2 = mp.mpf('-1') / mp.mpf('20')

# Combine both parts
result = part1 + part2

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))