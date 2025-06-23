import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define the value of 'a' (example value, can be changed)
a = 1.0

# Compute the modified Struve function of order 1 at a
struve_L1 = mp.struvel(1, a)

# Multiply by pi/2 to get the final result
result = (mp.pi / 2) * struve_L1

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))