import sys,requests
import plugins as pl
url = str(sys.argv[1])
title = pl.get_title(url)
id = url.split('v=')
pl.dv(id[1])
pl.webp_to_jpg('./video/{id}.webp','./video/{id}.jpg')
