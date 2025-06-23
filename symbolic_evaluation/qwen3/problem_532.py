import mpmath as mp

# Set precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Calculate pi squared value using mpmath's constant
pi_value = mp.pi
result = pi_value ** 2

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))