import mpmath as mp

# Set internal decimal precision to 15 for intermediate calculations
mp.dps = 15

# Calculate pi raised to the power of 3/2 (which is pi^(1.5))
pi_power = mp.power(mp.pi, mp.mpf(3)/2)

# Divide the result by 8 to obtain the final value
result = pi_power / 8

# Print the result rounded to 10 decimal places
print(mp.nstr(result, n=10))