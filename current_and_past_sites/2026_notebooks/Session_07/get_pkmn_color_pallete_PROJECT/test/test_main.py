import sys, pathlib, matplotlib
matplotlib.use("Agg")  # no GUI needed for tests

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

# sanity check: this should exist in your tree
assert (ROOT / "src" / "get_pokemon_color_palletes" / "core.py").exists()

import numpy as np
import matplotlib.pyplot as plt
from get_pokemon_color_palletes.core import get_pkmn_pallete  # <-- the fix


pkmn=str(413)

pkmn='pikachu'

pkmn='Skeledirge'

colors = get_pkmn_pallete(pkmn)

for x in range(len(colors)):

    plt.scatter(x,np.sin(x),color=np.array(colors[x]),s=20**2)
    
plt.gca().set_facecolor('black')

plt.xticks([])

plt.yticks([])

plt.savefig('pkmn_pallete.png')

plt.close()
