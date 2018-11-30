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

m = cloudytab.CloudyModel("models/shell-R005-n30-LP_Ori20")
m2 = cloudytab.CloudyModel("models/shell-R003-n29-LP_Ori20")
m3 = cloudytab.CloudyModel("models/shell-R001-n25-LP_Ori22")

m3.data["ovr"]

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
r_pc2 = m2.data["rad"]["radius"]*u.cm.to(u.pc)
r_pc3 = m3.data["rad"]["radius"]*u.cm.to(u.pc)
AV3 = m3.data["ovr"]["AV(point)"]

# Plot density and temperature against radius in parsec

fig, ax = plt.subplots()
ax.plot(r_pc3, m3.data["ovr"]["eden"], label=r"Electron density")
ax.plot(r_pc3, m3.data["ovr"]["hden"], label=r"Total H density")
ax.plot(r_pc3, m3.data["ovr"]["Te"], label=r"Temperature")
ax.legend()
ax.set(xlim=[0, None], yscale='log', xlabel="Radius, pc")

# +
fig, ax = plt.subplots()
ax.plot(AV3, m3.data["ovr"]["eden"])
ax.plot(AV3, m3.data["ovr"]["hden"])
ax.plot(AV3, m3.data["ovr"]["Te"])

ax.set(xlim=[0, None], yscale='log')
# -

# Compare the canonical model with the lower density, smaller radius one

# +
fig, ax = plt.subplots()

ax.plot(r_pc, m.data["ovr"]["eden"], color="r", label=r"Electron density")
ax.plot(r_pc2, m2.data["ovr"]["eden"], color="r", ls="--", label="_nolabel_")
ax.plot(r_pc3, m3.data["ovr"]["eden"], color="r", ls=":", label="_nolabel_")


ax.plot(r_pc, m.data["ovr"]["hden"], color="c", label=r"Total H density")
ax.plot(r_pc2, m2.data["ovr"]["hden"], color="c", ls="--", label="_nolabel_")
ax.plot(r_pc3, m3.data["ovr"]["hden"], color="c", ls=":", label="_nolabel_")


ax.legend()
ax.set(xlim=[0, None], yscale='log', xlabel="Radius, pc")
# -

# So, the low-density one is too low, and hence the i-front is at too large a radius. We need to try ones where we don't change the density so much. 

# Look again on a linear scale, with just the pressure.

# +
fig, ax = plt.subplots()

def Pgas(ovr_tab):
    return (ovr_tab["eden"] + ovr_tab["hden"])*ovr_tab["Te"]*1.38e-16

ax.plot(r_pc, Pgas(m.data["ovr"]), label=r"R005-n30-LP_Ori20")
ax.plot(r_pc2, Pgas(m2.data["ovr"]), label="R003-n28-LP_Ori20")
ax.plot(r_pc3, Pgas(m3.data["ovr"]), label="R001-n25-LP_Ori22")


ax.legend(loc="upper left", fontsize="small")
ax.set(xlim=[0, None], ylim=[0, None], yscale='linear', xlabel="Radius, pc", ylabel="Gas pressure")
None
# -

# ## New improved models
#
# Look at each of the new models

# +
models = ["R003-n29-LP_Ori20", "R005-n30-LP_Ori20", "R001-n25-LP_Ori20", "R003-n29-LP_Ori22", "R001-n25-LP_Ori22"]

fig, ax = plt.subplots(figsize=(8, 6))

for label in models:
    m = cloudytab.CloudyModel(f"models/shell-{label}")
    r_pc = m.data["rad"]["radius"]*u.cm.to(u.pc)
    ax.plot(r_pc, m.data["pre"]["Pgas"], label=label)
    
ax.legend(loc="upper left", fontsize="small")
ax.set(xlim=[0, None], ylim=[0, None], yscale='linear', xlabel="Radius, pc", ylabel="Gas pressure")
None
# -

# And the same for the low dust opacity models

# +
models = ["R003-n29-LP_Ori20", "R005-n30-LP_Ori20", "R001-n28-LP_Ori20"]


fig, ax = plt.subplots(figsize=(10, 6))

