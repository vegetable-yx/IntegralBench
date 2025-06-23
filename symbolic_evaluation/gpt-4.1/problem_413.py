import mpmath as mp

# Set internal decimal precision to 15 for intermediate calculations
mp.dps = 15

# Calculate the analytical expression: 506 * π
constant = mp.mpf(506)  # Convert integer to mpmath float
pi_value = mp.pi        # mpmath's π constant
result = constant * pi_value

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))