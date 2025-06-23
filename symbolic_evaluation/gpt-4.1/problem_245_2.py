import mpmath as mp

# Set internal decimal precision to 15 digits
mp.dps = 15

# Define the constant factor: 48/105 simplifies to 16/35
const = mp.mpf(48) / mp.mpf(105)

# Parameters for the hypergeometric function {}_4F_3
# Numerator parameters: [3, 3, 4, 4]
a1 = 3
a2 = 3
a3 = 4
a4 = 4

# Denominator parameters: [1, 1, 9/2]
b1 = 1
b2 = 1
b3 = mp.mpf(9)/2

# Evaluate the generalized hypergeometric function at z=1
hyper_val = mp.hyper([a1, a2, a3, a4], [b1, b2, b3], 1)

# Multiply by the constant factor
result = const * hyper_val

# Print the final result with exactly 10 decimal places
print(mp.nstr(result, n=10))