for label in models:
    m = cloudytab.CloudyModel(f"models/shell-{label}lowZ")
    r_pc = m.data["rad"]["radius"]*u.cm.to(u.pc)
    ax.plot(r_pc, m.data["pre"]["Pgas"], label=label+"lowZ")
    
ax.legend(loc="lower right", fontsize="small")
ax.set(xlim=[0, None], ylim=[0, None], yscale='linear', xlabel="Radius, pc", ylabel="Gas pressure")
None
# -

# That is better now, but it looks like the shells are too thick.  Now look at the densities.

# +
fig, ax = plt.subplots(figsize=(10, 6))

for label in models:
    m = cloudytab.CloudyModel(f"models/shell-{label}lowZ")
    r_pc = m.data["rad"]["radius"]*u.cm.to(u.pc)
    ax.plot(r_pc, m.data["ovr"]["hden"], label=label+"lowZ")
    ax.plot(r_pc, m.data["ovr"]["eden"], ls="--", label="_nolabel_")
    ax.plot(r_pc, m.data["ovr"]["Te"], ls=":", label="_nolabel_")


    
ax.legend(loc="upper left", fontsize="small")
ax.set(xlim=[0, None], ylim=[None, None], yscale='log', xlabel="Radius, pc", ylabel="Density")
None

# +
fig, ax = plt.subplots(figsize=(10, 6))

for label in models:
    m = cloudytab.CloudyModel(f"models/shell-{label}lowZ")
    r_pc = m.data["rad"]["radius"]*u.cm.to(u.pc)
    AV = m.data["ovr"]["AV(point)"]
    ax.plot(AV, m.data["ovr"]["hden"], label=label+"lowZ")
    ax.plot(AV, m.data["ovr"]["eden"], ls="--", label="_nolabel_")
    ax.plot(AV, m.data["ovr"]["Te"], ls=":", label="_nolabel_")


    
ax.legend(loc="right", fontsize="small")
ax.set(xlim=[0, None], ylim=[None, None], yscale='log', xlabel="Visual extinction, $A_V$", ylabel="Density")
None
# -

# So the problem was that we never got to the requested $A_V$.  The models hit the $T=100$ K first, and stopped because of that. I have changed the floor to 10 K, so they now do reach $A_V = 0.3$, but now they are too thick. 

# And the magnetic field models

# +
models = ["R003-n29-LP_Ori20", "R005-n30-LP_Ori20", "R001-n28-LP_Ori20"]


fig, ax = plt.subplots(figsize=(10, 6))

for label, color in zip(models, ["c", "orange", "g"]):
    m = cloudytab.CloudyModel(f"models/shell-{label}B")
    r_pc = m.data["rad"]["radius"]*u.cm.to(u.pc)
    ax.plot(r_pc, m.data["pre"]["Pgas"], color=color, label=label+"B")
    ax.plot(r_pc, m.data["pre"]["P(mag)"] + m.data["pre"]["P(turb)"], ls="--", color=color, label="_nolabel_")
    
ax.legend(loc="upper right", fontsize="small")
ax.set(xlim=[0, None], ylim=[0, None], yscale='linear', xlabel="Radius, pc", ylabel="Gas pressure")
None

# +
fig, ax = plt.subplots(figsize=(10, 6))

for label, color in zip(models, ["c", "orange", "g"]):
    m = cloudytab.CloudyModel(f"models/shell-{label}B")
    r_pc = m.data["rad"]["radius"]*u.cm.to(u.pc)
    ax.plot(r_pc, m.data["ovr"]["hden"], color=color, label=label+"B")
    ax.plot(r_pc, m.data["ovr"]["eden"], color=color, ls="--", label="_nolabel_")
    ax.plot(r_pc, m.data["ovr"]["Te"], color=color, ls=":", label="_nolabel_")


    
ax.legend(loc="right", fontsize="small")
ax.set(xlim=[0, None], ylim=[None, None], yscale='log', xlabel="Radius, pc", ylabel="Density")
None
# -

# Repeat for the models with constant Alfven speed

# +
models = ["R003-n29-LP_Ori20BB", "R005-n30-LP_Ori20BB", "R001-n23-LP_Ori20BB", "R001-n27-LP_Ori20Bz5"]


fig, ax = plt.subplots(figsize=(10, 6))

