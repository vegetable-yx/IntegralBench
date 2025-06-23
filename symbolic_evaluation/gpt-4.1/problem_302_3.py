import mpmath as mp

# Set internal decimal precision to 15 for accurate computations
mp.dps = 15

# Calculate the first term: (π/2) * arcsin(1/4)
arcsin_val = mp.asin(1/4)          # Compute arcsin(1/4)
term1 = (mp.pi / 2) * arcsin_val   # Multiply by π/2

# Calculate the second term: (1/8) * K(1/4) where K is the complete elliptic integral of the first kind
k_val = mp.ellipk(1/4)             # Compute K(1/4)
term2 = (1/8) * k_val              # Multiply by 1/8

# Sum the two terms to get the final result
result = term1 + term2

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))