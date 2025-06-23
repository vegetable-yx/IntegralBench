import mpmath as mp
mp.dps = 15

# Calculate sin(1) using mpmath's sine function
angle = mp.mpf(1)
result = mp.sin(angle)

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))