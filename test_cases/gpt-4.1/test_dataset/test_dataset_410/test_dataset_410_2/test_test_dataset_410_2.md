Let's proceed step-by-step:

1. **Start with the integral:**
   \[
   I = \int_0^\infty e^{-x^2} \cos(2x) \, dx
   \]

2. **Recall a standard result:**
   \[
   \int_0^\infty e^{-a x^2} \cos(bx) \, dx = \frac{1}{2} \sqrt{\frac{\pi}{a}}\, e^{-\frac{b^2}{4a}} \quad \text{for} \quad a > 0
   \]

   Here, \( a = 1 \), \( b = 2 \):

3. **Substitute values:**
   \[
   I = \frac{1}{2} \sqrt{\frac{\pi}{1}}\, e^{-\frac{2^2}{4\cdot 1}}
   = \frac{1}{2} \sqrt{\pi}\, e^{-1}
   \]

   So the exact answer is:
   \[
   I = \frac{\sqrt{\pi}}{2e}
   \]

4. **Numerical evaluation:**

   - \( \sqrt{\pi} \approx 1.7724538509 \)
   - \( e \approx 2.7182818285 \)
   - \( \frac{\sqrt{\pi}}{2e} \approx \frac{1.7724538509}{2 \times 2.7182818285} \approx \frac{1.7724538509}{5.436563657} \approx 0.3264827485 \)

---

```json
{"answer": "\\frac{\\sqrt{\\pi}}{2e}", "numerical_answer": "0.3264827485"}
```