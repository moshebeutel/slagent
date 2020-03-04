from Action import Action as Action

class TimedAction(Action):
    
    def __init__(self, name, world, average_duration = 10000, std_duration = 0, ):
        super().__init__(name, world)
        self._avg_duration = average_duration
        self._std_duration = std_duration
        
    