import pyproj

def GR_to_NE( gr ):
	gr = gr.strip().replace( ' ', '' )
	if len(gr) == 0 or len(gr) % 2 == 1 or len(gr) > 12:
	    return None, None

	gr = gr.upper()
	if gr[0] not in 'STNOH' or gr[1] == 'I' :
		return None, None

	e = n = 0
	c = gr[0]

	if c == 'T' :
		e = 500000
	elif c == 'N' :
		n = 500000
	elif c == 'O' :
		e = 500000
		n = 500000
	elif c == 'H':
		n = 10000000

	c = ord(gr[1]) - 66
	if c < 8: # J
	    c += 1;

	e += (c % 5) * 100000;
	n += (4 - c/5) * 100000;

	c = gr[2:]
	try :
	    s = c[:len(c)/2]
	    while len(s) < 5 :
	    	s += '0'

	    e += int( s )

	    s = c[-len(c)/2:]
	    while len(s) < 5 :
	    	s += '0';

	    n += int( s )

	except Exception:
	    return None,None;

	return e,n

def get_ne_lat_long( grid ):
    e,n = GR_to_NE( grid )
    bng = pyproj.Proj(init='epsg:27700')
    wgs84 = pyproj.Proj(init='epsg:4326')
    lon,lat = pyproj.transform(bng,wgs84, e, n)
    return e,n,lon,lat
