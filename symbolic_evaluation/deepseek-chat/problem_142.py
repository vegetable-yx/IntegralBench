import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define the parameter 'a' (user can modify this value as needed)
a = 1.0

# Compute the modified Bessel function of the first kind of order 0
bessel_term = mp.besseli(0, a)

# Subtract 1 from the Bessel function result
bessel_minus_one = bessel_term - 1

# Multiply by pi: pi * (I_0(a) - 1)
numerator = mp.pi * bessel_minus_one

# Compute the denominator: 2 * a
denominator = 2 * a

# Final result: [pi * (I_0(a) - 1)] / (2 * a)
result = numerator / denominator

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))