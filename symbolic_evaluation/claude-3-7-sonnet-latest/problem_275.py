import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define input parameters (example values, can be changed)
a = 1.0
b = 1.0

# Convert to mpmath floats for consistent precision
a_mp = mp.mpf(a)
b_mp = mp.mpf(b)

# Compute argument for Bessel functions: (a*b)/2
arg = (a_mp * b_mp) / 2

# Compute modified Bessel functions of the first kind
I0 = mp.besseli(0, arg)  # I_0 function at arg
I1 = mp.besseli(1, arg)  # I_1 function at arg

# Compute difference: I0(arg) - I1(arg)
bessel_diff = I0 - I1

# Compute a^{3/2}
a_power = a_mp**(mp.mpf(3)/2)

# Compute prefactor: π * a^{3/2} / 4
prefactor = (mp.pi * a_power) / 4

# Compute final result
result = prefactor * bessel_diff

# Print result to 10 decimal places
print(mp.nstr(result, n=10))