import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the modified Bessel function of the first kind of order 0 at 6
I0 = mp.besseli(0, 6)

# Compute the modified Bessel function of the first kind of order 1 at 6
I1 = mp.besseli(1, 6)

# Calculate the difference between the Bessel function values
diff = I0 - I1

# Multiply by pi/3 to get the final result
result = (mp.pi / 3) * diff

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))