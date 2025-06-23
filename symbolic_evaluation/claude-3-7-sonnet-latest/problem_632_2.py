import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the fraction 3/4 using mpmath for high precision
numerator = mp.mpf(3)
denominator = mp.mpf(4)
fraction = numerator / denominator

# Compute the natural logarithm of the fraction
result = mp.log(fraction)

# Print the result rounded to 10 decimal places
print(mp.nstr(result, n=10))