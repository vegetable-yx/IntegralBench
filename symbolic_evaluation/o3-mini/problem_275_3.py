import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define parameters a and b (example values - can be modified)
a = mp.mpf(1)  # Parameter a (set to 1.0 as example)
b = mp.mpf(1)  # Parameter b (set to 1.0 as example)

# Compute the argument for the hypergeometric function: (a^2 * b^2)/16
arg = (a**2 * b**2) / 16

# Compute the confluent hypergeometric limit function _0F_1(; 5/2; arg)
hyp_val = mp.hyper([], [mp.mpf(5)/2], arg)

# Compute the coefficient: (2/3) * a^(3/2)
coeff = (mp.mpf(2)/3) * (a ** (mp.mpf(3)/2))

# Multiply coefficient by hypergeometric function value
result = coeff * hyp_val

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))