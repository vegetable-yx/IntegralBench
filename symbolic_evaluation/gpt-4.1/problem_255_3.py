import mpmath as mp

# Set internal decimal precision to 15 for calculations
mp.dps = 15

# Calculate the constant pi
pi_value = mp.pi

# Multiply pi by 11
eleven_pi = 11 * pi_value

# Divide by 2
eleven_pi_over_two = eleven_pi / 2

# Apply the negative sign
result = -eleven_pi_over_two

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))