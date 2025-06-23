import mpmath as mp

# Set the internal precision to 15 decimal places
mp.dps = 15

# Compute the hypergeometric function {}_1F_2(3/2; 2, 2; -1)
hyper_val = mp.hyper([mp.mpf('1.5')], [2, 2], -1)

# Multiply by π and divide by 8
result = (mp.pi / 8) * hyper_val

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))