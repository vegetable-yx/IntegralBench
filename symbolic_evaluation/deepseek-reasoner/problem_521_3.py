import mpmath as mp
mp.dps = 15

# Calculate natural logarithm of 3 using mpmath
result = mp.log(3)

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))