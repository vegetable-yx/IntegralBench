import mpmath as mp

# Set internal precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Calculate pi to the fourth power
pi_sq = mp.pi ** 2  # pi squared
pi_fourth = pi_sq ** 2  # pi^4 by squaring pi^2

# Divide by 120 to get the final result
result = pi_fourth / 120

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))