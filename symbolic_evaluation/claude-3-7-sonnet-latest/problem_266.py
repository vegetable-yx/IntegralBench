import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Define the parameter 'a' (user should adjust this value as needed)
a = 1.0  # Example value; change to desired input

# Compute the Bessel function of the first kind of order 0 at 'a'
j0_val = mp.besselj(0, a)

# Calculate the numerator: 1 - J_0(a)
numerator = 1 - j0_val

# Compute the final result: (1 - J_0(a)) / a
result = numerator / a

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))