import mpmath as mp

# Set precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Calculate the constant denominator
denominator = 2019

# Compute the value of pi divided by 2019
pi_over_2019 = mp.pi / denominator

# Calculate the square root of (pi/2019)
result = mp.sqrt(pi_over_2019)

# Print the final result with 10 decimal places
print(mp.nstr(result, n=10))