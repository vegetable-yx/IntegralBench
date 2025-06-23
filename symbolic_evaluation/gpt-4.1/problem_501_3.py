import mpmath as mp

# Set internal decimal places for high precision calculation
mp.dps = 15

# Calculate the fraction 2/5 using exact rational arithmetic
numerator = mp.mpf(2)
denominator = mp.mpf(5)
result = numerator / denominator

# Output the result to exactly 10 decimal places
print(mp.nstr(result, n=10))