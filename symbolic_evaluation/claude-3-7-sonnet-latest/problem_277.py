import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define the parameters a and b (using example values 1.0 and 1.0)
a = mp.mpf(1.0)
b = mp.mpf(1.0)

# Compute the argument for the Bessel function: (a * b) / 2
arg = (a * b) / 2

# Calculate the modified Bessel function of the first kind of order 1
bessel_term = mp.besseli(1, arg)

# Compute the constant factor: π * a² / 4
constant_factor = (mp.pi * a**2) / 4

# Multiply the constant factor by the Bessel function result
result = constant_factor * bessel_term

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))