for label, color in zip(models, ["c", "orange", "g", "r"]):
    m = cloudytab.CloudyModel(f"models/shell-{label}")
    r_pc = m.data["rad"]["radius"]*u.cm.to(u.pc)
    ax.plot(r_pc, m.data["pre"]["Pgas"], color=color, label=label)
    ax.plot(r_pc, m.data["pre"]["P(mag)"] + m.data["pre"]["P(turb)"], ls="--", color=color, label="_nolabel_")
    
ax.legend(loc="right", fontsize="small")
ax.set(xlim=[0, None], ylim=[0, None], yscale='linear', xlabel="Radius, pc", ylabel="Gas pressure")
None

# +
fig, ax = plt.subplots(figsize=(10, 6))

for label, color in zip(models, ["c", "orange", "g", "r"]):
    m = cloudytab.CloudyModel(f"models/shell-{label}")
    r_pc = m.data["rad"]["radius"]*u.cm.to(u.pc)
    ax.plot(r_pc, m.data["ovr"]["hden"], color=color, label=label)
    ax.plot(r_pc, m.data["ovr"]["eden"], color=color, ls="--", label="_nolabel_")
    ax.plot(r_pc, m.data["ovr"]["Te"], color=color, ls=":", label="_nolabel_")


    
ax.legend(loc="right", fontsize="small")
ax.set(xlim=[0, None], ylim=[None, None], yscale='log', xlabel="Radius, pc", ylabel="Density")
None
# -

# ## Emissivity profiles

label = "R003-n29-LP_Ori20"
m = cloudytab.CloudyModel(f"models/shell-{label}")
r_pc = m.data["rad"]["radius"]*u.cm.to(u.pc)
em = m.data["emis"]

# +
fig, ax = plt.subplots(figsize=(15, 10))
drop_these_bands = "O  3 5006.84A", "nInu 6209.66A", "InwT 6209.66A", "H-CT 6562.81A", "Dest 6562.81A", "Ca A 6562.81A"

for band in em.colnames[1:]:
    if band in drop_these_bands:
        continue
    e = em[band]*(r_pc/0.01)**2
    ax.plot(r_pc, e/np.max(e), label=band)
    
ax.legend(ncol=2, fontsize="xx-small")
ax.set(xlim=[0, None], yscale='linear', ylim=[0.0, 1.05], xlabel="Radius, pc", ylabel=r"Emissivity $\times\ R^2$")
None

# +
fig, ax = plt.subplots(figsize=(15, 10))
for band in em.colnames[1:]:
    if band in drop_these_bands:
        continue
    e = em[band]*(r_pc/0.01)**2
    ax.plot(r_pc, e, label=band)
    
    
ax.legend(ncol=2, fontsize="xx-small", title=label)
ax.set(xlim=[0, None], yscale='log', ylim=[1e-20, None], xlabel="Radius, pc", ylabel=r"Emissivity $\times\ R^2$")
None

# +
label = "R001-n25-LP_Ori22"
m = cloudytab.CloudyModel(f"models/shell-{label}")
r_pc = m.data["rad"]["radius"]*u.cm.to(u.pc)
em = m.data["emis"]
fig, ax = plt.subplots(figsize=(15, 10))

for band in em.colnames[1:]:
    if band in drop_these_bands:
        continue
    e = em[band]*(r_pc/0.01)**2
    ax.plot(r_pc, e/np.max(e), label=band)
    
ax.legend(ncol=2, fontsize="xx-small", title=label)
ax.set(xlim=[0, None], yscale='linear', ylim=[0.0, 1.1], xlabel="Radius, pc", ylabel=r"Emissivity $\times\ R^2$")
None

# +
label = "R001-n25-LP_Ori22"
m = cloudytab.CloudyModel(f"models/shell-{label}")
r_pc = m.data["rad"]["radius"]*u.cm.to(u.pc)
em = m.data["emis"]
fig, ax = plt.subplots(figsize=(15, 10))

for band in em.colnames[1:]:
    if band in drop_these_bands:
        continue
    e = em[band]
    ax.plot(r_pc, e*(r_pc/0.01)**2, label=band)
    
ax.legend(ncol=2, fontsize="xx-small", title=label)
ax.set(xlim=[0, None], yscale='log', ylim=[1e-20, None], xlabel="Radius, pc", ylabel=r"Emissivity $\times\ R^2$")
None

