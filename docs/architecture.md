# Architecture

The statevector uses little-endian qubit indexing. Pairwise amplitude updates apply single-qubit gates in O(2^n); controlled-X permutes amplitudes. Circuit execution, Z expectations, and seeded shot sampling live outside the gate primitives.

## Data flow

- `qstate/core.py` — algorithm primitives.
- `qstate/features.py` — experiment and analysis APIs.
- `qstate/cli.py` — argument parsing and JSON output.
- `examples/` — small reproducible inputs.
- `tests/` — API, numerical, and CLI checks.
- `benchmarks/run.py` — timed representative workload.

## Limits

Statevectors require exponential memory and are limited to 16 qubits. This is ideal, noiseless simulation, with no hardware backend or quantum-speedup claim.
