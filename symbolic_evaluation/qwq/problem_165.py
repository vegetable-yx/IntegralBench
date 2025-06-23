import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate modified Struve functions L0(2) and L1(2)
L0_2 = mp.struvel(0, 2)
L1_2 = mp.struvel(1, 2)

# Compute the difference between Struve functions
struve_diff = L0_2 - L1_2

# Multiply by π/2 to get final result
result = (mp.pi / 2) * struve_diff

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))