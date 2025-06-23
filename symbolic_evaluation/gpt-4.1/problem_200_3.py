import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the constant factor: sqrt(2)/2
constant_factor = mp.sqrt(2) / 2

# Calculate the Beta function with parameters a=5/4 and b=1/4
beta_value = mp.beta(5/4, 1/4)

# Compute the final result by multiplying the constant factor with the Beta value
result = constant_factor * beta_value

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))