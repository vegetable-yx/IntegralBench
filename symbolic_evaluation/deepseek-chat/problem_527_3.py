import mpmath as mp

# Set the precision to 15 decimal places for internal calculations
mp.dps = 15

# The analytical solution for the integral is 0 due to symmetry:
# The function cos(x + cos(x)) is antisymmetric about x = pi/2.
# Specifically, f(pi - x) = cos(pi - x + cos(pi - x)) = cos(pi - x - cos(x)) 
# = -cos(x + cos(x)) = -f(x). Thus, the integral from 0 to pi is zero.

# Define the result as 0
result = mp.mpf(0)

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))