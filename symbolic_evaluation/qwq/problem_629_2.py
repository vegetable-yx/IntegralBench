import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

numerator = 253
denominator = 3
fraction = mp.mpf(numerator) / mp.mpf(denominator)  # Compute 253/3 with mpmath precision

result = mp.log(fraction)  # Calculate natural logarithm of the fraction

print(mp.nstr(result, n=10))  # Print result formatted to 10 decimal places