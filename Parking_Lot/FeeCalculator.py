import math
from abc import ABC, abstractmethod
from Enum import SpotType


class FeeCalculator(ABC):
    @abstractmethod
    def calculate_fee(self, duration_hours, spot_type):
        pass


class HourlyFeeCalculator(FeeCalculator):
    RATE_PER_HOUR = {
        SpotType.SMALL: 10,
        SpotType.COMPACT: 20,
        SpotType.LARGE: 40,
    }

    def calculate_fee(self, duration_hours, spot_type):
        rate = self.RATE_PER_HOUR.get(spot_type, 20)
        return math.ceil(duration_hours) * rate
