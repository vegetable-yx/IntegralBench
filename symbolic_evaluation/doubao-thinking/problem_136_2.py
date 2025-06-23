import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate the complete elliptic integral of the second kind E(1/2)
E_half = mp.ellipe(0.5)

# Multiply the result by 2 as per the given expression
result = 2 * E_half

# Print the final value with 10 decimal places
print(mp.nstr(result, n=10))