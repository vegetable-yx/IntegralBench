import mpmath as mp

# Set precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Calculate e^4 using mpmath's exponential function
exp_4 = mp.exp(4)

# Subtract 1 from the computed exponential value
result = exp_4 - 1

# Print the final result with exactly 10 decimal places
print(mp.nstr(result, n=10))