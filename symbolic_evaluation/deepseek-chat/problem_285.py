import mpmath as mp

# Set the precision to 15 decimal places for internal calculations
mp.dps = 15

# Define the analytical expression step by step
# Intermediate calculations for the definite integral result
term1 = mp.pi * (mp.pi - 4 * mp.sqrt(2))
term2 = 8 * (mp.pi * mp.log(2) + 2 * mp.sqrt(2) - 4)
result = (term1 + term2) / 128

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))