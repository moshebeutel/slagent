import BaseAgent

class CompoundAgent(BaseAgent):
    def __init__(self, policy, children):
        super().__init__(policy)
        assert isinstance(children, list) and len(children) > 0
        self._children = children
        