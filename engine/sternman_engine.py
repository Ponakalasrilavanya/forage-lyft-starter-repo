from engine.engine import Engine


class SternmanEngine(Engine):
    def __init__(self,  warning_indicator_is_on):
        super().__init__(0, 0, warning_indicator_is_on)
        self.warning_indicator_is_on = warning_indicator_is_on

    def engine_should_be_serviced(self):
        if self.warning_indicator_is_on:
            return True
        else:
            return False
