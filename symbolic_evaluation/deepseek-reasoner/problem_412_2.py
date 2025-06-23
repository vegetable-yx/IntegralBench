import mpmath as mp
mp.dps = 15  # Set internal precision

# The analytical answer is Euler's number e
result = mp.e  # Directly use mpmath constant for e

# Print result with 10 decimal places
print(mp.nstr(result, n=10))