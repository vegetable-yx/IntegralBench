import mpmath as mp

# Set decimal places for internal calculations
mp.dps = 15

# Define parameters (example values - user should modify as needed)
a = 1.0
b = 1.0

# Calculate the argument for the Bessel functions
arg = b * a / 2

# Compute modified Bessel functions of the first kind
I0 = mp.besseli(0, arg)  # I0 at the computed argument
I2 = mp.besseli(2, arg)  # I2 at the computed argument

# Sum the Bessel function results
I_sum = I0 + I2

# Calculate the constant factor (pi * a^2 / 8)
factor = (mp.pi * a**2) / 8

# Compute the final result
result = factor * I_sum

# Print result to 10 decimal places
print(mp.nstr(result, n=10))