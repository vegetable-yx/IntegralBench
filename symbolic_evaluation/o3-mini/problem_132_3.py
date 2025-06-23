import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the constant factor: sqrt(pi)/4
sqrt_pi = mp.sqrt(mp.pi)
constant_factor = sqrt_pi / 4

# Compute the hypergeometric function _0F_1(; 5/2; 1/8)
# Using mp.hyper with empty top parameters and bottom parameter [5/2]
hyp_value = mp.hyper([], [mp.mpf(5)/2], mp.mpf(1)/8)

# Multiply constant factor by hypergeometric value
result = constant_factor * hyp_value

# Print result to exactly 10 decimal places
print(mp.nstr(result, n=10))