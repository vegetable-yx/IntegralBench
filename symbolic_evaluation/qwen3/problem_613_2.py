import mpmath as mp
mp.dps = 15  # Set decimal places for internal calculations

# Define numerator and denominator using mpmath types
numerator = mp.mpf(1)
denominator = mp.mpf(5)

# Compute the result of 1 divided by 5
result = numerator / denominator

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))