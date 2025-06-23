import mpmath as mp

# Set internal decimal places for precision
mp.dps = 15

# Compute the hypergeometric function {}_3F_2(1/2,1,1; 3/2,2; 0.25)
hyp_val = mp.hyper([0.5, 1, 1], [1.5, 2], 0.25)

# Compute pi cubed
pi_cubed = mp.pi ** 3

# Compute the constant factor: pi^3 / 8
factor = pi_cubed / 8

# Multiply factor by the hypergeometric value
result = factor * hyp_val

# Print the final result to 10 decimal places
print(mp.nstr(result, n=10))