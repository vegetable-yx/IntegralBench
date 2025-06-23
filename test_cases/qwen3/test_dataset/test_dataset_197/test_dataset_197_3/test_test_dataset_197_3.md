To evaluate the definite integral  
$$
\int_0^1 x \arcsin x \arccos x \, dx,
$$  
we proceed through a combination of substitution and integration by parts, leveraging known identities and simplifying the expression step-by-step.

---

### Step 1: Use of Identity

We begin by using the identity:
$$
\arccos x = \frac{\pi}{2} - \arcsin x.
$$
Substituting this into the integrand, we get:
$$
x \arcsin x \arccos x = x \arcsin x \left(\frac{\pi}{2} - \arcsin x\right) = \frac{\pi}{2} x \arcsin x - x (\arcsin x)^2.
$$
This allows us to split the integral:
$$
\int_0^1 x \arcsin x \arccos x \, dx = \frac{\pi}{2} \int_0^1 x \arcsin x \, dx - \int_0^1 x (\arcsin x)^2 \, dx.
$$

Let’s denote these two integrals as:
- $ I_1 = \int_0^1 x \arcsin x \, dx $,
- $ I_2 = \int_0^1 x (\arcsin x)^2 \, dx $.

---

### Step 2: Evaluate $ I_1 = \int_0^1 x \arcsin x \, dx $

Use the substitution $ x = \sin t $, so that $ \arcsin x = t $, $ dx = \cos t \, dt $, and the limits become:
- $ x = 0 \Rightarrow t = 0 $,
- $ x = 1 \Rightarrow t = \frac{\pi}{2} $.

Then:
$$
I_1 = \int_0^{\frac{\pi}{2}} t \sin t \cos t \, dt = \frac{1}{2} \int_0^{\frac{\pi}{2}} t \sin 2t \, dt.
$$
Using integration by parts:
- Let $ u = t $, $ dv = \sin 2t \, dt $,
- Then $ du = dt $, $ v = -\frac{1}{2} \cos 2t $.

$$
\int t \sin 2t \, dt = -\frac{t}{2} \cos 2t + \frac{1}{2} \int \cos 2t \, dt = -\frac{t}{2} \cos 2t + \frac{1}{4} \sin 2t.
$$
Evaluating from $ 0 $ to $ \frac{\pi}{2} $:
$$
\left[ -\frac{t}{2} \cos 2t + \frac{1}{4} \sin 2t \right]_0^{\frac{\pi}{2}} = -\frac{\pi}{4} \cdot (-1) + 0 = \frac{\pi}{4}.
$$
So,
$$
I_1 = \frac{1}{2} \cdot \frac{\pi}{4} = \frac{\pi}{8}.
$$

---

### Step 3: Evaluate $ I_2 = \int_0^1 x (\arcsin x)^2 \, dx $

Again, use the substitution $ x = \sin t $, so:
$$
I_2 = \int_0^{\frac{\pi}{2}} t^2 \sin t \cos t \, dt = \frac{1}{2} \int_0^{\frac{\pi}{2}} t^2 \sin 2t \, dt.
$$
This is a standard integral that can be evaluated via integration by parts twice. The result is:
$$
\int_0^{\frac{\pi}{2}} t^2 \sin 2t \, dt = \frac{\pi^2}{8} - \frac{1}{2}.
$$
Thus,
$$
I_2 = \frac{1}{2} \left( \frac{\pi^2}{8} - \frac{1}{2} \right) = \frac{\pi^2}{16} - \frac{1}{4}.
$$

---

### Step 4: Combine Results

Now substitute back:
$$
\int_0^1 x \arcsin x \arccos x \, dx = \frac{\pi}{2} \cdot \frac{\pi}{8