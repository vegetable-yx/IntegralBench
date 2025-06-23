import mpmath as mp

# Set precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Calculate e squared
e_squared = mp.exp(2)

# Compute numerator (e² - 1)
numerator = e_squared - 1

# Calculate final result by dividing by 4
result = numerator / 4

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))