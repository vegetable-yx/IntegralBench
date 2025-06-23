import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the complete elliptic integral of the second kind E(1/2)
# Note: mpmath uses m = k^2, so for k=1/2 we have m = (1/2)^2 = 0.25
E_half = mp.ellipe(0.25)

# Compute the incomplete elliptic integral of the second kind E(φ|m)
# for φ = π/6 and m = 4. This corresponds to the integral term after substitution.
# The integral ∫₀¹ √(1-x²)/√(4-x²) dx = E(π/6, 4)
integral_term = mp.ellipe(mp.pi/6, 4)

# Combine all terms: -π + 2*E(1/2) + integral
result = -mp.pi + 2 * E_half + integral_term

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))