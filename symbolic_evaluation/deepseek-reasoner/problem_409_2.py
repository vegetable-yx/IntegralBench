import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate 2*π
term1 = mp.mpf(2) * mp.pi

# Calculate 3*ln(2)
term2 = mp.mpf(3) * mp.log(2)

# Sum the two terms
sum_terms = term1 + term2

# Divide by 5 to get final result
result = sum_terms / mp.mpf(5)

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))