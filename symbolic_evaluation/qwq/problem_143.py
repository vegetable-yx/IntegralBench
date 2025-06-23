import mpmath as mp
# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Define numerator and denominator using exact values
numerator = mp.mpf(9)
denominator = mp.mpf(16)

# Perform exact division using mpmath
result = numerator / denominator

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))