#!/usr/bin/env python
def CalculaCPF(cpf):

    parte1=((int(cpf[0]))*10)+\
           ((int(cpf[1]))*9)+\
           ((int(cpf[2]))*8) + \
           ((int(cpf[3]))*7) + \
           ((int(cpf[4]))*6) + \
           ((int(cpf[5]))*5) + \
           ((int(cpf[6]))*4) + \
           ((int(cpf[7]))*3) + \
           ((int(cpf[8]))*2)

    resto1 = (parte1 - ((int(parte1 / 11) * 11)))

    if (resto1 < 2):
        primeiroDigito =0
    else:
        primeiroDigito =(11 - resto1)

    cpf = str(cpf) + str(primeiroDigito)

    parte2 = (int(cpf[0] ) *11 )+ \
             (int(cpf[1] ) *10 )+ \
             (int(cpf[2] ) *9 )+ \
             (int(cpf[3] ) *8 )+ \
             (int(cpf[4] ) *7 )+ \
             (int(cpf[5] ) *6 )+ \
             (int(cpf[6] ) *5 )+ \
             (int(cpf[7] ) *4 )+ \
             (int(cpf[8] ) *3 )+ \
             (int(cpf[9] ) *2)

    resto2 = (parte2 - ((int(parte2 / 11) * 11)))
    if (resto2 < 2):
        segundoDigito = 0
    else:
        segundoDigito = (11 - resto2)

    cpf = str(cpf) + str(segundoDigito)
    return(cpf)
