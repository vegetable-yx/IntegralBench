import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate Bessel function of the first kind J_3(2.0)
result = mp.besselj(3.0, 2.0)

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))