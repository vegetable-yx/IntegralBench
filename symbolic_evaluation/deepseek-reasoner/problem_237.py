import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate 3 times pi using exact symbolic representation
three = mp.mpf(3)
pi_value = mp.pi

# Multiply to get final result
result = three * pi_value

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))