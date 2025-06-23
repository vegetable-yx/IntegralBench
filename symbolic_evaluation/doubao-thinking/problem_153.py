import mpmath as mp
mp.dps = 15

# Calculate the value of pi
pi_value = mp.pi

# Divide pi by 8 to get the result
result = pi_value / 8

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))