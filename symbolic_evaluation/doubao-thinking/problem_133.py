import mpmath as mp
mp.dps = 15

# Calculate pi/2 using mpmath's constant
result = mp.pi / 2

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))