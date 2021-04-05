import numpy as np 
import pygmt

np.random.seed(0)

minlon, maxlon = -142, -128
minlat, maxlat = 50, 60

## Generate fake coordinates in the range for plotting
lons = minlon + np.random.rand(10)*(maxlon-minlon)
lats = minlat + np.random.rand(10)*(maxlat-minlat)


#define etopo data file
topo_data = '@earth_relief_30s' #30 arc second global relief (SRTM15+V2.1 @ 1.0 km)
basement_grid = "Bouger_copy.nc"

# Visualization
fig = pygmt.Figure()

# make color pallets
pygmt.makecpt(
    cmap='topo',
    series='-8000/8000/1000',
    continuous=True
)

#plot high res topography
fig.grdimage(
    grid=topo_data,
    region=[minlon, maxlon, minlat, maxlat], 
    projection='M4i',
    frame=["ag","x+lLongitude","y+lLatitude"],
    shading=True
    )

# plot coastlines
fig.coast(
    region=[minlon, maxlon, minlat, maxlat], 
    projection='M4i', 
    shorelines=True,
    )

# plot topo contour lines
#fig.grdcontour(
#    grid=basement_grid,
#    interval=250,
#    annotation="4000+f6p",
    # annotation="1000+f6p",
#    limit="-8000/0",
#    pen="a0.15p"
#    )

fig.grdimage(
    grid=basement_grid,
    frame=["ag","x+lLongitude","y+lLatitude"],
    shading=True,
    projection="M4i",
    transparency=35,
    cmap="gray",
    nan_transparent=True
    )

# plot topo contour lines
fig.grdcontour(
    grid=basement_grid,
    interval=30,
    annotation="4000+f6p",
    # annotation="1000+f6p",
    limit="-400/400",
    pen="a0.15p"
    )    

# plot data points
#fig.plot(
#    x=lons,
#    y=lats, 
#    style='c0.1i', 
#    color='red', 
#    pen='black', 
#    label='something',
#    )

## Plot colorbar
# Default is horizontal colorbar
#fig.colorbar(
#    frame='+l"Topography"'
#    )


# save figure as pdf
fig.savefig("fm-plot8.pdf", crop=True, dpi=300)