import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define the parameter a (example value, can be adjusted)
a = 1.0

# Calculate the square root of pi
sqrt_pi = mp.sqrt(mp.pi)

# Calculate the modified Bessel function of the first kind of order 1
bessel_i1 = mp.besseli(1, a)

# Compute the final result: sqrt(pi)/2 * I_1(a)
result = (sqrt_pi / 2) * bessel_i1

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))