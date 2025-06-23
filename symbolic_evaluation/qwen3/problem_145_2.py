import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the modified Bessel function of the first kind of order 0 at 2
I0 = mp.besseli(0, 2)

# Compute the modified Bessel function of the first kind of order 1 at 2
I1 = mp.besseli(1, 2)

# Calculate the difference: I0(2) - I1(2)
diff = I0 - I1

# Multiply by pi/2 to get the final result
result = (mp.pi / 2) * diff

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))