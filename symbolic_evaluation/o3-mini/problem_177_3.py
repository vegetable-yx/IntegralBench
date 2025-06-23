import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define the parameter 'a' (example value, can be changed)
a = 1.0

# Compute the argument for the hypergeometric function: z = -a^2/4
z = -a**2 / 4

# Calculate the hypergeometric function: _2F_1(1/2, 1/2; 3/2; z)
hyper_val = mp.hyp2f1(0.5, 0.5, 1.5, z)

# Compute the bracket term: 1 - hypergeometric value
bracket_term = 1 - hyper_val

# Calculate the prefactor: pi/(2a)
prefactor = mp.pi / (2 * a)

# Compute the final result
result = prefactor * bracket_term

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))