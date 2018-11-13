# ---
# jupyter:
#   jupytext_format_version: '1.2'
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
#   language_info:
#     codemirror_mode:
#       name: ipython
#       version: 3
#     file_extension: .py
#     mimetype: text/x-python
#     name: python
#     nbconvert_exporter: python
#     pygments_lexer: ipython3
#     version: 3.6.3
# ---

import numpy as np
import cloudytab

m = cloudytab.CloudyModel("models/shell-R005-n30-LP_Ori")

m.data["ovr"]

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# %matplotlib inline

sns.set_color_codes()
sns.set_context('talk')

import astropy.units as u

u.cm.to(u.pc)

r_pc = m.data["rad"]["radius"]*u.cm.to(u.pc)
AV = m.data["ovr"]["AV(point)"]

# Plot density and temperature against radius in parsec

fig, ax = plt.subplots()
ax.plot(r_pc, m.data["ovr"]["eden"], label=r"Electron density")
ax.plot(r_pc, m.data["ovr"]["hden"], label=r"Total H density")
ax.plot(r_pc, m.data["ovr"]["Te"], label=r"Temperature")
ax.legend()
ax.set(xlim=[0, None], yscale='log', xlabel="Radius, pc")

# +
fig, ax = plt.subplots()
ax.plot(AV, m.data["ovr"]["eden"])
ax.plot(AV, m.data["ovr"]["hden"])
ax.plot(AV, m.data["ovr"]["Te"])

ax.set(xlim=[0, None], yscale='log')
# -


