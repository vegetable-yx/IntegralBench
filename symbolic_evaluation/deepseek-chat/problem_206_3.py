import mpmath as mp

# Set internal decimal places for computation
mp.dps = 15

# Calculate the square root of pi
sqrt_pi = mp.sqrt(mp.pi)

# Calculate the arctangent of 1/2
atan_val = mp.atan(0.5)

# Combine the components: (sqrt(pi)/2) * arctan(1/2)
result = (sqrt_pi / 2) * atan_val

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))