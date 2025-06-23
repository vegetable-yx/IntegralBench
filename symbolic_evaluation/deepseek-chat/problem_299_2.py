import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the value of pi using mpmath constant
pi_value = mp.pi

# Divide pi by 2 to get pi/2
half_pi = pi_value / 2

# Apply the negative sign to obtain -pi/2
result = -half_pi

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))