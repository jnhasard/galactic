class Mercader:
    def __init__(self):
        self.mapper = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        self.units = {}
        self.credits = {}
        self.error_msj = 'I have no idea what you are talking about'

    def roman_decoder(self, roman):
        integer = 0
        i = 0
        while i < len(roman):
            if len(roman) - i >= 2 and self.mapper[roman[i]] < self.mapper[roman[i + 1]]:
                integer += self.mapper[roman[i + 1]] - self.mapper[roman[i]]
                i += 1
            else:
                integer += self.mapper[roman[i]]
            i += 1
        return integer

    def instruction_decoder(self, instruction):
        instruction = instruction.split()
        if instruction[1] == 'is':
            return self.add_symbol(instruction)
        elif instruction[-1] == 'Credits':
            return self.add_conversion(instruction)
        elif instruction[1] == 'much':
            return ' '.join(instruction[3:-1]) + ' is ' + str(self.convert_units(instruction[3:-1]))
        elif instruction[1] == 'many':
            return ' '.join(instruction[4:-2]) + ' is ' + str(self.convert_credits(instruction)) + ' Galactic Credits'
        return self.error_msj

    def add_symbol(self, instruction):
        if instruction[2] in self.mapper:
            self.units[instruction[0]] = instruction[2]
            return instruction[0] + ' is ' + instruction[2] + ' in Roman Numbers'
        else:
            print(self.error_msj)

    def add_conversion(self, instruction):
        credit = int(instruction[-2])
        amount = self.convert_units(instruction[:-4])
        self.credits[instruction[-4]] = credit / amount
        return 'One ' + instruction[-4] + ' is ' + str(credit / amount) + ' Galactic Credits'

    def convert_units(self, instruction):
        roman = ''
        for unit in instruction:
            roman += self.units[unit]
        return self.roman_decoder(roman)

    def convert_credits(self, instruction):
        credit = instruction[-2]
        amount = self.convert_units(instruction[4:-2])
        return self.credits[credit] * amount


# s = Mercader()
# inp = '''glob is I
# prok is V
# pish is X
# tegj is L
# glob glob Silver is 34 Credits
# glob prok Gold is 57800 Credits
# pish pish Iron is 3910 Credits
# How much is pish tegj glob glob ?
# how many Credits is glob prok Silver ?
# how many Credits is glob prok Gold ?
# how many Credits is glob prok Iron ?
# how much wood could a wood?'''
# inp = inp.split('\n')
# for i in inp:
#     print(s.instruction_decoder(i))
