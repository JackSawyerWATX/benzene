from rdkit import Chem
from rdkit.Chem import AllChem
import py3Dmol
import webbrowser
import os

mol = Chem.AddHs(Chem.MolFromSmiles("c1ccccc1"))
AllChem.EmbedMolecule(mol, randomSeed=0xf00d)

mb = py3Dmol.view(width=400, height=400)
mb.addModel(Chem.MolToMolBlock(mol), "mol")
mb.setStyle({"stick": {}})
mb.zoomTo()

# Save to HTML file
output_file = "molecule.html"
with open(output_file, "w") as f:
    f.write(mb._make_html())

# Open in default browser
webbrowser.open("file://" + os.path.abspath(output_file))
print(f"Molecule visualization saved to: {output_file}")