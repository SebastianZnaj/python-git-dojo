class GittieHelper:

    def __init__(self):
        """
        Initialize attributes with default value
        """
        self.temperature_degree = None
        self.humidity_value = None


    def set_temperature(self, temperature_degree):
        """
        Method sets temperature to attribute and validate input
        :param temperature_degree:
        """
        return temperature_degree

    def set_humidity(self, humidity_value):
        """
        Method sets humidity level to attribute and validate input
        :param humidity_value:
        """
        self.humidity_value = humidity_value
        return humidity_value

    def set_air_pollution(self, air_pollution_level):
        """
        Method sets air pollution level to attribute and validate input
        :param air_pollution_level:
        """
        pass

    def set_day_of_the_year(self, day_number):
        """
        Method sets day number from beginning of the year to attribute and validate input
        :param day_number:
        """
        pass

    def get_value_better(self):
        """
        Method should calculate if exiting home is safe for gittie
        :param:
        """
        pass
