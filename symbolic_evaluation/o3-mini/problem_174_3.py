import mpmath as mp

# Set the decimal places for internal precision
mp.dps = 15

# Compute the hypergeometric function term: {}_3F_2(1/2, 1/2, 1; 3/2, 3/2; 1/16)
# Parameters: a = [0.5, 0.5, 1], b = [1.5, 1.5], z = 1/16
hyper_term = mp.hyper([0.5, 0.5, 1], [1.5, 1.5], 1/16)

# Multiply by π/64
result = (mp.pi / 64) * hyper_term

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))