import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Compute common constants
sqrt3 = mp.sqrt(3)
half = mp.mpf('0.5')

# Calculate the argument for the logarithm and dilogarithm functions
arg_log = (sqrt3 + 1) * half  # (sqrt(3) + 1)/2
arg_dilog1 = half - sqrt3 * half  # 1/2 - sqrt(3)/2 = (1 - sqrt(3))/2
arg_dilog2 = arg_log  # same as above: (sqrt(3) + 1)/2

# Compute each term in the expression
# Term 1: sqrt(3) * pi
term1 = sqrt3 * mp.pi

# Term 2: 4 * [ln((sqrt(3)+1)/2)]^2
log_val = mp.log(arg_log)
term2 = 4 * (log_val ** 2)

# Term 3: -8 * Li_2((1 - sqrt(3))/2)
dilog1 = mp.polylog(2, arg_dilog1)
term3 = -8 * dilog1

# Term 4: 8 * Li_2((sqrt(3)+1)/2)
dilog2 = mp.polylog(2, arg_dilog2)
term4 = 8 * dilog2

# Sum all terms and divide by 8
total = term1 + term2 + term3 + term4
result = total / 8

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))