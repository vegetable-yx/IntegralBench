import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define the value of parameter 'a' (user can adjust this as needed)
a_val = 1.0

# Compute intermediate value: a^2 / 4
a_sq_over_4 = (a_val**2) / 4.0

# Calculate the first hypergeometric term: _1F_2(1/2; 3/2, 2; a^2/4)
hyp1 = mp.hyp1f2(0.5, 1.5, 2, a_sq_over_4)

# Calculate the second hypergeometric term: _1F_2(1; 3/2, 3/2; a^2/4)
hyp2 = mp.hyp1f2(1.0, 1.5, 1.5, a_sq_over_4)

# Compute the first part: (π/8) * hyp1
term1 = (mp.pi / 8) * hyp1

# Compute the second part: (a/8) * hyp2
term2 = (a_val / 8) * hyp2

# Combine the terms: term1 - term2
result = term1 - term2

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))