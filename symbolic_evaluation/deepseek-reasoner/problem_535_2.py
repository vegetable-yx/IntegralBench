import mpmath as mp

# Set precision to 15 decimal places for calculations
mp.dps = 15

# Calculate e^3 using mpmath exponential function
e_cubed = mp.exp(3)

# Divide the result by 3 to get the final value
result = e_cubed / 3

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))