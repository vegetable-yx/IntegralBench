import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute constants and intermediate values
sqrt2 = mp.sqrt(2)  # square root of 2

# Arguments for the dilogarithm functions
arg1 = 0.5 - 1/(2*sqrt2)  # 1/2 - 1/(2√2)
arg2 = 0.5 + 1/(2*sqrt2)  # 1/2 + 1/(2√2)

# Compute the two dilogarithms
li1 = mp.polylog(2, arg1)  # Li_2(1/2 - 1/(2√2))
li2 = mp.polylog(2, arg2)  # Li_2(1/2 + 1/(2√2))

# Compute the logarithm argument: (√2 - 1)/(√2 + 1)
log_arg = (sqrt2 - 1) / (sqrt2 + 1)

# Compute the logarithm and its square
log_val = mp.log(log_arg)
log_sq = log_val**2  # [ln((√2-1)/(√2+1))]^2

# Combine the terms inside the brackets: 4*(li1 - li2) + log_sq
bracket_term = 4*(li1 - li2) + log_sq

# Multiply by the factor: √2 / 16
part1 = (sqrt2 / 16) * bracket_term

# Compute the second part: (π/8) * [ln(1+√2)]^2
ln_val2 = mp.log(1 + sqrt2)  # ln(1+√2)
ln_sq2 = ln_val2**2          # [ln(1+√2)]^2
part2 = (mp.pi / 8) * ln_sq2

# Sum the two parts
result = part1 + part2

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))