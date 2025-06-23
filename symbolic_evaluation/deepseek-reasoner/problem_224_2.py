import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate Euler's number e
e_value = mp.e

# Calculate the constant term 5/2
constant_term = mp.mpf(5)/2

# Compute the difference (e - 5/2)
difference = e_value - constant_term

# Multiply by pi
pi_times_diff = mp.pi * difference

# Divide by 8 to get final result
result = pi_times_diff / 8

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))