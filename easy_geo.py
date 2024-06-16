
import numpy as np
import numpy.linalg as npl
import utm


def _get_logger(x):
    import logging
    return logging.getLogger(__name__ + '.' + x.__name__)


class Transformer:
    def __init__(self,lat,lon,unit='m'):
        '''
        '''

        self.log    = _get_logger(Transformer)

        self.x0, self.y0, self.zone, self.ns = utm.from_latlon(lat,lon)

        self.origin = np.array((self.x0, self.y0))

        self.unit_converter = lambda x : x
        if unit == 'km':
            self.unit_converter = lambda x : x/1000

        self.log.debug('Created geo->utm projection in zone %s with n/s=%s and origin=(%f,%f)',
                       self.zone, self.ns, self.x0, self.y0)

    def to_cart(self,lat,lon):
        '''
        Transforms a geo location point on the form (lat,lon) to cartesian coordinates.
        Output is a numpy array of shape (2,).
        '''
        x,y,z,ns = utm.from_latlon(lat,lon)
        if z != self.zone or ns != self.ns:
            raise ValueErrpr(f'({lat},{lon}) is outsize utm zone {self.zone}{self.ns}.')

        result = (x,y) - self.origin

        if np.any(np.isnan(result)):
            self.log.warning('nan coordinate %s for geo coordinates %s.',
                             tuple(result), tuple(lat,lon))

        return self.unit_converter(result)
