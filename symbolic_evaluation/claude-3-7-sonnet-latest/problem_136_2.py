import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the constant: 3 * π
three_pi = 3 * mp.pi

# Divide by 2 to get the final result: (3π)/2
result = three_pi / 2

# Print the result formatted to 10 decimal places
print(mp.nstr(result, n=10))