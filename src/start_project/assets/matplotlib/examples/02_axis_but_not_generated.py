"""
Axis
----

some options are presented here
"""

# %%
import cartopy.crs as ccrs
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(9, 4))
ax1 = fig.add_subplot(1, 2, 1, projection=ccrs.PlateCarree())

ax2 = fig.add_subplot(1, 2, 2, projection=ccrs.PlateCarree())

gridlines = ax2.gridlines(
    alpha=0.2,
    color="black",
    draw_labels=dict(bottom="x", right=False, top=False, left="y"),
    auto_update=True,
)
