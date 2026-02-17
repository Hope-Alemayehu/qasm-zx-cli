# Quantum Circuit Renderer

A minimal command-line tool to render OpenQASM 2.0 quantum circuits as images (PNG/PDF) using PyZX.

## Features

- Parses OpenQASM 2.0 files
- Renders quantum circuits with the `box` style
- Outputs PNG or PDF
- Handles basic gates (H, CX, T, Tdg, X, etc.)

## Requirements

- Python 3.11+
- Install dependencies:
  ```bash
  pip install -r requirements.txt
  ```

## Usage

```bash
python quantum_style.py <input.qasm> --output <output.png|output.pdf>
```

### Examples

```bash
# Render to PNG
python quantum_style.py example.qasm --output circuit.png

# Render to PDF
python quantum_style.py example.qasm --output circuit.pdf

# Show in a window (no --output)
python quantum_style.py example.qasm
```

## Notes

- Classical registers and `measure` statements are not supported in the QASM input.
- The renderer always uses the `box` style for Hadamard edges.
- Output images are automatically cropped to fit the circuit.

## Example QASM

See `example.qasm` for a simple 2-qubit circuit:

```qasm
OPENQASM 2.0;
include "qelib1.inc";

qreg q[2];

h q[0];
cx q[0],q[1];
t q[0];
tdg q[1];
x q[1];
```