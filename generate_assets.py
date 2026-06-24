import os

docs_dir = 'docs'
os.makedirs(docs_dir, exist_ok=True)

pages = {
    'vanilla_pinn.md': '# The Vanilla PINN Era\n\nVanilla PINNs introduced the concept of adding the PDE residual to the loss function.\n\n```mermaid\ngraph TD;\n    A[Coordinates x, t] --> B[Neural Network]\n    B --> C[Prediction u]\n    C --> D[Automatic Differentiation]\n    D --> E[PDE Residual]\n    E --> F[Loss Function]\n```\n\n[Back to README](../README.md)',
    'domain_decomposition_pinn.md': '# Domain Decomposition & Parallelization (cPINNs / XPINNs)\n\nSplits the domain into sub-domains with independent networks.\n\n```mermaid\ngraph TD;\n    A[Domain] --> B[Sub-domain 1]\n    A --> C[Sub-domain 2]\n    B --> D[Network 1]\n    C --> E[Network 2]\n    D --> F[Interface Conditions]\n    E --> F\n```\n\n[Back to README](../README.md)',
    'operator_learning_pinn.md': '# The Operator Learning Era\n\nLearns infinite-dimensional mappings between function spaces.\n\n```mermaid\ngraph TD;\n    A[Input Function] --> B[Branch Net]\n    C[Coordinates] --> D[Trunk Net]\n    B --> E[Dot Product]\n    D --> E\n    E --> F[Output Solution]\n```\n\n[Back to README](../README.md)',
    'variational_pinn.md': '# Variational PINNs (VPINNs)\n\nEmbeds the weak formulation of PDEs to handle discontinuities.\n\n```mermaid\ngraph TD;\n    A[Weak Form] --> B[Integration with Test Functions]\n    B --> C[Residual Loss]\n```\n\n[Back to README](../README.md)',
    'fractional_pinn.md': '# Fractional PINNs (fPINNs)\n\nUses fractional calculus for non-local operators.\n\n```mermaid\ngraph TD;\n    A[Input] --> B[NN]\n    B --> C[Fractional Derivative Operator]\n    C --> D[Loss]\n```\n\n[Back to README](../README.md)',
    'conservative_pinn.md': '# Conservative PINNs (cPINNs)\n\nEnforces macroscopic conservation laws across domains.\n\n```mermaid\ngraph TD;\n    A[Sub-domain 1] -->|Flux Interface| B[Sub-domain 2]\n```\n\n[Back to README](../README.md)',
    'inverse_pinn.md': '# Inverse-PINNs (Parameter Estimation)\n\nDiscovers physical parameters from sparse data.\n\n```mermaid\ngraph TD;\n    A[Data] --> B[NN Loss]\n    B --> C[Unknown Parameters optimized]\n```\n\n[Back to README](../README.md)',
    'bayesian_pinn.md': '# Bayesian PINNs (B-PINNs)\n\nProvides uncertainty quantification using Bayesian inference.\n\n```mermaid\ngraph TD;\n    A[Priors] --> B[Posterior via HMC/VI]\n    B --> C[Predictions + Uncertainty]\n```\n\n[Back to README](../README.md)',
    'stochastic_pinn.md': '# Stochastic PINNs (SPINNs)\n\nSolves Stochastic PDEs by handling random fields.\n\n```mermaid\ngraph TD;\n    A[Random variables] --> B[NN]\n    B --> C[SPDE Residual]\n```\n\n[Back to README](../README.md)',
    'subsurface_fluid_dynamics_pinn.md': '# Subsurface Fluid Dynamics & Reservoir Engineering\n\nApplies PINNs to simulate Darcy flow in porous media.\n\n```mermaid\ngraph TD;\n    A[Drill-hole Data] --> B[PINN with Darcy Eq]\n    B --> C[Reservoir Forecast]\n```\n\n[Back to README](../README.md)',
    'aerodynamic_shape_optimization_pinn.md': '# Aerodynamic Shape Optimization\n\nUses Navier-Stokes embedded networks for fast CFD.\n\n```mermaid\ngraph TD;\n    A[Shape params] --> B[PINN Naviers-Stokes]\n    B --> C[Pressure/Velocity profile]\n```\n\n[Back to README](../README.md)',
    'biomedical_cardiovascular_modeling_pinn.md': '# Biomedical Cardiovascular Modeling\n\nModels blood flow using MRI data and fluid equations.\n\n```mermaid\ngraph TD;\n    A[MRI Data] --> B[PINN]\n    B --> C[Wall Shear Stress]\n```\n\n[Back to README](../README.md)'
}

for filename, content in pages.items():
    with open(os.path.join(docs_dir, filename), 'w') as f:
        f.write(content)

os.makedirs('assets', exist_ok=True)
svg_content = """<svg width="800" height="200" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <linearGradient id="grad1" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:#4facfe;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#00f2fe;stop-opacity:1" />
        </linearGradient>
    </defs>
    <rect width="800" height="200" fill="url(#grad1)" rx="15" />
    <text x="50%" y="50%" font-family="Arial" font-size="40" fill="white" font-weight="bold" text-anchor="middle" dominant-baseline="middle">
        Awesome Physics-Informed Neural Networks
    </text>
    <text x="50%" y="75%" font-family="Arial" font-size="20" fill="white" text-anchor="middle" dominant-baseline="middle">
        Curated List &amp; Resources
    </text>
</svg>"""
with open('assets/banner.svg', 'w') as f:
    f.write(svg_content)
