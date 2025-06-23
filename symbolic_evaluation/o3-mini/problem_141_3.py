import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Example value for the parameter 'a'
# Replace this value with the desired input
a = mp.mpf(1)

# Compute intermediate variable z = a^2 / 4
z = a**2 / 4

# Calculate the hypergeometric function:
# {}_1F_{2}\left(1; \frac{3}{2}, 2; \frac{a^2}{4}\right)
result = mp.hyper([1], [mp.mpf(3)/2, 2], z)

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))