import mpmath as mp

# Set precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Calculate 2^(1/4) using mpmath power function
denominator = mp.power(2, 0.25)

# Compute π divided by 2^(1/4)
result = mp.pi / denominator

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))