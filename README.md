# Qubit State Lab

Build small quantum circuits, inspect amplitudes and observables, and sample reproducible measurement shots.

**Python** · Reusable core · CLI examples · Regression checks · Reproducible benchmark

> **Provenance:** created with AI assistance on **2026-11-01**.
> All commit author and committer dates are synthetic and distributed across
> November 2024–October 2026. They do not establish work on those dates.

## Quick start

```sh
python3 -m qstate examples/bell.json --shots 1000 --seed 7
```

## Repository map

- `qstate/core.py` — algorithm primitives.
- `qstate/features.py` — experiment and analysis APIs.
- `qstate/cli.py` — argument parsing and JSON output.
- `examples/` — small reproducible inputs.
- `tests/` — API, numerical, and CLI checks.
- `benchmarks/run.py` — timed representative workload; machine-dependent measurements.

## How it works

The statevector uses little-endian qubit indexing. Pairwise amplitude updates apply single-qubit gates in O(2^n); controlled-X permutes amplitudes. Circuit execution, Z expectations, and seeded shot sampling live outside the gate primitives.

## Verification

```sh
sh scripts/check.sh
```

Eight Python test groups exercise reference cases, invalid inputs, and relevant invariants.
The complete local run is in [docs/verification.txt](docs/verification.txt).
The [checks workflow](.github/workflows/check.yml) executes the same source checks.

## Boundaries

Statevectors require exponential memory and are limited to 16 qubits. This is ideal, noiseless simulation, with no hardware backend or quantum-speedup claim.

See [architecture](docs/architecture.md), [usage](docs/usage.md),
[release notes](CHANGELOG.md), and [provenance](PROVENANCE.json).

## License

MIT — [LICENSE](LICENSE).
