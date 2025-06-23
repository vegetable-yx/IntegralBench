import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the modified Bessel function of the first kind of order 1 at 5
I1 = mp.besseli(1, 5)

# Calculate the numerator: 125 * pi * I1(5)
numerator = 125 * mp.pi * I1

# Divide by 16 to get the final result
result = numerator / 16

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))