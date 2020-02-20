from BaseAgent import BaseAgent as base_agent


class CompoundAgent(base_agent):
    def __init__(self, policy, children):
        super().__init__(policy)
        assert isinstance(children, list) and len(children) > 0
        self._children = children
        