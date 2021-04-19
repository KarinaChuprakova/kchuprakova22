# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 21:57:15 2021

@author: Карина
"""

import modul
from flask import Flask

app = Flask(__name__)
@app.route("/")
def web():
    f = modul.Fibs()
    return modul.itertools.islice(f, 20)
    
if __name__ == "__main__":
    app.run()
