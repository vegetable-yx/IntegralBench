import mpmath as mp

# Set internal decimal places for precision
mp.dps = 15

# Calculate the value of 1/64 using exact rational arithmetic
numerator = mp.mpf(1)
denominator = mp.mpf(64)
result = numerator / denominator

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))