import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate k = 1/sqrt(2) = sqrt(2)/2, the argument for elliptic integral
k = mp.sqrt(2) / 2

# Compute the complete elliptic integral of the second kind E(k)
E_k = mp.ellipe(k)

# First term: 2 * E(k)
term1 = 2 * E_k

# Compute the multiplicative factor for the second term: sqrt(2)/2 (which equals k)
# Compute the expression inside parentheses: (1 + pi/2)
parentheses_term = 1 + mp.pi / 2

# Second term: (sqrt(2)/2) * (1 + pi/2) = k * parentheses_term
term2 = k * parentheses_term

# Sum the two terms for final result
result = term1 + term2

# Print result rounded to 10 decimal places
print(mp.nstr(result, n=10))