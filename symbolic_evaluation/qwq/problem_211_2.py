import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

numerator = mp.mpf(3)  # Define numerator
denominator = mp.mpf(2)  # Define denominator
result = numerator / denominator  # Perform exact division

print(mp.nstr(result, n=10))