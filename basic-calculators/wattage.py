from batterypack import get_usable_battery

"""
    Basic calculation for single device is:

        Wh = W * h
        Amps = Wh / 12

    Where:
        W is Watt
        h is Hour

    It outputs Wh required for each device to operate per day
    Sum this up for all devices and you get the resulting Wh/day

    Make sure h <= 24
"""

devices = [
    {
        'name': 'Macbook - internet',
        'watt': 50
    },
    {
        'name': 'Macbook - intense',
        'watt': 100
    },
    {
        'name': 'Kettle',
        'watt': 2000
    },
    {
        'name': 'Microwave',
        'watt': 1000
    },
    {
        'name': 'Router',
        'watt': 10
    }
]

class WattageCalculator:
    def __init__(self, items):
        self.items = items
        self.usage = []

    def generate_options(self):
        output = ''

        for i, item in enumerate(self.items):
            output += "[%s] %s\n" % (i, item.get('name'))

        return output

    def add_usage(self, i, hours):
        #Calculation: Wh = W * h
        self.usage.append(self.items[i].get('watt') * hours)

    def total_usage(self):
        return sum(self.usage)

def list_devices(calc):
    print('Please Select one of the following options:')
    print(calc.generate_options())
    print('Or type x to cancel and get result')

def offer_input(calc):
    list_devices(calc)
    item = input()
    if item == 'x':
        total_usage = calc.total_usage()
        print("Watts/Day: %s" % total_usage)
        amps = total_usage / 12
        print("Amps in 12 volt system: %s" % amps)
        usable_batt = get_usable_battery(amps)
        print("Usable battery at least: %s Amps" % usable_batt)
        #let's assume we get direct sunlight for 8 hours
        required_hourly_charge = usable_batt / 8
        print("In sunny day (8 hours of direct sunlight) we require panels that perform: %s amps/h" % required_hourly_charge)
        #r / pe * v
        # Where:
        # r = Required Hourly charge
        # pe = Panel efficiency (usually 85% in direct sunlight)
        # v = Voltage system
        print("It means that we need at least %s Watt panels" % (required_hourly_charge / 0.85 * 12))
    else:
        hours = float(input('How many hours per day? '))
        item = int(item)

        calc.add_usage(item, hours)

        offer_input(calc)


calculator = WattageCalculator(devices)
offer_input(calculator)
