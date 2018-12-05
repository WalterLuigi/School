class Room(object):

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.paths = {}
        self.actions = {}

    def go(self, direction):
        return self.paths.get(direction, None)

    def go_conditional(self, direction, paths):
        if self.actions['hit']:
            self.add_paths(paths)
        return self.paths.get(direction, None)

    def add_paths(self, paths):
        self.paths.update(paths)

    def add_actions(self, actions):
        self.actions.update(actions)