import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define the value of parameter 'a' (modify as needed)
a = mp.mpf(1)

# Precompute common argument for hypergeometric functions
z = a**2 / 4

# Compute the first hypergeometric term: _1F_2(1; 3/2, 2; z)
hyp1 = mp.hyper([1], [mp.mpf(3)/2, 2], z)

# Compute the first part: (a/2) * hyp1
term1 = (a / 2) * hyp1

# Compute the second hypergeometric term: _1F_2(2; 5/2, 3; z)
hyp2 = mp.hyper([2], [mp.mpf(5)/2, 3], z)

# Compute the second part: (a^3/8) * hyp2
term2 = (a**3 / 8) * hyp2

# Combine results: term1 - term2
result = term1 - term2

# Print final result to 10 decimal places
print(mp.nstr(result, n=10))