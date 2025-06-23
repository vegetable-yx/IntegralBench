import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate the numerical value of 3π
three_pi = mp.mpf(3) * mp.pi

# Divide by 16 to get the final result
result = three_pi / mp.mpf(16)

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))