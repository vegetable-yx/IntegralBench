import mpmath as mp
mp.dps = 15

# Calculate the exact value of -π/4 using high-precision constants
result = -mp.pi / 4

# Print the result with 10 decimal place precision
print(mp.nstr(result, n=10))