import mpmath as mp

# Set precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Define the argument for the arcsin function: 1/3
arg = mp.mpf('1') / mp.mpf('3')

# Compute the result using the analytical expression: arcsin(1/3)
result = mp.asin(arg)

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))