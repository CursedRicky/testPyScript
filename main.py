from pyscript import document
import random as r

def tiradado(valore):
    out = document.querySelector("#nascosto")
    out.innerText = f"Valore: {r.randint(1,valore)}"

def d6(*args, **kwargs):
    tiradado(6)

def d20(*args, **kwargs):
    tiradado(20)

def d2(*args, **kwargs):
    tiradado(2)

def d4(*args, **kwargs):
    tiradado(4)

def d8(*args, **kwargs):
    tiradado(8)

def d10(*args, **kwargs):
    tiradado(10)

def d12(*args, **kwargs):
    tiradado(12)

def d100(*args, **kwargs):
    tiradado(100)