def fixImage(parent, self, name, path):
    """
        this function fix image if not found
        parameters:
            parent: the main class
            self: is a target object
            name: the name of property of object
            path: the path for default image you want
        return: None
    """
    if not getattr(self, name):
        image = {
            name: path
        }
        # here will update image in db but will not update in memory
        parent.objects.filter(id=self.id).update(**image)
        # update object in memory
        setattr(self, name, {
            'url': f'/media/{path}'
        })
        
        
