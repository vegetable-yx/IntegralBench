import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Precompute constants
two_power_neg11half = mp.power(2, -11/2)
two_power_neg7half = mp.power(2, -7/2)

# Compute digamma terms
digamma_3 = mp.digamma(3)
digamma_3half = mp.digamma(3/2)
digamma_diff = digamma_3 - digamma_3half

# Compute trigamma terms
trigamma_3 = mp.polygamma(1, 3)
trigamma_3half = mp.polygamma(1, 3/2)
trigamma_diff = trigamma_3half - trigamma_3  # Note: expression has -ψ₁(3) + ψ₁(3/2)

# Combine digamma and trigamma parts
inner_term = digamma_diff**2 + trigamma_diff

# Compute hypergeometric function _2F_1(7/2, 3/2; 3; 1/2)
hyp_val = mp.hyp2f1(7/2, 3/2, 3, 1/2)

# First part of the expression
part1 = two_power_neg11half * mp.pi * inner_term * hyp_val

# Compute derivative of _2F_1(7/2, a; 3; 1/2) w.r.t. a at a=3/2
def hyp_func(a):
    return mp.hyp2f1(7/2, a, 3, 1/2)

derivative = mp.diff(hyp_func, 3/2)

# Precompute gamma terms for the second part
gamma_3half = mp.gamma(3/2)
gamma_3 = mp.gamma(3)  # Γ(3) = 2

# Second part of the expression
gamma_term = (gamma_3half**2) / gamma_3
part2 = two_power_neg7half * gamma_term * derivative

# Combine both parts
result = part1 + part2

# Print result with 10 decimal places
print(mp.nstr(result, n=10))