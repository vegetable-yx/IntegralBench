import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate common constants and arguments
sqrt3 = mp.sqrt(3)

# Argument for the first logarithm: (sqrt3 + 1)/2
arg1 = (sqrt3 + 1) / 2
ln1 = mp.log(arg1)  # First logarithmic term

# Argument for the second logarithm: (3 + 2*sqrt3)/3
arg2 = (3 + 2 * sqrt3) / 3
ln2 = mp.log(arg2)  # Second logarithmic term

# Argument for the dilogarithm: (1 - sqrt3)/2
arg_dilog = (1 - sqrt3) / 2
dilog_term = mp.polylog(2, arg_dilog)  # Dilogarithm term

# Compute each term in the expression
term1 = 128 * (ln1 ** 2)  # 128 * ln^2((√3+1)/2)
term2 = -64 * ln1 * ln2   # -64 * ln1 * ln2
term3 = 27 * mp.pi        # 27π
term4 = -96 * sqrt3 * ln2 # -96√3 * ln2
term5 = 256 * dilog_term  # 256 * Li₂((1-√3)/2)

# Sum all terms and divide by 6912
total_sum = term1 + term2 + term3 + term4 + term5
result = total_sum / 6912

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))