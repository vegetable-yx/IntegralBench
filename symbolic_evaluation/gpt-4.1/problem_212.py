import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the hypergeometric function component: _0F_1(; 3; -1)
hyper_term = mp.hyp0f1(3, -1)

# Multiply by pi/4
result = (mp.pi / 4) * hyper_term

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))