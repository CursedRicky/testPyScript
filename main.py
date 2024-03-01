from pyscript import document
import random as r

enable = False

def test(*args, **kwargs):
    print("A")
    out = document.querySelector("#nascosto")
    out.innerText = f"Valore {r.randint(1,6)}"
