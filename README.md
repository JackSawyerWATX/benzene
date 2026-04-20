# Benzene Molecule Visualization

## Description

This project generates and visualizes a 3D molecular structure of benzene using RDKit and py3Dmol. The benzene molecule is created with hydrogen atoms and 3D coordinates, then rendered in an interactive 3D viewer that opens in your default web browser.

Benzene (C₆H₆) is a fundamental aromatic compound consisting of a six-membered carbon ring with alternating single and double bonds, along with hydrogen atoms bonded to each carbon.

## Technologies Used

- **RDKit** - Open-source cheminformatics software library for working with molecular structures
- **py3Dmol** - Python wrapper for 3Dmol.js, enabling interactive 3D molecular visualization
- **Python 3.13** - Programming language

## Installation

1. Clone the repository or download the files
2. Install required dependencies:

```bash
pip install rdkit py3Dmol
```

## How to Run

1. Navigate to the project directory:

```bash
cd path/to/benzene
```

2. Run the script:

```bash
python benzene.py
```

3. A browser window will automatically open displaying the 3D benzene molecule visualization

## Output

The script generates:
- `molecule.html` - An interactive HTML file containing the 3D molecule visualization
- Opens automatically in your default web browser

## Features

- **3D Visualization** - Interactive 3D rendering of the benzene molecule
- **Stick Model** - Molecular structure displayed using stick representation
- **Auto-rotation** - View is automatically zoomed to fit the molecule
- **Interactive** - Rotate, zoom, and pan the molecule in the browser viewer

## Requirements

- Python 3.7+
- Modern web browser with WebGL support
