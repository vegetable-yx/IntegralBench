import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define the value of a (example value, can be changed as needed)
a = mp.mpf('1.0')

# Compute z = a^2 / 4 for the hypergeometric function arguments
z = a**2 / 4

# Compute the first hypergeometric function: {}_1F_2(1/2; 3/2, 2; z)
hyp1 = mp.hyper([mp.mpf('0.5')], [mp.mpf('1.5'), mp.mpf('2')], z)

# Compute the first term: (a/2) * hyp1
term1 = (a / 2) * hyp1

# Compute the second hypergeometric function: {}_1F_2(1; 3/2, 5/2; z)
hyp2 = mp.hyper([mp.mpf('1')], [mp.mpf('1.5'), mp.mpf('2.5')], z)

# Compute the second term: (a^2 / (2 * sqrt(pi))) * hyp2
term2 = (a**2 / (2 * mp.sqrt(mp.pi))) * hyp2

# Combine terms to get the final result
result = term1 - term2

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))