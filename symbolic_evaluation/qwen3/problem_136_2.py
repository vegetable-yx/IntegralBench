import mpmath as mp
mp.dps = 15

# Calculate the complete elliptic integral of the second kind E(1/2)
m = mp.mpf(1)/2  # Define the parameter for the elliptic integral
e_value = mp.ellipe(m)  # Compute E(1/2)

# Multiply by 2 to get the final result
result = 2 * e_value

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))