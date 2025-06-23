import mpmath as mp

# Set decimal places for internal calculations
mp.dps = 15

# Compute the hypergeometric function value: _2F_1(1, 1/2; 2; 1/2)
hyp2f1_val = mp.hyp2f1(1, 0.5, 2, 0.5)

# Multiply by pi to get the final result
result = mp.pi * hyp2f1_val

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))