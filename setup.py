from setuptools import setup

setup(
    name='simple-lpk',
    version='0.0.2',
    url='https://github.com/databasin/simple-lpk',
    license='see LICENSE',
    author='databasin',
    author_email='databasinadmin@consbio.org',
    description='Simple tool for creating an ArcGIS layer package from a shapefile',
    py_modules=['pkg'],
    data_files=[('lyr', ['lyr/line.lyr', 'lyr/point.lyr', 'lyr/polygon.lyr'])],
    entry_points='''
        [console_scripts]
        pkg_lpk=pkg:pkg_lpk
    '''
)
