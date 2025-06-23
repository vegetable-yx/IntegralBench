import mpmath as mp
mp.dps = 15

# Calculate Euler's number e using mpmath constant
result = mp.e

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))