# +
label = "R001-n25-LP_Ori22thick"
m = cloudytab.CloudyModel(f"models/shell-{label}")
r_pc = m.data["rad"]["radius"]*u.cm.to(u.pc)
em = m.data["emis"]
fig, ax = plt.subplots(figsize=(15, 10))

for band in em.colnames[1:]:
    if band in drop_these_bands:
        continue
    e = em[band]
    ax.plot(r_pc, e*(r_pc/0.01)**2, label=band)
    
ax.legend(ncol=2, fontsize="xx-small", title=label)
ax.set(xlim=[0, None], yscale='log', ylim=[1e-20, None], xlabel="Radius, pc", ylabel=r"Emissivity $\times\ R^2$")
None

# +
label = "R001-n28-LP_Ori20lowZ"
m = cloudytab.CloudyModel(f"models/shell-{label}")
r_pc = m.data["rad"]["radius"]*u.cm.to(u.pc)
em = m.data["emis"]
fig, ax = plt.subplots(figsize=(15, 10))

for band in em.colnames[1:]:
    if band in drop_these_bands:
        continue
    e = em[band]
    ax.plot(r_pc, e*(r_pc/0.01)**2, label=band)
    
ax.legend(ncol=2, fontsize="xx-small", title=label)
ax.set(xlim=[0, None], yscale='log', ylim=[1e-20, None], xlabel="Radius, pc", ylabel=r"Emissivity $\times\ R^2$")
None

# +
label = "R003-n29-LP_Ori20B"
m = cloudytab.CloudyModel(f"models/shell-{label}")
r_pc = m.data["rad"]["radius"]*u.cm.to(u.pc)
em = m.data["emis"]
fig, ax = plt.subplots(figsize=(15, 10))

for band in em.colnames[1:]:
    if band in drop_these_bands:
        continue
    e = em[band]
    ax.plot(r_pc, e*(r_pc/0.01)**2, label=band)
    
ax.legend(ncol=2, fontsize="xx-small", title=label)
ax.set(xlim=[0, None], yscale='log', ylim=[1e-20, None], xlabel="Radius, pc", ylabel=r"Emissivity $\times\ R^2$")
None

# +
label = "R003-n29-LP_Ori20BB"
m = cloudytab.CloudyModel(f"models/shell-{label}")
r_pc = m.data["rad"]["radius"]*u.cm.to(u.pc)
em = m.data["emis"]
fig, ax = plt.subplots(figsize=(15, 10))

for band in em.colnames[1:]:
    if band in drop_these_bands:
        continue
    e = em[band]
    ax.plot(r_pc, e*(r_pc/0.01)**2, label=band)
    
ax.legend(ncol=2, fontsize="xx-small", title=label)
ax.set(xlim=[0, None], yscale='log', ylim=[1e-20, None], xlabel="Radius, pc", ylabel=r"Emissivity $\times\ R^2$")
None

# +
label = "R001-n23-LP_Ori20BB"
m = cloudytab.CloudyModel(f"models/shell-{label}")
r_pc = m.data["rad"]["radius"]*u.cm.to(u.pc)
em = m.data["emis"]
fig, ax = plt.subplots(figsize=(15, 10))

for band in em.colnames[1:]:
    if band in drop_these_bands:
        continue
    e = em[band]
    ax.plot(r_pc, e*(r_pc/0.01)**2, label=band)
    
ax.legend(ncol=2, fontsize="xx-small", title=label)
ax.set(xlim=[0, None], yscale='log', ylim=[1e-20, None], xlabel="Radius, pc", ylabel=r"Emissivity $\times\ R^2$")
None

# +
label = "R001-n27-LP_Ori20Bz5"
m = cloudytab.CloudyModel(f"models/shell-{label}")
r_pc = m.data["rad"]["radius"]*u.cm.to(u.pc)
em = m.data["emis"]
fig, ax = plt.subplots(figsize=(15, 10))

for band in em.colnames[1:]:
    if band in drop_these_bands:
        continue
    e = em[band]
    ax.plot(r_pc, e*(r_pc/0.01)**2, label=band)
    
