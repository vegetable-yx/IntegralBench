import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate pi divided by 2019
fraction = mp.pi / 2019

# Take the square root of the fraction
result = mp.sqrt(fraction)

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))