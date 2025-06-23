import mpmath as mp

# Set the decimal places for internal calculations to 15 for accuracy
mp.dps = 15

# Define the parameters for the hypergeometric function
a = mp.mpf(1)/mp.mpf(2)  # a = 1/2
# Compute b = (3 + 2*sqrt(2)) / 4
b_numerator = mp.mpf(3) + mp.mpf(2) * mp.sqrt(2)
b = b_numerator / mp.mpf(4)
# Compute c = (7 + 2*sqrt(2)) / 4
c_numerator = mp.mpf(7) + mp.mpf(2) * mp.sqrt(2)
c = c_numerator / mp.mpf(4)
z = mp.mpf(-1)  # z = -1

# Compute the hypergeometric function _2F_1(a, b; c; z)
hyper_result = mp.hyp2f1(a, b, c, z)

# Multiply the hypergeometric result by pi/16
result = (mp.pi / mp.mpf(16)) * hyper_result

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))