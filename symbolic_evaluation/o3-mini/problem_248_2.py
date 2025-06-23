import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate square root of 5
sqrt5 = mp.sqrt(5)

# Compute the argument for the logarithm: (3 + sqrt(5)) / (3 - sqrt(5))
num_log = 3 + sqrt5
den_log = 3 - sqrt5
log_arg = num_log / den_log

# First term: (pi/4) * ln(log_arg)
term1 = (mp.pi / 4) * mp.log(log_arg)

# Compute arguments for the dilogarithm functions
# First argument: (sqrt(5) - 1) / (2 * sqrt(5))
arg1 = (sqrt5 - 1) / (2 * sqrt5)

# Second argument: -(sqrt(5) + 1) / (2 * sqrt(5))
arg2 = -(sqrt5 + 1) / (2 * sqrt5)

# Compute dilogarithm values
dilog1 = mp.polylog(2, arg1)
dilog2 = mp.polylog(2, arg2)

# Second term: (1/2) * [dilog1 - dilog2]
term2 = 0.5 * (dilog1 - dilog2)

# Sum both terms
result = term1 + term2

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))