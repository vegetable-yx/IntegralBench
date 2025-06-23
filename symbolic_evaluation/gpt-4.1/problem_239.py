import mpmath as mp

# Set internal decimal places for high precision
mp.dps = 15

# Define the argument for the Bessel function
a = 1.0  # Example value; can be adjusted as needed

# Compute the modified Bessel function of the second kind of order 0
result = mp.besselk(0, a)

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))