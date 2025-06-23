import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate the complete elliptic integral of the second kind E(1/2)
m = mp.mpf(1)/2  # Define the parameter for the elliptic integral
result = mp.ellipe(m)  # Compute E(1/2) using mpmath's ellipe function

print(mp.nstr(result, n=10))  # Print result with 10 decimal places precision