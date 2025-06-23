import mpmath as mp
mp.dps = 15

# Calculate 7 factorial using mpmath
result = mp.factorial(7)

# Print result with 10 decimal places
print(mp.nstr(result, n=10))