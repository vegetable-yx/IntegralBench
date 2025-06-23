import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Analytical solution: π/2 - 1
pi_val = mp.pi           # Get precise value of π
half_pi = pi_val / 2     # Compute π/2
result = half_pi - 1     # Final result is π/2 - 1

# Output the result to exactly 10 decimal places
print(mp.nstr(result, n=10))