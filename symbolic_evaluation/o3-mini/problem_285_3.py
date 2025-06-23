import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Precompute frequently used constants
sqrt2 = mp.sqrt(2)
ln_arg = 1 + sqrt2  # Argument for logarithm

# Compute ln(1 + sqrt(2))
ln_val = mp.log(ln_arg)

# Term 1: (pi/8) * [ln(1+sqrt(2))]^2
term1 = (mp.pi / 8) * (ln_val ** 2)

# Compute argument for Li2: 1/2 - 1/(2*sqrt(2))
arg_li2 = 0.5 - 0.5 / sqrt2

# Compute Li2 for the argument
li2_val = mp.polylog(2, arg_li2)

# Term 2: (1/4) * ln(1+sqrt(2)) * Li2(1/2 - 1/(2*sqrt(2)))
term2 = (1/4) * ln_val * li2_val

# Compute arguments for Li3 terms
arg_li3a = 1 - 1/sqrt2  # 1 - 1/sqrt(2)
arg_li3b = 1/sqrt2      # 1/sqrt(2)

# Compute Li3 for both arguments
li3a = mp.polylog(3, arg_li3a)
li3b = mp.polylog(3, arg_li3b)

# Term 3: (1/8) * [Li3(1-1/sqrt(2)) - Li3(1/sqrt(2))]
term3 = (1/8) * (li3a - li3b)

# Combine all terms: term1 - term2 + term3
result = term1 - term2 + term3

# Print the final result with 10 decimal places
print(mp.nstr(result, n=10))