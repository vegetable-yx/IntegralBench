import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate Euler's number e using mpmath constant
result = mp.e

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))