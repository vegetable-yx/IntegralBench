import mpmath as mp

# Set decimal places for internal calculations
mp.dps = 15

# Define the parameters a and b (replace with desired values)
a = mp.mpf('1.0')
b = mp.mpf('1.0')

# Compute the argument for the Bessel functions: (b * a) / 2
arg = b * a / 2

# Compute the modified Bessel functions I1 and I2
I1 = mp.besseli(1, arg)   # Modified Bessel function of first kind, order 1
I2 = mp.besseli(2, arg)   # Modified Bessel function of first kind, order 2

# Compute the expression inside the brackets: I1 - (1/2)*I2
bracket_expr = I1 - 0.5 * I2

# Compute the constant factor: π * a^{3/2} / 4
factor = (mp.pi * (a ** 1.5)) / 4

# Multiply the factor by the bracket expression to get final result
result = factor * bracket_expr

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))