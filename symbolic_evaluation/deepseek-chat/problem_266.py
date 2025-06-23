import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Define the value of 'a' (user can adjust as needed)
a = mp.mpf(1.0)

# Compute the first part: π/2 * (1 - J0(a))
first_part = (mp.pi / 2) * (1 - mp.besselj(0, a))

# Initialize the outer sum
outer_sum = mp.mpf(0)
# Tolerance for breaking the summation
tol = mp.mpf('1e-20')
# Maximum number of terms to avoid infinite loops
max_n = 1000
# Variable to store previous integral value for recurrence
prev_integral = None

# Loop over n from 0 to max_n-1
for n in range(max_n):
    # Compute the integral for current n using recurrence
    if n == 0:
        # Base case: integral for n=0
        integral_val = 1 - mp.besselj(0, a)
    else:
        # Recurrence relation for integral: 
        # I_n = -a^{2n}*J0(a) + 2n*a^{2n-1}*J1(a) - 2n*(2n-1)*I_{n-1}
        term1 = -(a ** (2 * n)) * mp.besselj(0, a)
        term2 = 2 * n * (a ** (2 * n - 1)) * mp.besselj(1, a)
        term3 = -2 * n * (2 * n - 1) * prev_integral
        integral_val = term1 + term2 + term3
    
    # Compute the coefficient: (2n)! / [4^n * (n!)^2 * (2n+1)]
    numerator = mp.fac(2 * n)
    denominator = (4 ** n) * (mp.fac(n) ** 2) * (2 * n + 1)
    coeff = numerator / denominator
    
    # Compute the factor: 1 / a^{2n+1}
    a_factor = 1 / (a ** (2 * n + 1))
    
    # Compute the term for current n
    term = coeff * a_factor * integral_val
    outer_sum += term
    
    # Store current integral for next recurrence step
    prev_integral = integral_val
    
    # Break if term is below tolerance
    if mp.fabs(term) < tol:
        break

# Combine the results
result = first_part - outer_sum

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))