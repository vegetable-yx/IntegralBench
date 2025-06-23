import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate arcsin(1/4)
a = mp.asin(mp.mpf(1)/4)

# Compute term1: (π/4) * arcsin(1/4)
term1 = (mp.pi / 4) * a

# Compute term2: (1/4) * [arcsin(1/4)]^2
term2 = (mp.mpf(1)/4) * (a ** 2)

# Combine terms: term1 - term2
result = term1 - term2

# Print final result to 10 decimal places
print(mp.nstr(result, n=10))