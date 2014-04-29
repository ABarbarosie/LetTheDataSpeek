from pyGoogleTrendsCsvDownloader import pyGoogleTrendsCsvDownloader
r = pyGoogleTrendsCsvDownloader('letthedataspeak', 'Ilovemagic!')
r.get_csv(cat='0-958', geo='US-ME-500')