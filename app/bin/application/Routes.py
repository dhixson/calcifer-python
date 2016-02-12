class Routes:
    """Class to control routing"""

    def __init__(self):
        """Initialize route map"""
        self.mapping = {
            'GET': {},
            'POST': {},
            'PUT': {},
            'DELETE': {}
        }

    def add(self, method, path, func, param=False):
        """Store new route to route mapping"""
        if param:
            self.mapping[method][path] = {'param': func}
        else:
            self.mapping[method][path] = func

    def get(self, path, func, param=False):
        self.add('GET', path, func, param)

    def post(self, path, func, param=False):
        self.add('POST', path, func, param)

    def put(self, path, func, param=False):
        self.add('PUT', path, func, param)

    def delete(self, path, func, param=False):
        self.add('DELETE', path, func, param)
