import mpmath as mp

# Set internal decimal places for high precision calculation
mp.dps = 15

# Define the value of the parameter 'a' (here set to 1, can be adjusted)
a_val = mp.mpf(1)

# Compute z = a^2 / 4
z_val = a_val**2 / 4

# Calculate the first hypergeometric term: {}_{1}F_{2}(1; 3/2, 5/2; z_val)
hyp1 = mp.hyper([1], [mp.mpf('1.5'), mp.mpf('2.5')], z_val)
term1 = (mp.mpf(2)/3) * hyp1

# Calculate the second hypergeometric term: {}_{1}F_{2}(1; 5/2, 3; z_val)
hyp2 = mp.hyper([1], [mp.mpf('2.5'), mp.mpf(3)], z_val)
term2 = (a_val**2 / 6) * hyp2

# Combine the terms to get the final result
result = term1 - term2

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))