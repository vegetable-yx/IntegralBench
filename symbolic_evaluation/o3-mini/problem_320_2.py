import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define the value of 'a'. Change this value as needed for different evaluations.
a_val = mp.mpf(1.0)

# Compute the common argument for hypergeometric functions
z = -a_val**2 / 4

# Calculate gamma function values
gamma_14 = mp.gamma(mp.mpf(1)/4)
gamma_34 = mp.gamma(mp.mpf(3)/4)

# Compute the first hypergeometric function: 1F2(1/4; 1/2, 3/4; -a^2/4)
hyp1 = mp.hyper([mp.mpf(1)/4], [mp.mpf(1)/2, mp.mpf(3)/4], z)

# Compute the second hypergeometric function: 1F2(3/4; 5/4, 3/2; -a^2/4)
hyp2 = mp.hyper([mp.mpf(3)/4], [mp.mpf(5)/4, mp.mpf(3)/2], z)

# Calculate the first term: Gamma(1/4)^2 * hyp1
term1 = gamma_14**2 * hyp1

# Calculate the second term: a * Gamma(3/4)^2 * hyp2
term2 = a_val * gamma_34**2 * hyp2

# Compute the expression inside the brackets
bracket_term = term1 - term2

# Calculate the numerator: sqrt(pi) * bracket_term
numerator = mp.sqrt(mp.pi) * bracket_term

# Final result: numerator divided by (2a)
result = numerator / (2 * a_val)

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))