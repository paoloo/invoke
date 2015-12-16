# invoke
Pequeno utilitario para testar rapidamente a carga e o comportamento dos shared objects no ctypes.

Exemplos:

$ python invoke.py /lib/x86_64-linux-gnu/libc.so.6 printf "oi, hoje é " `date +%A` ". Vai dormir!"
oi, hoje é terça. Vai dormir!
function "printf" from "/lib/x86_64-linux-gnu/libc.so.6" returned "31"

$ python invoke.py ./libmotor getPIDgain 1 1
ganho do motor 1: 0.685493
function "getPIDgain" from "./libmotor" returned "0"


Falta adicionar tipos no retorno e nos parametros, para evitar resultado anomalos no caso de strings returnadas e qualquer coisa não-numerica, mas este utilitario foi feita para testar saidas numericas de bibliotecas de motores, ganhos, e controle em geral.
