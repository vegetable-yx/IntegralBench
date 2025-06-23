import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Direct calculation of the simple closed-form solution
numerator = mp.mpf(1)
denominator = mp.mpf(2)
result = numerator / denominator

# Output the result with exactly 10 decimal places
print(mp.nstr(result, n=10))