class MooreAutomaton:
    def __init__(self):
        self.state = "q0"  # Estado inicial

    def transition(self, bit):
        if self.state == "q0":
            if bit == "0":
                output = "0"
                self.state = "q0"
            elif bit == "1":
                output = "0"
                self.state = "q1"
        elif self.state == "q1":
            if bit == "0":
                output = "0"
                self.state = "q0"
            elif bit == "1":
                output = "00"
                self.state = "q0"
        return output

    def process_input(self, input_string):
        output_string = ""
        for bit in input_string:
            output_string += self.transition(bit)
        return output_string

# Ejemplo de uso
automaton = MooreAutomaton()
input_data = "1101101"  # Ejemplo de entrada
output_data = automaton.process_input(input_data)
print(f"Entrada: {input_data}")
print(f"Salida: {output_data}")
