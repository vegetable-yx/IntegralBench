import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define the value of 'a' (example value, can be changed)
a = 1.0

# Compute argument for the hypergeometric functions
arg = -a**2 / 4

# Calculate J0(a) - Bessel function of the first kind of order 0
j0 = mp.besselj(0, a)

# Calculate J1(a) - Bessel function of the first kind of order 1
j1 = mp.besselj(1, a)

# Compute the first hypergeometric function: _1F_2(1/2; 1/2, 1; -a^2/4)
hyp1 = mp.hyper([0.5], [0.5, 1], arg)

# Compute the second hypergeometric function: _1F_2(1; 1, 3/2; -a^2/4)
hyp2 = mp.hyper([1], [1, 1.5], arg)

# Calculate the first term: J0(a) * hyp1
term1 = j0 * hyp1

# Calculate the second term: a * J1(a) * hyp2
term2 = a * j1 * hyp2

# Combine terms: (term1 - term2)
combined = term1 - term2

# Multiply by pi/4 to get the final result
result = (mp.pi / 4) * combined

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))