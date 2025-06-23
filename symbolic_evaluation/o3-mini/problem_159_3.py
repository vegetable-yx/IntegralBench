import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define parameters (example values - user can modify these)
a = mp.mpf(1.0)  # Upper limit of integration
b = mp.mpf(1.0)  # Parameter in the integrand

# Compute common argument for the hypergeometric functions
z = (b**4 * a) / 64

# Calculate first hypergeometric function: {}_0F_1(; 3/4; z)
hyp1 = mp.hyper([], [mp.mpf(3)/4], z)

# Calculate second hypergeometric function: {}_0F_1(; 5/4; z)
hyp2 = mp.hyper([], [mp.mpf(5)/4], z)

# Compute first term: (2/3) * hyp1
term1 = (mp.mpf(2)/3) * hyp1

# Compute second term: (b^2 * a / 8) * hyp2
term2 = (b**2 * a / 8) * hyp2

# Sum the terms inside the brackets
bracket_sum = term1 + term2

# Multiply by a^{3/2} for final result
result = a**(mp.mpf(3)/2) * bracket_sum

# Print result to 10 decimal places
print(mp.nstr(result, n=10))