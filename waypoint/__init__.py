class Waypoint(object):
    def __init__(self,name,code,country,lat,long,elevation
                ,style=31,rwdir='',rwlen='',freq='',desc='""'):
        self._name      = '"'+name+'"'
        self._code      = '"'+code+'"'
        self._country   = country
        self._latitude  = lat
        self._longitude = long
        self._elevation = "{:010.5f}m".format(elevation)
        self._style     = str(style)
        self._rwdir     = str(rwdir)
        self._rwlen     = str(rwlen)
        self._freq      = str(freq)
        self._desc      = str(desc)

    @staticmethod
    def header():
        return ("Nome,Codigo,Pais,Latitude,Longitude,Elevacao,style,"
               +"rwdir,rwlen,freq,desc")

    def __str__(self):
        fields = (
            self._name, self._code, self._country, self._latitude,
            self._longitude, self._elevation, self._style, self._rwdir,
            self._rwlen, self._freq, self._desc
        )

        return ','.join(fields)

name   = "T%04i" % 1
lat    = "1937.835S"
long   = "04057.348W"
height = 794.44482

wp = Waypoint(name,name,'',lat,long,height)

print wp
