import mpmath as mp

# Set internal decimal precision to 15 for accurate calculations
mp.dps = 15

# Define the input parameter 'a'. Change this value as needed.
a = 1.0

# Calculate Bessel function of the first kind of order 0 at point a
j0 = mp.besselj(0, a)

# Calculate modified Struve function of order 0 at point a
l0 = mp.struvel(0, a)

# Compute the difference: J0(a) - L0(a)
diff = j0 - l0

# Multiply by pi/2 to get the final result
result = (mp.pi / 2) * diff

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))