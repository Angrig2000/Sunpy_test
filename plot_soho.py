from pathlib import Path
import hvpy
from hvpy.datasource import DataSource
from datetime import datetime
import sunpy.map
import matplotlib.pyplot as plt


date = datetime(2024,4,1,10,0,0,0)
fname = f'EIT195_{date:%y%m%d}.jp2'
if not Path(fname).exists():
    hvpy.save_file(
        hvpy.getJP2Image(date, DataSource.EIT_195.value),
        fname)
eit_map = sunpy.map.Map(fname)
fig = plt.figure()
ax = fig.add_subplot(projection=eit_map)
eit_map.plot(axes=ax)
plt.savefig(Path(fname).with_suffix('.png'))