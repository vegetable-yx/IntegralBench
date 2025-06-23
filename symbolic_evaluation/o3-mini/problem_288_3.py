import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Compute the constant sqrt(2)
sqrt2 = mp.sqrt(2)

# Compute the argument for the logarithm: (1 + sqrt(2))
log_arg = 1 + sqrt2

# Calculate ln(1 + sqrt(2))
ln_val = mp.log(log_arg)

# Cube the logarithm value
ln_cubed = ln_val**3

# Calculate the first term: π * ln^3(1+√2) / 96
term1 = (mp.pi * ln_cubed) / 96

# Compute arguments for the polylogarithms
arg1 = sqrt2 - 1  # √2 - 1 (positive)
arg2 = 1 - sqrt2  # 1 - √2 (negative)

# Calculate Li₃(√2 - 1) and Li₃(1 - √2)
Li3_arg1 = mp.polylog(3, arg1)
Li3_arg2 = mp.polylog(3, arg2)

# Compute the difference between the polylogarithms
Li3_diff = Li3_arg1 - Li3_arg2

# Calculate the second term: (1/8) * (Li₃(√2-1) - Li₃(1-√2))
term2 = (1/8) * Li3_diff

# Sum both terms to get the final result
result = term1 + term2

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))