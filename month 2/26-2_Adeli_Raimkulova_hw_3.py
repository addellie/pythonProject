class Computer:
    def __init__(self, cpu, memory):
        if isinstance(memory, int):
            self.__cpu = cpu
            self.__memory = memory

    @property
    def cpu(self):
        return self.__cpu

    @cpu.setter
    def cpu(self, value):
        self.__cpu = value

    @property
    def memory(self):
        return self.__memory

    @memory.setter
    def memory(self, value):
        self.__memory = value

    def make_computations(self):
        return f'sum: {self.cpu + self.memory}, diff: {self.cpu - self.memory}'

    def __gt__(self, other):
        return self.memory > other.memory

    def __lt__(self, other):
        return self.memory < other.memory

    def __eq__(self, other):
        return self.memory == other.memory

    def __neg__(self):
        return self.memory != other.memory

    def __str__(self):
        return f'cpu: {self.__cpu}, memory: {self.__memory}'


class Phone:
    def __init__(self, sim_cards_list):
        self.__sim_cards_list = sim_cards_list

    @property
    def sim_cards_list(self):
        return ['Beeline', 'O!']

    @sim_cards_list.setter
    def sim_cards_list(self, value):
        self.__sim_cards_list = value

    def call(self, sim_card_number, call_to_number):
        if sim_card_number == 1:
            return f'Идет звонок на номер {call_to_number} с сим-карты-{sim_card_number}: {self.sim_cards_list[0]}'
        elif sim_card_number == 2:
            return f'Идет звонок на номер {call_to_number} с сим-карты-{sim_card_number}: {self.sim_cards_list[1]}'

    def __str__(self):
        return f"phone's sim cards: {self.__sim_cards_list}"


class SmartPhone(Computer, Phone):
    def __init__(self, cpu, memory, sim_cards_list):
        Computer.__init__(self, cpu, memory)
        Phone.__init__(self, sim_cards_list)

    def use_gps(self, location):
        self.location = location
        return f'Маршрут до {location} проложен!'

    def __str__(self):
        return super().__str__() + f' sim cards: {self.sim_cards_list}'


computer = Computer(2, 1000)
print(computer)
print(computer.make_computations())

phone1 = Phone('MegaCom')
print(phone1)

my_smart_phone = SmartPhone(12, 129, 2)
print(my_smart_phone)
print(my_smart_phone.call(2, 1234324))
print(my_smart_phone.use_gps('Moscow'))

your_smart_phone = SmartPhone(16, 562, 2)
print(your_smart_phone)
print(your_smart_phone.call(1, 1348927439))
print(your_smart_phone.use_gps('St. Peterburg'))

print(f'My smartphone is better than yours {my_smart_phone.memory > your_smart_phone.memory}')
print(f'My smartphone is better than yours {my_smart_phone.memory < your_smart_phone.memory}')
print(f'My smartphone is better than yours {my_smart_phone.memory == your_smart_phone.memory}')
print(f'My smartphone is better than yours {my_smart_phone.memory != your_smart_phone.memory}')
