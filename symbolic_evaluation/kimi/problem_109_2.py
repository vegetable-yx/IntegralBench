import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate the complete elliptic integral of the second kind E(1/2)
m = mp.mpf(1)/2  # Define the modulus parameter
E_value = mp.ellipe(m)  # Compute E(1/2) using mpmath's ellipe function

# Multiply by 8/3 as per the analytical expression
result = (mp.mpf(8)/3) * E_value

# Print the final result with exactly 10 decimal places
print(mp.nstr(result, n=10))