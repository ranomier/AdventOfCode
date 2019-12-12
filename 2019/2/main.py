#!/usr/bin/env python3
import sys

def print_csl(list_obj):
    print(str(list_obj).strip("[]").replace(" ", ""))

class ParseOpCode(object):
    def __init__(self, input_file, ):
        # load input_file=il
        if type(input_file) is str:
            with open(input_file, "r") as file_fd:
                self.il = list(map(int, file_fd.read().strip("\n").split(",")))
        elif type(input_file) is list:
            self.il = input_file
        self.__consume = 0
        self.__reset = self.il.copy()
        print_csl(self.il)

    def add(self, op_code, pos1, pos2, pos_write):
        self.il[pos_write] = self.il[pos1] + self.il[pos2]
        self.__consume = 3

    def multiply(self, op_code, pos1, pos2, pos_write):
        self.il[pos_write] = self.il[pos1] * self.il[pos2]
        self.__consume = 3

    def calculate(self):
        for pos in range(len(self.il)):
            try:
                op_code_set = self.il[pos], self.il[pos + 1], self.il[pos + 2], self.il[pos + 3]
            except:
                break
            if self.__consume:
                self.__consume -= 1
                pos += 1
                continue
            elif op_code_set[0] == 1:
                self.add(*op_code_set)
            elif op_code_set[0] == 2:
                self.multiply(*op_code_set)
            elif op_code_set[0] == 99:
                return self.il
            else:
                raise SyntaxError("your opcode is bad: " + str(op_code_set))
            pos += 1
        return self.il
    
    def set_values(self, dict_var):
        for i, j in dict_var.items():
            self.il[i] = j

    def reset(self):
        self.il = self.__reset.copy()

    def part_1(self):
        self.set_values({1: 12, 2: 2})
        return self.calculate()
    

    def part_2(self, seek):
        for i in range(100):
            for j in range(100):
                self.reset()
                self.set_values({1: i, 2: j})
                result = self.calculate()[0]
                print(result)
                if result == seek:
                    print(i, j)
                    return i, j


            


if __name__ == "__main__":
    #aoc_input = ParseOpCode("./input")
    #print_csl(aoc_input.calculate())
    bla = ParseOpCode("./input")
    print(bla.part_2(19690720))
