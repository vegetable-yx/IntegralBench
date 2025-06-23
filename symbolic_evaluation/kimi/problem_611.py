import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate components of the expression step by step
sqrt3 = mp.sqrt(3)  # Compute square root of 3
numerator = 2 + sqrt3  # Calculate numerator (2 + √3)
denominator = sqrt3  # Denominator is √3
ratio = numerator / denominator  # Compute (2 + √3)/√3
result = mp.log(ratio)  # Calculate natural logarithm of the ratio

print(mp.nstr(result, n=10))  # Print result with 10 decimal places precision