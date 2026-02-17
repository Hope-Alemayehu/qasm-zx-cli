#!/usr/bin/env python3
import argparse
import pyzx as zx
from pyzx import Circuit
import matplotlib.pyplot as plt
import os

def main():
    parser = argparse.ArgumentParser(
        description="Minimal Quantum Circuit Renderer (QASM → Image)"
    )
    parser.add_argument("input", help="Path to QASM file")
    parser.add_argument("--output", help="Output file (png, pdf)")

    args = parser.parse_args()

    # Check file exists
    if not os.path.exists(args.input):
        print(f"Error: File {args.input} does not exist")
        return

    # Load QASM and convert to graph
    with open(args.input, "r") as f:
        qasm = f.read()
    circuit = Circuit.from_qasm(qasm)
    g = circuit.to_graph()

    
    fig = zx.draw_matplotlib(g, figsize=(10, 2), h_edge_draw='box')
   
      
    ax = fig.axes[0] if fig.axes else None
    if ax is not None:
        rows = [g.row(v) for v in g.vertices()]
        ys = [-g.qubit(v) for v in g.vertices()]
        if rows and ys:
            pad_x = 1
            pad_y = 1
            ax.set_xlim(min(rows) - pad_x, max(rows) + pad_x)
            ax.set_ylim(min(ys) - pad_y, max(ys) + pad_y)

    # Save or show
    if args.output:
        fig.savefig(args.output, bbox_inches='tight')
        print(f"Saved image to {args.output}")
    else:
        plt.show()

if __name__ == "__main__":
    main()

