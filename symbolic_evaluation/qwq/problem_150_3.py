import mpmath as mp
mp.dps = 15

# Compute the complete elliptic integral of the first kind K(1/sqrt(2))
k_value = 1 / mp.sqrt(2)  # Calculate modulus parameter
elliptic_integral = mp.ellipk(k_value**2)  # Compute K(k^2) using mpmath's ellipk

# Multiply by π to get the final result
result = mp.pi * elliptic_integral

print(mp.nstr(result, n=10))