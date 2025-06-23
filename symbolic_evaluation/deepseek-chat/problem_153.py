import mpmath as mp

# Set the precision to 15 decimal places for internal calculations
mp.dps = 15

# Define the expression using intermediate variables for clarity
# The analytical solution is expressed in terms of zeta and pi
zeta_3 = mp.zeta(3)  # Compute Riemann zeta function at 3
pi = mp.pi  # Pi constant

# Calculate the result: (π * ζ(3)) / 8
result = (pi * zeta_3) / 8

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))