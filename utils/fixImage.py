def fixImage(self, name, path):
    """
        this function fix image if not found
        parameters:
            self: is a target object
            name: the name of property of object
            path: the path for default image you want
        return: None
    """
    if not getattr(self, name):
        setattr(self, name, {})
        eval(f'self.{name}')['url'] = path