import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate J_0(1) using Bessel function of the first kind
j0_1 = mp.besselj(0, 1)

# Multiply by pi to get the final result
result = mp.pi * j0_1

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))