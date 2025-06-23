import mpmath as mp

# Set internal precision to 15 decimal places for accuracy
mp.dps = 15

# Compute the argument for the elliptic integral: 1/sqrt(2)
arg = 1 / mp.sqrt(2)

# Evaluate the complete elliptic integral of the second kind E(k) at k = 1/sqrt(2)
E_value = mp.ellipe(arg)

# Compute the constant factor pi/2
pi_half = mp.pi / 2

# Calculate the final result: (pi/2) * E(1/sqrt(2))
result = pi_half * E_value

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))