import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the hypergeometric function 2F1(1, 1/2; 2; 2)
hyp_val = mp.hyp2f1(1, 0.5, 2, 2)

# Multiply by pi to get the final result
result = mp.pi * hyp_val

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))