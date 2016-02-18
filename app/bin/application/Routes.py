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
        if path in self.mapping[method]:
            if param:
                self.mapping[method][path]['param'] = func
            else:
                self.mapping[method][path]['no_param'] = func
        else:
            if param:
                self.mapping[method][path] = {'param': func}
            else:
                self.mapping[method][path] = {'no_param': func}

    def get(self, path, func, param=False):
        """store get route"""
        self.add('GET', path, func, param)

    def post(self, path, func, param=False):
        """store post route"""
        self.add('POST', path, func, param)

    def put(self, path, func, param=False):
        """store put route"""
        self.add('PUT', path, func, param)

    def delete(self, path, func, param=False):
        """store delete route"""
        self.add('DELETE', path, func, param)

    def restful(self, path, ctrl):
        """create all CRUD routes for path"""
        self.get(path, ctrl.list)
        self.get(path, ctrl.show, True)
        self.post(path, ctrl.create)
        self.put(path, ctrl.update, True)
        self.delete(path, ctrl.delete, True)
