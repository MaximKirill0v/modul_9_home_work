class UnitConverter:

    @staticmethod
    def millimeters_to_inches(millimeters: float):
        return millimeters * 0.0394

    @staticmethod
    def inches_to_millimeters(inches: float):
        return inches * 25.4

    @staticmethod
    def meters_to_foot(meters: float):
        return meters * 3.281

    @staticmethod
    def foot_to_meters(foot: float):
        return foot * 0.305

    @staticmethod
    def kilograms_to_lb(kilograms: float):
        return kilograms * 2.205

    @staticmethod
    def lb_to_kilograms(lb: float):
        return lb * 0.454
