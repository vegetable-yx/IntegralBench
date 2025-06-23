import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the Bessel function of the first kind of order 3 at 2
result = mp.besselj(3, 2)

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))