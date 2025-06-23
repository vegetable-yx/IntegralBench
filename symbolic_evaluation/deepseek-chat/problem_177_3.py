import mpmath as mp

# Set internal decimal places for high precision
mp.dps = 15

# Calculate pi constant
pi_val = mp.pi

# Compute the sine integral Si(3)
sine_integral = mp.si(3)

# Multiply by pi/2
result = (pi_val / 2) * sine_integral

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))