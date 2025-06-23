import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Compute the hypergeometric function _0F1(; 3/4; -1)
hyp = mp.hyper0f1(3/4, -1)

# Multiply the result by pi
result = mp.pi * hyp

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))