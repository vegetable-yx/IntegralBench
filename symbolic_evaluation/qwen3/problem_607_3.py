import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate sqrt(2)
sqrt_2 = mp.sqrt(2)

# Calculate ln(1 + sqrt(2))
log_term = mp.log(1 + sqrt_2)

# Calculate pi/2 multiplied by the logarithmic term
result = (mp.pi / 2) * log_term

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))