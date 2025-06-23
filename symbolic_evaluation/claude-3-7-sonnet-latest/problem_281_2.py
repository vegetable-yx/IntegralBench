import mpmath as mp

# Set internal decimal precision to 15 for accurate computation
mp.dps = 15

# Calculate 2 * π using mpmath constants
two = mp.mpf(2)  # Represent 2 as an mpmath floating-point number
pi_value = mp.pi  # Use mpmath's built-in constant for π
result = two * pi_value  # Multiply to get 2π

# Print the result formatted to exactly 10 decimal places
print(mp.nstr(result, n=10))