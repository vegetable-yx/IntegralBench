import mpmath as mp
mp.dps = 15

# Calculate Bessel function of the first kind J_3(2.0)
result = mp.besselj(3.0, 2.0)

# Print result with 10 decimal place precision
print(mp.nstr(result, n=10))