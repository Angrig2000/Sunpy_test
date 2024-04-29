from sunpy.net import Fido
from sunpy.net import attrs as a
from sunpy.timeseries import TimeSeries

trange = a.Time('2024/04/11', '2024/04/12')
dataset = a.cdaweb.Dataset('SOHO_ERNE-LED_L2-1MIN')
#'SOHO_COSTEP-EPHIN_L3I-1MIN')#'SOHO_CELIAS-SEM_15S')
result = Fido.search(trange, dataset)

print(result)

downloaded_files = Fido.fetch(result[0, 0:2])

print(downloaded_files)

solo_mag = TimeSeries(downloaded_files, concatenate=True)

print(solo_mag.columns)

#solo_mag.peek(columns=['B_RTN_0', 'B_RTN_1', 'B_RTN_2'])
