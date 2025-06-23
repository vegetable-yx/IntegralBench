import mpmath as mp
mp.dps = 15  # Set decimal places for internal calculations

# Calculate the negative value of pi using mpmath's constant
result = -mp.pi

# Print the result formatted to 10 decimal places
print(mp.nstr(result, n=10))