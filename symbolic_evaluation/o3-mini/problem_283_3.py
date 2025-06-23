import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the square root of 5
sqrt5 = mp.sqrt(5)

# Calculate the golden ratio (positive root)
golden_ratio = (1 + sqrt5) / 2

# Compute the logarithmic term: (π/4) * ln((1+√5)/2)
log_term = (mp.pi / 4) * mp.log(golden_ratio)

# Compute the two arguments for the dilogarithm function
arg1 = (1 - sqrt5) / 2  # This is negative
arg2 = (sqrt5 - 1) / 2  # This is positive

# Evaluate the dilogarithm for both arguments
dilog1 = mp.polylog(2, arg1)
dilog2 = mp.polylog(2, arg2)

# Compute the dilogarithm difference term: (1/4)[Li₂(arg1) - Li₂(arg2)]
dilog_diff_term = (dilog1 - dilog2) / 4

# Combine both terms to get the final result
result = log_term + dilog_diff_term

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))