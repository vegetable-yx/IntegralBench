import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate 4 times pi using exact symbolic relationship
four = mp.mpf(4)
result = four * mp.pi

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))