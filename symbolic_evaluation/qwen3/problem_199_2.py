import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate square root of 2
sqrt2 = mp.sqrt(2)

# Get mathematical constant pi
pi_val = mp.pi

# Compute Struve H function of order 0 at 1
struve_h0_1 = mp.struveh(0, 1)

# Combine components to get final result
result = sqrt2 * pi_val * struve_h0_1

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))