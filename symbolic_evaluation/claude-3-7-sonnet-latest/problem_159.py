import mpmath as mp

# Set internal decimal precision to 15 for accurate calculations
mp.dps = 15

# Define input parameters (example values; user should modify these as needed)
a = 1.0
b = 1.0

# Calculate a^{1/2} (square root of a)
sqrt_a = mp.sqrt(a)

# Calculate the argument for the Bessel function: b * a^{1/2}
arg = b * sqrt_a

# Compute the modified Bessel function of the first kind of order 1
bessel_term = mp.besseli(1, arg)

# Calculate a^{3/2}
a_power_3_2 = a**1.5

# Compute the coefficient: a^{3/2} / b
coefficient = a_power_3_2 / b

# Multiply coefficient by the Bessel function to get final result
result = coefficient * bessel_term

# Print the result rounded to 10 decimal places
print(mp.nstr(result, n=10))