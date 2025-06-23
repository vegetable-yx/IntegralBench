import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Compute Bessel function J0 at 1
j0_1 = mp.besselj(0, 1)

# Compute Bessel function J1 at 1
j1_1 = mp.besselj(1, 1)

# Calculate the combination (J0(1) - 1/4 J1(1))
combined_term = j0_1 - (1/4) * j1_1

# Multiply by π to get the final result
result = mp.pi * combined_term

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))