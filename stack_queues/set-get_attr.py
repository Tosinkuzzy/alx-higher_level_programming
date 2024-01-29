#!/usr/bin/python3
class Robot:
    def __init__(self, name, build_year, city):
        self.name = name
        self.build_year = build_year
        self.city = city
    def __getattr__(self, name):
        return self.__dict__[f"__{name}"]
    def __setattr__(self, name, value):
        if name == 'name':
            if value in ['Henry', 'Tosinkuzzy']:
                raise ValueError('Not a decent robot name')
            elif name == 'build_year':
                if int(value) < 2024:
                    raise ValueError('Build year has to be after 2024')
            self.__dict_-[f"__{name}"] = value

robot = Robot("Marvin", 2024, "TechCity")
print(robot.name)
print(robot.build_year)
print(robot.city)

