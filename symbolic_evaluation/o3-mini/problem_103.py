import mpmath as mp

# Set decimal places for internal precision
mp.dps = 15

# Calculate constants and intermediate values
sqrt3 = mp.sqrt(3)  # Square root of 3
pi = mp.pi  # Pi constant

# Compute the two arguments for the dilogarithm function
arg1 = (1 + sqrt3) / 2  # (1 + sqrt(3))/2
arg2 = (1 - sqrt3) / 2  # (1 - sqrt(3))/2

# Calculate the two dilogarithm terms
li2_arg1 = mp.polylog(2, arg1)  # Li_2((1 + sqrt(3))/2)
li2_arg2 = mp.polylog(2, arg2)  # Li_2((1 - sqrt(3))/2)

# Compute the constant term: sqrt(3)*pi/12
constant_term = (sqrt3 * pi) / 12

# Compute the dilogarithm difference term: (1/4)*(li2_arg1 - li2_arg2)
dilog_diff_term = (1/4) * (li2_arg1 - li2_arg2)

# Combine both terms to get final result
result = constant_term + dilog_diff_term

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))