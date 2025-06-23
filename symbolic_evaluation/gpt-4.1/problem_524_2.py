import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute e^2 using mpmath's exponential function
e_squared = mp.exp(2)

# Add 1 to e^2
sum_val = e_squared + 1

# Multiply the sum by 1/4 (equivalent to dividing by 4)
result = sum_val / 4

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))