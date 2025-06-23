import mpmath as mp
mp.dps = 15  # Set internal precision

numerator = mp.mpf(80)  # Define numerator
denominator = mp.mpf(23)  # Define denominator
ratio = numerator / denominator  # Compute 80/23
result = mp.log(ratio)  # Calculate natural logarithm

print(mp.nstr(result, n=10))