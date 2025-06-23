import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define maximum terms for the series (k_max for outer, n_max for inner sum)
k_max = 200
n_max = 200

# Initialize sums for each part of the expression
part1 = mp.mpf(0)
part2 = mp.mpf(0)
part3 = mp.mpf(0)

# Precompute ln(2) for part3
ln2 = mp.ln(2)

# Main loop over k from 0 to k_max
for k in range(0, k_max + 1):
    # Parameters for beta and digamma functions: a1 = 3/2 + k, b1 = 3/2
    a1 = mp.mpf('1.5') + k
    b1 = mp.mpf('1.5')
    ab1 = a1 + b1  # a1 + b1 = 3 + k

    # Generalized binomial coefficient: binom(1/2, k)
    binom_k = mp.binomial(mp.mpf('0.5'), k)

    # Compute beta(a1, b1) and digamma values for part1 and part3
    beta_val1 = mp.beta(a1, b1)
    psi0_a1 = mp.psi(0, a1)
    psi0_b1 = mp.psi(0, b1)
    psi0_ab1 = mp.psi(0, ab1)
    psi1_ab1 = mp.psi(1, ab1)

    # Part1: Second mixed partial derivative of beta at (a1, b1)
    deriv_factor = (psi0_a1 - psi0_ab1) * (psi0_b1 - psi0_ab1) - psi1_ab1
    term1 = binom_k * beta_val1 * deriv_factor
    part1 += term1

    # Part3: Beta and digamma difference term
    term3 = binom_k * beta_val1 * (psi0_a1 - psi0_ab1)
    part3 += term3

    # Part2: Inner sum over n from 1 to n_max
    inner_sum = mp.mpf(0)
    for n in range(1, n_max + 1):
        a2 = a1 + n  # 3/2 + k + n
        ab2 = a2 + b1  # 3 + k + n
        beta_val2 = mp.beta(a2, b1)
        psi0_a2 = mp.psi(0, a2)
        psi0_ab2 = mp.psi(0, ab2)
        diff_psi = psi0_a2 - psi0_ab2

        # Sign: (-1)^(n+1)
        sign = mp.mpf(-1)**(n + 1)
        term_inner = sign * beta_val2 * diff_psi / n
        inner_sum += term_inner

    part2 += binom_k * inner_sum

# Combine the parts with their respective coefficients
total = (mp.mpf('0.25') * part1) + (mp.mpf('0.25') * part2) - (ln2 * mp.mpf('0.5') * part3)

# Print the result to 10 decimal places
print(mp.nstr(total, n=10))