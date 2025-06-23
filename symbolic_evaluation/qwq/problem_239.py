import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate e^-2 using mpmath's exponential function
exp_minus2 = mp.exp(-2)

# Compute the final result: 1 - e^-2
result = 1 - exp_minus2

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))