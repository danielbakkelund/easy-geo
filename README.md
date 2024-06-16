# easy-geo-py
A very-easy-to-use library for conversion between geographical coordinate (GPS, Google maps etc) and Cartesian coordinates.

The library allows you to set up a two-way transformer to convert between geo-coordinates and Cartesian coordinates.
The library does not require you to know anything about coordinate transformations, UTM-zones or anything alike. 
The down-side is that you can only use it for fairly simple operations. 
If you need something more powerful, you should look somewhere else.

## Example

In this example, we have a data set of geo locations, and want to convert them to cartesian coordinates,
so that we can measure the distance between these locations in meters.

```python
import easy-geo-py as egp
import numpy as np
import numpy.linalg as npl

lat1 = 69.846781
lon1 = 19.993397

lat2 = 69.842767
lon2 = 20.044246

# Set up a transformer with origin in (lat1,lon1)
transformer = egp.Transformer(lat=lat1,lon=lon1, unit='m')

# Compute the cartesian coords of the points
c1 = transformer.to_cart(lat1,lon1)
c2 = transformer.to_cart(lat2,lon2)

# Compute their Euclidean distance in meters
dist = npl.norm(c1-c2)
```
