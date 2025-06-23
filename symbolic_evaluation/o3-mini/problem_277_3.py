import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# User must define the input parameters a and b here
a = 1.0  # Replace with actual value of a
b = 1.0  # Replace with actual value of b

# Calculate the argument for Bessel functions: ab/2
arg = a * b / 2

# Compute modified Bessel functions of first kind
# I0: order 0 Bessel function
I0 = mp.besseli(0, arg)
# I2: order 2 Bessel function
I2 = mp.besseli(2, arg)

# Compute the difference: I0(arg) - I2(arg)
bessel_diff = I0 - I2

# Calculate the constant factor: πa²/8
constant_factor = mp.pi * a**2 / 8

# Multiply constant factor by Bessel difference to get final result
result = constant_factor * bessel_diff

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))