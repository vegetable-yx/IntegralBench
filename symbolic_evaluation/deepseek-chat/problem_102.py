import mpmath as mp

# Set internal precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Compute π using mpmath's constant
pi_val = mp.pi

# Square π
pi_squared = pi_val ** 2

# Divide by 72
result = pi_squared / 72

# Print the result rounded to 10 decimal places
print(mp.nstr(result, n=10))