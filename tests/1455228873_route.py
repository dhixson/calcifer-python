"""Run tests for routes."""
import os
import sys
import unittest
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)).strip('tests'))
from app.bin.application.Routes import Routes
from app.controllers.TestController import TestController


class Testroute(unittest.TestCase):
    """Class to test routes."""

    def test_init(self):
        """Test that route class is callable."""
        routes = Routes()
        self.assertIsInstance(routes, Routes)

    def test_map_init(self):
        """Test that a route map is created."""
        routes = Routes()
        testDict = {
            'GET': {},
            'POST': {},
            'PUT': {},
            'DELETE': {}
        }
        self.assertEqual(routes.mapping, testDict)

    def test_single_route_get_no_param(self):
        """Test that a single get route can be saved."""
        route = Routes()
        route.get('/home', lambda: 8**2)
        self.assertEqual(route.mapping['GET']['/home']['no_param'](), 64)

    def test_single_route_post_no_param(self):
        """Test that a single post route can be saved."""
        route = Routes()
        route.post('/home', lambda: 8**2)
        self.assertEqual(route.mapping['POST']['/home']['no_param'](), 64)

    def test_single_route_put_no_param(self):
        """Test that a single put route can be saved."""
        route = Routes()
        route.put('/home', lambda: 8**2)
        self.assertEqual(route.mapping['PUT']['/home']['no_param'](), 64)

    def test_single_route_delete_no_param(self):
        """Test that a single delete route can be saved."""
        route = Routes()
        route.delete('/home', lambda: 8**2)
        self.assertEqual(route.mapping['DELETE']['/home']['no_param'](), 64)

    def test_single_route_get_param(self):
        """Test that a single get route with param can be saved."""
        route = Routes()
        route.get('/home', lambda x: x**2, True)
        self.assertEqual(route.mapping['GET']['/home']['param'](8), 64)

    def test_single_route_post_param(self):
        """Test that a single post route with param can be saved."""
        route = Routes()
        route.post('/home', lambda x: x**2, True)
        self.assertEqual(route.mapping['POST']['/home']['param'](8), 64)

    def test_single_route_put_param(self):
        """Test that a single put route with param can be saved."""
        route = Routes()
        route.put('/home', lambda x: x**2, True)
        self.assertEqual(route.mapping['PUT']['/home']['param'](8), 64)

    def test_single_route_delete_param(self):
        """Test that a single delete route with param can be saved."""
        route = Routes()
        route.delete('/home', lambda x: x**2, True)
        self.assertEqual(route.mapping['DELETE']['/home']['param'](8), 64)

    def test_resource_route(self):
        """Test that a resource rout creates all routes for resource."""
        route = Routes()
        route.restful('/home', TestController)
        self.assertEqual(route.mapping['GET']['/home']['no_param'](), 64)
        self.assertEqual(route.mapping['GET']['/home']['param'](8), 64)
        self.assertEqual(route.mapping['POST']['/home']['no_param'](), 64)
        self.assertEqual(route.mapping['PUT']['/home']['param'](8), 64)
        self.assertEqual(route.mapping['DELETE']['/home']['param'](8), 64)


if __name__ == '__main__':
    unittest.main()
