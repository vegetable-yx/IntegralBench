import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define the parameter 'a' (user can change this value as needed)
a = 1.0

# Compute common argument for hypergeometric functions: -a^2/16
z = -a**2 / 16.0

# Calculate the first generalized hypergeometric function: 
# {}_1F_2(1/2; 3/4, 5/4; -a^2/16)
hyper1 = mp.hyper([0.5], [0.75, 1.25], z)

# First term: (π/2) * {}_1F_2(...)
term1 = (mp.pi / 2) * hyper1

# Calculate the second generalized hypergeometric function:
# {}_1F_2(1; 5/4, 7/4; -a^2/16)
hyper2 = mp.hyper([1.0], [1.25, 1.75], z)

# Second term: (a * √π / 4) * {}_1F_2(...)
term2 = (a * mp.sqrt(mp.pi) / 4) * hyper2

# Combine terms to get final result
result = term1 - term2

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))