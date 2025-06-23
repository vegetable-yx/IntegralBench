import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Compute Bessel function of the first kind J_1 at 1
j1_value = mp.besselj(1, 1)

# Compute square root of 2
sqrt2 = mp.sqrt(2)

# Calculate the final result using exact formula components
result = mp.pi * j1_value / sqrt2

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))