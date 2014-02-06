class Employee(object):
    def __init__(self, name):
        self._name = name # Store the name of the employee
        self._rate = 25

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_hours(self):
        return 40 # A standard employee works 40 hours a week

    def get_rate(self):
        return self._rate

    def get_vac_days(self):
        return 5

    def get_annual_pay(self):
        return self.get_rate() * self.get_hours() * (52 - self.get_vac_days() / 5.0)
