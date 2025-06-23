import mpmath as mp
mp.dps = 15

# Calculate 506 multiplied by pi
coefficient = 506
result = coefficient * mp.pi

# Print result with 10 decimal places
print(mp.nstr(result, n=10))