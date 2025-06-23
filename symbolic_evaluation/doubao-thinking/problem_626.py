import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the value of π (pi) using mpmath constant
pi_val = mp.pi

# Divide π by 2 to get π/2
pi_over_2 = pi_val / 2

# Compute the natural logarithm of π/2
result = mp.log(pi_over_2)

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))