ax.legend(ncol=2, fontsize="xx-small", title=label)
ax.set(xlim=[0, None], yscale='log', ylim=[1e-20, None], xlabel="Radius, pc", ylabel=r"Emissivity $\times\ R^2$")
None

# +
label = "R001-n27-LP_Ori20Bz5"
m = cloudytab.CloudyModel(f"models/shell-{label}")
r_pc = m.data["rad"]["radius"]*u.cm.to(u.pc)
em = m.data["emis"]
fig, ax = plt.subplots(figsize=(15, 10))

for band in em.colnames[1:]:
    if band in drop_these_bands:
        continue
    e = em[band]
    ax.plot(r_pc, e/e[r_pc > 0.008].max(), label=band)
    
ax.legend(ncol=2, fontsize="xx-small", title=label)
ax.set(xlim=[0, None], yscale='linear', ylim=[0.0, 1.2], xlabel="Radius, pc", ylabel=r"Emissivity")
None
# -

# ## Grain drift

# It looks like the grains become uncoupled at the smallest radii

# +
#label = "R001-n23-LP_Ori20BB"
label = "R001-n27-LP_Ori20Bz5"
m = cloudytab.CloudyModel(f"models/shell-{label}")
r_pc = m.data["rad"]["radius"]*u.cm.to(u.pc)
vdrift= m.data["gdrift"]
fig, ax = plt.subplots(figsize=(15, 10))

for grain in vdrift.colnames[1:]:
    if grain.startswith("pah"):
        continue
    v = vdrift[grain]
    ax.plot(r_pc, v, label=grain)
    
ax.plot(r_pc, m.data["pre"]["cad(wind km/s)"], ls="--", color="k", label="sound speed")
ax.plot(r_pc, 2.0*np.ones_like(r_pc), ls=":", color="k", label="Alfven speed")

ax.legend(ncol=2, fontsize="xx-small", title=label)
ax.set(xlim=[0, None], yscale='log', ylim=[None, None], xlabel="Radius, pc", ylabel=r"Drift velocity")
None
# -

# So, the drift velocity is safely subsonic and sub-alfvenic in the shell and in the outer part of the ionized gas.

# +
label = "R003-n50-th1D-z-AV5"
m = cloudytab.CloudyModel(f"models/shell-{label}")
r_pc = m.data["rad"]["radius"]*u.cm.to(u.pc)
vdrift= m.data["gdrift"]
fig, ax = plt.subplots(figsize=(15, 10))

for grain in vdrift.colnames[1:]:
    if grain.startswith("pah"):
        continue
    v = vdrift[grain]
    ax.plot(r_pc, v, label=grain)
    
ax.plot(r_pc, m.data["pre"]["cad(wind km/s)"], ls="--", color="k", label="sound speed")
ax.plot(r_pc, 2.0*np.ones_like(r_pc), ls=":", color="k", label="Alfven speed")

ax.legend(ncol=2, fontsize="xx-small", title=label)
ax.set(xlim=[0, None], yscale='log', ylim=[None, None], xlabel="Radius, pc", ylabel=r"Drift velocity")
None
# -

# ## Look at theta 1 D

# +
models = [f"R003-{_}-th1D" for _ in ["n33", "n35", "n37"]]

fig, ax = plt.subplots(figsize=(10, 6))

for label, color in zip(models, ["c", "orange", "g"]):
    m = cloudytab.CloudyModel(f"models/shell-{label}")
    r_pc = m.data["rad"]["radius"]*u.cm.to(u.pc)
    ax.plot(r_pc, m.data["ovr"]["hden"], color=color, label=label)
    ax.plot(r_pc, m.data["ovr"]["eden"], color=color, ls="--", label="_nolabel_")
    ax.plot(r_pc, m.data["ovr"]["Te"], color=color, ls=":", label="_nolabel_")


    
ax.legend(loc="best", fontsize="small")
ax.set(xlim=[0, None], ylim=[None, None], yscale='log', xlabel="Radius, pc", ylabel="Density")
None

# +
models = ["R003-n45-th1D-z-AV3", "R003-n50-th1D-z-AV3", "R003-n50-th1D-z-AV5"]

fig, ax = plt.subplots(figsize=(10, 6))

