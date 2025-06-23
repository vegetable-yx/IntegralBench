import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define the arguments for the hypergeometric function 3F2
# Numerator parameters: a1 = 1/2, a2 = 1/2, a3 = 1
a = [mp.mpf('0.5'), mp.mpf('0.5'), mp.mpf(1)]
# Denominator parameters: b1 = 3/2, b2 = 3/2
b = [mp.mpf('1.5'), mp.mpf('1.5')]
# Argument z = 1
z = mp.mpf(1)

# Compute the hypergeometric function value
hyper_val = mp.hyper(a, b, z)

# Multiply by pi/4
result = mp.pi / 4 * hyper_val

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))