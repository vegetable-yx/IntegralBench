import mpmath as mp

# Set internal decimal precision to 15 for calculations
mp.dps = 15

# Define the parameters for the hypergeometric function
# Numerator parameters: a = [-1/2, -1/2, 1/4, 3/4]
a1 = mp.mpf('-0.5')  # -1/2
a2 = mp.mpf('-0.5')  # -1/2
a3 = mp.mpf('0.25')  # 1/4
a4 = mp.mpf('0.75')  # 3/4
a_params = [a1, a2, a3, a4]

# Denominator parameters: b = [1, 1, 1]
b1 = mp.mpf('1')
b2 = mp.mpf('1')
b3 = mp.mpf('1')
b_params = [b1, b2, b3]

# Argument of the hypergeometric function
z_val = mp.mpf('0.25')  # 1/4

# Compute the generalized hypergeometric function 4F3
hyper_term = mp.hyper(a_params, b_params, z_val)

# Compute pi squared
pi_sq = mp.pi ** 2

# Multiply by pi^2/4 to get the final result
result = (pi_sq / 4) * hyper_term

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))