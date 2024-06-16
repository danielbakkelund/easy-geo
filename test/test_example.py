
import unittest as ut

import easy_geo as eg

import numpy as np
import numpy.linalg as npl
import numpy.testing as npt

class TestExample(ut.TestCase):

    def test_example(self):
        '''
        Run the example in the README.md
        '''
        lat1 = 69.845889
        lon1 = 19.991958

        lat2 = 69.844875
        lon2 = 20.045554

        # Set up a transformer with origin in (lat1,lon1)
        transformer = eg.Transformer(lat=lat1,lon=lon1, unit='m')

        # Compute the cartesian coords of the points
        c1 = transformer.from_latlon(lat1,lon1)
        c2 = transformer.from_latlon(lat2,lon2)

        npt.assert_allclose(c1, (0,0))

        # Compute their Euclidean distance in meters
        dist = npl.norm(c1-c2)

        # Should be about 2 kilometers
        self.assertEqual(np.round(dist), 2064)

    def test_example_km(self):
        '''
        Run the example in the README.md
        '''
        lat1 = 69.845889
        lon1 = 19.991958

        lat2 = 69.844875
        lon2 = 20.045554

        # Set up a transformer with origin in (lat1,lon1)
        transformer = eg.Transformer(lat=lat1,lon=lon1, unit='km')

        # Compute the cartesian coords of the points
        c1 = transformer.from_latlon(lat1,lon1)
        c2 = transformer.from_latlon(lat2,lon2)

        npt.assert_allclose(c1, (0,0))

        # Compute their Euclidean distance in meters
        dist = npl.norm(c1-c2)

        # Should be about 2 kilometers
        self.assertEqual(np.round(dist,1), 2.1)

    def test_outside_zone_strict(self):
        '''
        Run the example in the README.md
        '''
        lat1 = 69.845889
        lon1 = 19.991958

        # Set up a struct transformer with origin in (0,0)
        transformer = eg.Transformer(lat=0,lon=0, unit='m',strict=True)

        # Compute the cartesian coords of the points
        with self.assertRaises(ValueError) as context:
            transformer.from_latlon(lat1,lon1)
