import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# The analytical solution is π²/16
pi_val = mp.pi           # Get the value of π
pi_sq = pi_val ** 2      # Square π to get π²
result = pi_sq / 16      # Divide π² by 16 to get the result

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))