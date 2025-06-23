import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute frequently used constants
sqrt2 = mp.sqrt(2)  # square root of 2
one_plus_sqrt2 = 1 + sqrt2  # (1 + sqrt(2))

# Compute the logarithm ln(1 + sqrt(2))
ln_val = mp.log(one_plus_sqrt2)

# Compute the arguments for the polylog functions
arg1 = 1 - sqrt2  # (1 - sqrt(2)), which is negative
arg2 = 1 / one_plus_sqrt2  # 1/(1 + sqrt(2)) = sqrt(2) - 1

# Compute the polylogarithms: Li2(1 - sqrt(2)), Li3(1 - sqrt(2)), Li3(1/(1 + sqrt(2)))
li2_arg1 = mp.polylog(2, arg1)
li3_arg1 = mp.polylog(3, arg1)
li3_arg2 = mp.polylog(3, arg2)

# Compute the cube of the logarithm
ln_cubed = ln_val ** 3

# Calculate each term in the expression
term1 = (3 + 2 * sqrt2) * ln_cubed
term2 = -6 * ln_val * li2_arg1
term3 = -12 * li3_arg1
term4 = 12 * li3_arg2

# Combine terms and divide by 64
result = (term1 + term2 + term3 + term4) / 64

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))