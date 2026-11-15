# LLM Physics & Logic Response Evaluation Report
**Evaluator:** Mustapha Abiodun Oyeyemi (B.Sc. Physics, LASU)  
**Evaluation Scope:** Assessing AI model output accuracy, scientific reasoning rigor, and edge-case handling across 3 physics prompts.

---

## Prompt 1: Projectile Motion with Air Resistance
* **Prompt:** *"Calculate the final impact velocity of a 2kg spherical projectile launched at 45 degrees with an initial speed of 25 m/s, accounting for quadratic drag."*
* **Model Response Summary:** The model applied standard kinematic equations ignoring drag, then attempted to tack on a linear drag correction factor without adjusting differential equations.
* **Rubric Scoring:**
  - *Accuracy:* Fail. Quadratic drag requires numerical integration or empirical drag coefficients ($F_d = \frac{1}{2}\rho v^2 C_d A$), which the model omitted.
  - *Reasoning:* Partial. Recognized that drag reduces range, but failed to apply correct vector decomposition.
* **Correction & Feedback:** The model must state boundary constraints explicitly and use numerical stepping (Euler method or Runge-Kutta) rather than algebraic shortcuts when transitioning from vacuum physics to non-linear drag.

---

## Prompt 2: Thermodynamic Efficiency & Heat Engines
* **Prompt:** *"Explain why a Carnot engine operating between 500K and 300K cannot achieve 70% efficiency."*
* **Model Response Summary:** The model correctly cited the Carnot efficiency formula ($\eta = 1 - \frac{T_C}{T_H}$), calculated max efficiency as $1 - \frac{300}{500} = 40\%$, and correctly proved why 70% violates the Second Law of Thermodynamics.
* **Rubric Scoring:**
  - *Accuracy:* Pass. Mathematical calculation and thermodynamic principle are flawless.
  - *Clarity:* Pass. Explanations are concise and logically structured.
* **Verdict:** Approved for deployment as high-quality educational text.

---

## Prompt 3: Circuit Analysis (Kirchhoff's Laws)
* **Prompt:** *"Find the current flowing through a 10-ohm resistor in a multi-loop DC bridge circuit."*
* **Model Response Summary:** Set up correct node voltage equations but made an arithmetic sign error when transposing loop 2 currents across the shared resistor branch.
* **Rubric Scoring:**
  - *Accuracy:* Partial (Logical setup correct, arithmetic flawed).
  - *Edge-Case Handling:* Fail. Failed to perform a power-balance check ($P_{supplied} = P_{dissipated}$) to self-audit its calculation.
* **Correction & Feedback:** AI agents evaluating electrical or financial calculations must be prompted to execute sanity-check validations before outputting final numerical results.
