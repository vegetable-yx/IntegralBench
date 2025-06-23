import mpmath as mp

# Set internal decimal places for precision
mp.dps = 15

# Define the variables a and b (using example values; replace with actual values)
a = 1.0
b = 1.0

# Calculate the argument for the Bessel function
arg = (a * b) / 4

# Compute the modified Bessel function of the first kind, order 0
bessel_value = mp.besseli(0, arg)

# Multiply by pi to get the final result
result = mp.pi * bessel_value

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))