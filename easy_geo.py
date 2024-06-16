
import numpy as np
import numpy.linalg as npl
import utm


def _get_logger(x):
    import logging
    return logging.getLogger(__name__ + '.' + x.__name__)


class Transformer:
    def __init__(self,lat,lon,unit='m',strict=True):
        '''
        lat - The zero latitude
        lon - The zero longitude
        unit - The length unit of the cartesian coordinates.
               Defaults to 'm' (meters). Supported units are: 'm', 'km'.
        '''

        self.log    = _get_logger(Transformer)
        self.strict = strict

        self.x0, self.y0, self.zone, self.ns = utm.from_latlon(lat,lon)

        self.origin = np.array((self.x0, self.y0))

        if unit == 'm':
            self.unit_converter = lambda x : x
        elif unit == 'km':
            self.unit_converter = lambda x : x/1000
        else:
            raise ValueError(f'Unknown unit: "{unit}".')

        self.log.debug('Created geo->utm projection in zone %s%s with origin=(%f,%f)',
                       self.zone, self.ns, self.x0, self.y0)


    def from_latlon(self,lat,lon):
        '''
        Transforms a geo location point on the form (lat,lon) to cartesian coordinates.
        Output is a numpy array of shape (2,).
        '''
        x,y,z,ns = utm.from_latlon(lat,lon)

        if z != self.zone or ns != self.ns:
            msg = f'({lat},{lon}) is outsize utm zone {self.zone}{self.ns}.'
            if self.strict:
                raise ValueError(msg)
            else:
                self.log.warning(msg)

        result = (x,y) - self.origin

        if np.any(np.isnan(result)):
            self.log.warning('nan coordinate %s for geo coordinates %s.',
                             tuple(result), tuple(lat,lon))

        return self.unit_converter(result)
