"""
==============================================
Requesting cutouts of AIA images from the JSOC
==============================================

This example shows how to request a cutout of a series of
AIA images from the JSOC.
"""
import os
from dotenv import load_dotenv

import matplotlib.pyplot as plt

import astropy.units as u
from astropy.coordinates import SkyCoord
from astropy.time import Time
from astropy.visualization import ImageNormalize, SqrtStretch

import sunpy.coordinates  # NOQA
import sunpy.map
from sunpy.net import Fido
from sunpy.net import attrs as a

#####################################################
# As this is an example, we have already worked out where
# we need to crop for the active region we want to showcase.

start_time = Time('2012-09-24T14:56:03', scale='utc', format='isot')
#bottom_left = SkyCoord(-500*u.arcsec, -275*u.arcsec, obstime=start_time, observer="earth", frame="helioprojective")
#top_right = SkyCoord(150*u.arcsec, 375*u.arcsec, obstime=start_time, observer="earth", frame="helioprojective")

#####################################################
# Now construct the cutout from the coordinates above
# above using the `~sunpy.net.jsoc.attrs.Cutout` attribute.

#cutout = a.jsoc.Cutout(bottom_left, top_right=top_right, tracking=True)

#####################################################
# Exporting data from the JSOC requires registering your email first.
# Please replace this with your email address once you have registered
# like so: jsoc_email = "your_email@example.com"
# See `this page <http://jsoc.stanford.edu/ajax/register_email.html>`__ for more details.

load_dotenv()
jsoc_email = os.environ["JSOC_EMAIL"]

#####################################################
# Now we are ready to construct the query. Note that all of this is
# the same for a full-frame image except for the
# cutout component. We will download images from a 12 hour interval
# centered on the time of the above cutout.
# We request one image every 2 hours.

query = Fido.search(
    a.Time(start_time, start_time + 1*u.s),
    a.Wavelength(171*u.angstrom),
    a.jsoc.Series.aia_lev1_euv_12s, # 94 Å,131 Å,171 Å, 193 Å, 211 Å, 304 Å, 335 Å
    a.jsoc.Notify(jsoc_email),
    #a.jsoc.Segment.image,
    #cutout,
)
print(query)

#####################################################
# Submit the export request and download the data.

file = Fido.fetch(query)

#####################################################
# Now that we've downloaded the files, we can create
# a `~sunpy.map.MapSequence` from them and animate
# them.
print(file)
map = sunpy.map.Map(file[0])

fig = plt.figure()
ax = fig.add_subplot(projection=map)
ani = map.plot(axes=ax, norm=ImageNormalize(vmin=0, vmax=5e3, stretch=SqrtStretch()))

plt.show()
