import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the numerator: 19 * π
numerator = mp.mpf(19) * mp.pi

# Divide the numerator by 512 to get the result
result = numerator / mp.mpf(512)

# Print the result formatted to 10 decimal places
print(mp.nstr(result, n=10))