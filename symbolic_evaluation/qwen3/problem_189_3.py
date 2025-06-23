import mpmath as mp
mp.dps = 15

# Calculate the square root of 5
sqrt5 = mp.sqrt(5)

# Compute the golden ratio (1 + sqrt(5))/2
phi = (1 + sqrt5) / 2

# Calculate natural logarithm of the golden ratio
log_phi = mp.log(phi)

# Multiply by π/2 to get final result
result = (mp.pi / 2) * log_phi

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))