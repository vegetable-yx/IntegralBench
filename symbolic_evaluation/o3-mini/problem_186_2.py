import mpmath as mp

# Set internal decimal places for precision
mp.dps = 15

# Define the argument for the functions
a = 1 / (mp.sqrt(2) + mp.sqrt(3))
arg = 1 / a  # This is 1/(sqrt(2)+sqrt(3))

# Compute arctanh of the argument
atanh_term = mp.atanh(arg)

# Multiply by pi
pi_atanh = mp.pi * atanh_term

# Compute the dilogarithm terms
dilog_neg = mp.polylog(2, -arg)
dilog_pos = mp.polylog(2, arg)

# Combine the terms: pi * arctanh + (-dilog_neg) + dilog_pos
combined = pi_atanh - dilog_neg + dilog_pos

# Multiply by 1/8
result = combined / 8

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))