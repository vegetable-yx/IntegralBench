import mpmath as mp

# Set decimal places for internal calculations
mp.dps = 15

# Get the value of pi
pi_val = mp.pi

# Calculate pi squared
pi_squared = pi_val ** 2

# Calculate pi to the fourth power (by squaring pi_squared)
pi_fourth = pi_squared ** 2

# Divide pi_fourth by 64 to get the result
result = pi_fourth / 64

# Output the result with 10 decimal places
print(mp.nstr(result, n=10))