# simple-lpk
Simple tool for creating an ArcGIS layer package from a shapefile.

This tool simply applies pre-created layer files to a shapefile, and adds them to a zip file with the appropriate
folder layout.

The pre-generated styles are:
* red dots for point shapefiles
* black lines for line shapefiles
* black outlines for polygon shapefiles


## Installation:
* Make sure you have [pip](https://pip.pypa.io/en/stable/installing.html#pip-included-with-python) installed first
* Download this repository
* From the source directory, run ```pip install -e .```


## Example Usage:

```console
> pkg_lpk in.shp out.lpk
```


### Note:
ArcGIS is a registered trademark owned by ESRI, and is used in this project simply to provide reference to appropriate ESRI technologies.