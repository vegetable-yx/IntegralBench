import mpmath as mp

# Set the internal decimal precision to 15 for intermediate calculations
mp.dps = 15

# Compute the value of π
pi_value = mp.pi

# Compute the denominator (2)
denominator = mp.mpf(2)

# Compute the fraction π/2
fraction = pi_value / denominator

# Take the square root of the fraction
result = mp.sqrt(fraction)

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))