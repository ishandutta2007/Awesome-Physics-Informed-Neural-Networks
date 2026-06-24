# Awesome-Physics-Informed-Neural-Networks
## Physics-Informed Neural Networks (PINNs): Evolution, Variants, & Applications

Physics-Informed Neural Networks (PINNs) represent a groundbreaking convergence between deep learning and classical computational physics. Traditional neural networks act as pure data-driven black boxes, frequently violating fundamental physical constraints when data is scarce. PINNs solve this by embedding physical laws—expressed as Partial Differential Equations (PDEs)—directly into the neural network's loss function using Automatic Differentiation (AD). The network is penalized not just for failing to match data points, but for violating conservation laws, boundary conditions, or physical symmetries.

---

## 1. The Chronological Evolution

The architectural progression of PINNs highlights a transition from simple boundary-value solvers to highly adaptive, multi-scale, and stochastic physical simulators.

```mermaid
flowchart LR
    A["Vanilla PINNs (2019)<br/>(Single Global Network)"] ---> B["XPINNs / Domain Decomposition<br/>(Distributed Local Subnetworks)"] 
    B ---> C["Neural Operators (FNO / DeepONet)<br/>(Infinite-Dimensional PDE Mapping)"] 
```

*   **The Vanilla PINN Era (Raissi et al., 2019)**
    *   *Concept:* The foundation. Parameterized a physical state using a standard Multi-Layer Perceptron (MLP). Computed exact spatial and temporal derivatives using automatic differentiation, adding the residual of the target PDE directly to the loss function.
*   **Domain Decomposition & Parallelization (cPINNs / XPINNs, ~2020–2022)**
    *   *Concept:* Overcame the limitation of a single network trying to learn massive, complex geometric domains. Split the physical space into distinct sub-domains, assigning a dedicated local neural network to each slice while mathematically enforcing continuity along interfaces.
*   **The Operator Learning Era (Modern Progression)**
    *   *Concept:* Shifts from solving a single instance of a PDE to learning entire *families* of differential equations. Systems like **Fourier Neural Operators (FNO)** and **DeepONets** learn infinite-dimensional mappings between function spaces, allowing instantaneous inference for any variable boundary condition or initial state.

---

## 2. Core Mathematical & Architectural Variants

These structural variants alter how physical laws are formulated, partitioned, or calculated to improve training stability and handle multi-scale physical phenomena.

*   **Variational PINNs (VPINNs)**
    *   *Mechanism:* Embeds the PDE using its variational (weak) mathematical form. It integrates the PDE residual against a set of localized test functions (e.g., polynomial baselines) before feeding it to the loss optimizer.
    *   *Pros:* Drastically reduces the order of differentiation required by automatic differentiation, making it highly robust when handling non-smooth or discontinuous physical solutions (like shock waves).
*   **Fractional PINNs (fPINNs)**
    *   *Mechanism:* Extends standard calculus to fractional-order derivatives, which utilize non-local operators to model memory effects and anomalous diffusion behaviors.
*   **Conservative PINNs (cPINNs)**
    *   *Mechanism:* Strictly enforces macro-level conservation laws (like conservation of mass, momentum, or energy) directly across sub-domain boundaries using specialized internal flux-flux optimization constraints.
*   **Inverse-PINNs (Parameter Estimation)**
    *   *Mechanism:* Operates in reverse. Instead of predicting a physical state from a known equation, it uses sparse, noisy real-world sensor measurements to backwards-solve and discover unknown physical coefficients (like fluid viscosity or material elasticity constants).

---

## 3. Stochastic & Uncertainty Quantification Types

These advanced variations adapt PINNs to handle environmental noise, random initialization states, and unpredictable material behaviors.

*   **Bayesian PINNs (B-PINNs)**
    *   *Type:* Probabilistic Physics Integration.
    *   *Mechanism:* Replaces deterministic neural network weights with probability distributions using Hamiltonian Monte Carlo or Variational Inference.
    *   *Significance:* Quantifies both **aleatoric uncertainty** (noise in physical measurements) and **epistemic uncertainty** (lack of data or incomplete physics descriptions).
*   **Stochastic PINNs (SPINNs)**
    *   *Type:* Random Vector Field Solvers.
    *   *Mechanism:* Tailored to solve Stochastic Partial Differential Equations (SPDEs) by appending a continuous Brownian motion or random noise tensor to the physical constraint layer.

---

## 4. Real-World Engineering Applications

*   **Subsurface Fluid Dynamics & Reservoir Engineering**
    *   *Application:* Simulates oil, water, or gas migration through porous underground rock structures over decades. PINNs incorporate the Darcy Flow equations to accurately forecast reservoir depletion using highly sparse drill-hole data.
*   **Aerodynamic Shape Optimization**
    *   *Application:* Replaces computationally expensive, multi-hour Computational Fluid Dynamics (CFD) grid simulations. PINNs embed the Naviers-Stokes equations to instantly predict airflow velocity and pressure profiles around experimental aircraft wings or vehicle chassis.
*   **Biomedical Cardiovascular Modeling**
    *   *Application:* Models patient-specific blood flow trajectories through complex, irregular arterial blockages (aneurysms). PINNs fuse low-resolution MRI scan imagery with exact fluid mechanics equations to evaluate localized wall shear stress without requiring invasive surgical sensors.
