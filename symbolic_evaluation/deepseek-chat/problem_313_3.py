import mpmath as mp

# Set internal decimal places for precision
mp.dps = 15

# Calculate pi/2 using mpmath's constant for pi
pi_value = mp.pi
result = pi_value / 2

# Output the result with exactly 10 decimal places
print(mp.nstr(result, n=10))