import mpmath as mp
mp.dps = 15

# Calculate pi/4 using mpmath's constant for pi
pi_value = mp.pi
result = pi_value / 4

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))