import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate pi
pi_value = mp.pi

# Divide pi by 2019
fraction = pi_value / 2019

# Take the square root of the fraction
result = mp.sqrt(fraction)

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))