for label, color in zip(models, ["c", "orange", "g"]):
    m = cloudytab.CloudyModel(f"models/shell-{label}")
    r_pc = m.data["rad"]["radius"]*u.cm.to(u.pc)
    ax.plot(r_pc, m.data["ovr"]["hden"], color=color, label=label)
    ax.plot(r_pc, m.data["ovr"]["eden"], color=color, ls="--", label="_nolabel_")
    ax.plot(r_pc, m.data["ovr"]["Te"], color=color, ls=":", label="_nolabel_")


    
ax.legend(loc="best", fontsize="small")
ax.set(xlim=[0, None], ylim=[None, None], yscale='log', xlabel="Radius, pc", ylabel="Density")
None

# +
fig, ax = plt.subplots(figsize=(10, 6))

for label, color in zip(models, ["c", "orange", "g"]):
    m = cloudytab.CloudyModel(f"models/shell-{label}")
    r_pc = m.data["rad"]["radius"]*u.cm.to(u.pc)
    ax.plot(r_pc, m.data["pre"]["Pgas"], color=color, label=label)
    ax.plot(r_pc, m.data["pre"]["P(mag)"] + m.data["pre"]["P(turb)"], ls="--", color=color, label="_nolabel_")
    ax.plot(r_pc, m.data["pre"]["Pinteg"], ls=":", color=color, label="_nolabel_")
    
ax.legend(loc="best", fontsize="small")
ax.set(xlim=[0, None], ylim=[0, None], yscale='linear', xlabel="Radius, pc", ylabel="Gas pressure")
None

# +
label = "R003-n50-th1D-z-AV5"
m = cloudytab.CloudyModel(f"models/shell-{label}")
r_pc = m.data["rad"]["radius"]*u.cm.to(u.pc)
em = m.data["emis"]
fig, ax = plt.subplots(figsize=(15, 10))

for band in em.colnames[1:]:
    if band in drop_these_bands:
        continue
    e = em[band]
    ax.plot(r_pc, e, label=band)
    
ax.legend(ncol=2, fontsize="xx-small", title=label)
ax.set(xlim=[0, None], yscale='log', ylim=[None, None], xlabel="Radius, pc", ylabel=r"Emissivity")
None

# +
models = ["R003-n45-th1D-1m000-AV3", "R003-n50-th1D-1m000-AV3", "R003-n50-th1D-1m000-AV5"]

fig, ax = plt.subplots(figsize=(10, 6))

for label, color in zip(models, ["c", "orange", "g"]):
    m = cloudytab.CloudyModel(f"models/shell-{label}")
    r_pc = m.data["rad"]["radius"]*u.cm.to(u.pc)
    ax.plot(r_pc, m.data["ovr"]["hden"], color=color, label=label)
    ax.plot(r_pc, m.data["ovr"]["eden"], color=color, ls="--", label="_nolabel_")
    ax.plot(r_pc, m.data["ovr"]["Te"], color=color, ls=":", label="_nolabel_")


    
ax.legend(loc="best", fontsize="small")
ax.set(xlim=[0, None], ylim=[None, None], yscale='log', xlabel="Radius, pc", ylabel="Density")
None

# +
label = "R003-n50-th1D-1m000-AV5"
m = cloudytab.CloudyModel(f"models/shell-{label}")
r_pc = m.data["rad"]["radius"]*u.cm.to(u.pc)
em = m.data["emis"]
fig, ax = plt.subplots(figsize=(15, 10))

for band in em.colnames[1:]:
    if band in drop_these_bands:
        continue
    e = em[band]
    ax.plot(r_pc, e, label=band)
    
ax.legend(ncol=2, fontsize="xx-small", title=label)
ax.set(xlim=[0, None], yscale='log', ylim=[None, None], xlabel="Radius, pc", ylabel=r"Emissivity")
None

# +
models = ["R003-n45-th1D-0m100-AV3", "R003-n50-th1D-0m100-AV3", "R003-n50-th1D-0m100-AV5"]

fig, ax = plt.subplots(figsize=(10, 6))

for label, color in zip(models, ["c", "orange", "g"]):
    m = cloudytab.CloudyModel(f"models/shell-{label}")
    r_pc = m.data["rad"]["radius"]*u.cm.to(u.pc)
    ax.plot(r_pc, m.data["ovr"]["hden"], color=color, label=label)
    ax.plot(r_pc, m.data["ovr"]["eden"], color=color, ls="--", label="_nolabel_")
    ax.plot(r_pc, m.data["ovr"]["Te"], color=color, ls=":", label="_nolabel_")


    
