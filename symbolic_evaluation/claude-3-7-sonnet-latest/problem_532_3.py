import mpmath as mp

# Set internal precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Calculate the square of the mathematical constant π
result = mp.pi ** 2

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))