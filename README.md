# Entropy Trace Formulation of the Riemann Hypothesis

This repository presents a real-variable, operator-theoretic formulation of the **Riemann Hypothesis (RH)** based on the **collapse of a thermally weighted entropy trace**. 

We introduce a trace-class operator \( H_∞ \) constructed from **prime-weighted cosine interference**, and show that the **heat trace**
\[
\Theta(t) = \mathrm{Tr}(e^{-t H_\infty})
\]
vanishes as \( t \to 0^+ \) **if and only if** the Riemann Hypothesis is true.

This spectral entropy framework:
- Does **not** require analytic continuation or the functional equation;
- Avoids explicit zero-counting or assumptions about zeta regularity;
- Provides a **real-variable equivalence**: RH ⇔ entropy collapse at \( \sigma = \frac{1}{2} \);
- Supports numerical Laplace inversion to **recover the nontrivial zeta zeros**.

## Getting Started

1. Clone or download the repo
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Open the demo notebook in `notebooks/`

## License

MIT License