ax.legend(loc="best", fontsize="small")
ax.set(xlim=[0, None], ylim=[None, None], yscale='log', xlabel="Radius, pc", ylabel="Density")
None

# +
label = "R003-n50-th1D-0m100-AV5"
m = cloudytab.CloudyModel(f"models/shell-{label}")
r_pc = m.data["rad"]["radius"]*u.cm.to(u.pc)
em = m.data["emis"]
fig, ax = plt.subplots(figsize=(15, 10))

for band in em.colnames[1:]:
    if band in drop_these_bands:
        continue
    e = em[band]
    ax.plot(r_pc, e, label=band)
    
ax.legend(ncol=2, fontsize="xx-small", title=label)
ax.set(xlim=[0, None], yscale='log', ylim=[None, None], xlabel="Radius, pc", ylabel=r"Emissivity")
None

# +
models = ["R003-n45-th1D-twin-AV3", "R003-n50-th1D-twin-AV3", "R003-n50-th1D-twin-AV5"]

fig, ax = plt.subplots(figsize=(10, 6))

for label, color in zip(models, ["c", "orange", "g"]):
    m = cloudytab.CloudyModel(f"models/shell-{label}")
    r_pc = m.data["rad"]["radius"]*u.cm.to(u.pc)
    ax.plot(r_pc, m.data["ovr"]["hden"], color=color, label=label)
    ax.plot(r_pc, m.data["ovr"]["eden"], color=color, ls="--", label="_nolabel_")
    ax.plot(r_pc, m.data["ovr"]["Te"], color=color, ls=":", label="_nolabel_")


    
ax.legend(loc="best", fontsize="small")
ax.set(xlim=[0, None], ylim=[None, None], yscale='log', xlabel="Radius, pc", ylabel="Density")
None

# +
label = "R003-n50-th1D-twin-AV5"
m = cloudytab.CloudyModel(f"models/shell-{label}")
r_pc = m.data["rad"]["radius"]*u.cm.to(u.pc)
em = m.data["emis"]
fig, ax = plt.subplots(figsize=(15, 10))

for band in em.colnames[1:]:
    if band in drop_these_bands:
        continue
    e = em[band]
    ax.plot(r_pc, e, label=band)
    
ax.legend(ncol=2, fontsize="xx-small", title=label)
ax.set(xlim=[0, None], yscale='log', ylim=[None, None], xlabel="Radius, pc", ylabel=r"Emissivity")
None

# +
models = ["R001-n45-th1D-triple-AV3", "R003-n50-th1D-triple-AV3", "R003-n50-th1D-triple-AV5"]

fig, ax = plt.subplots(figsize=(10, 6))

for label, color in zip(models, ["c", "orange", "g"]):
    m = cloudytab.CloudyModel(f"models/shell-{label}")
    r_pc = m.data["rad"]["radius"]*u.cm.to(u.pc)
    ax.plot(r_pc, m.data["ovr"]["hden"], color=color, label=label)
    ax.plot(r_pc, m.data["ovr"]["eden"], color=color, ls="--", label="_nolabel_")
    ax.plot(r_pc, m.data["ovr"]["Te"], color=color, ls=":", label="_nolabel_")


    
ax.legend(loc="best", fontsize="small")
ax.set(xlim=[0, None], ylim=[None, None], yscale='log', xlabel="Radius, pc", ylabel="Density")
None

# +
label = "R003-n50-th1D-triple-AV3"
m = cloudytab.CloudyModel(f"models/shell-{label}")
r_pc = m.data["rad"]["radius"]*u.cm.to(u.pc)
em = m.data["emis"]
fig, ax = plt.subplots(figsize=(15, 10))

for band in em.colnames[1:]:
    e = em[band]
    ax.plot(r_pc, e, label=band)
    
ax.legend(ncol=2, fontsize="xx-small", title=label)
ax.set(xlim=[0, None], yscale='log', ylim=[None, None], xlabel="Radius, pc", ylabel=r"Emissivity")
None
# -


