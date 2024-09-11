"""
Features
--------

basic's feature example
"""

import cartopy.crs as ccrs

# %%
import cartopy.feature as cfeature
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(9, 4))
ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())

gridlines = ax.gridlines(
    alpha=0.2,
    color="black",
    draw_labels=dict(bottom="x", right=False, top=False, left="y"),
    auto_update=True,
)
ax.add_feature(
    cfeature.OCEAN,
)
ax.add_feature(cfeature.LAND, color="grey")
ax.add_feature(cfeature.COASTLINE, linewidths=2, linestyle=":", edgecolor="red")
