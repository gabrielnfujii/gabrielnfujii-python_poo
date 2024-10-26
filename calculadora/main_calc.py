from calculadora import *

if __name__ == "__main__":
   calc = Calculadora()

   print(f'>>{calc.resultado}')
   op = input(">> ")

   while op != 'q':
       if op == '+' or op == '-':
           n = float(input(">> "))
           if op == '+':
               o = Adicao(n)
           if op == '-':
               o = Subtracao(n)
           calc.add_operacao(o)
       elif op == '/' or op == '*':
           n = float(input(">> "))
           if op == '/':
               o = Divisao(n)
           elif op == '*':
               o = Multiplicao(n)
               calc.add_operacao(o)
       elif op == '=':
           calc.calcular_total()
           print(f'>> {calc.resultado}')
       elif op == 'z':
            calc.desfazer_ultima()
            print(f'>> {calc.resultado}')

       op = input(">> ")



   # print(a1.calcular(2))
    #print(a1.calcular_inverso(2))

   # print(s1.calcular(2))
    #print(s1.calcular_inverso(2))
