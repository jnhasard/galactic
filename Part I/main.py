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
        self.error_msj = 'I have no idea what you are talking about!'

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
        if len(instruction) < 3:
            return self.error_msj
        if instruction[1] == 'is':
            self.add_symbol(instruction)
        elif instruction[-1] == 'Credits':
            self.add_conversion(instruction)
        elif instruction[1] == 'much':
            result = str(self.convert_units(instruction[3:-1]))
            if result != self.error_msj:
                return ' '.join(instruction[3:-1]) + ' is ' + result
            return self.error_msj
        elif instruction[1] == 'many':
            result = str(self.convert_credits(instruction))
            if result != self.error_msj:
                return ' '.join(instruction[4:-1]) + ' is ' + result + ' Galactic Credits'
            return self.error_msj

    def add_symbol(self, instruction):
        if instruction[2] in self.mapper:
            self.units[instruction[0]] = instruction[2]
        else:
            print(self.error_msj)

    def add_conversion(self, instruction):
        if len(instruction) < 4:
            return self.error_msj
        credit = int(instruction[-2])
        amount = self.convert_units(instruction[:-4])
        self.credits[instruction[-4]] = credit / amount

    def convert_units(self, instruction):
        roman = ''
        for unit in instruction:
            if unit not in self.units:
                return self.error_msj
            roman += self.units[unit]
        return self.roman_decoder(roman)

    def convert_credits(self, instruction):
        if len(instruction) < 4:
            return self.error_msj
        credit = instruction[-2]
        if credit not in self.credits:
            return self.error_msj
        amount = self.convert_units(instruction[4:-2])
        return self.credits[credit] * amount


txt_file = open('input.txt', 'r')
txt_out = open('output.txt', 'w')
salesman = Mercader()
for i in txt_file.readlines():
    out = salesman.instruction_decoder(i.strip('\n'))
    if out:
        txt_out.write(out + "\n")
txt_file.close()
txt_out.close()
