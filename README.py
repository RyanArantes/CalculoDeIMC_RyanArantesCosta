# CalculoDeIMC_RyanArantesCosta
print("Seja Bem Vindo! Este é Uma Ferramenta Para Se Calcular o IMC, Desenvolvida Pelo Estudante Ryan Arantes Costa.")

valor01=float(input("Digite Seu Peso: "))

valor02=float(input("Digite Sua Altura: "))

valor3=valor02**2

imc=valor01/valor3

if imc<=10 or imc>=50:
   print(("Hm, Que Resultado Esquisito, Tem Certeza De Que Fez Corretamente?"))

elif imc<18.5:
    print("Seu IMC Atual é {}, o Que De Acordo Com a OMS, Você Está Abaixo Do Peso.".format(imc))

elif imc>=18.5 and imc<=24.9:
    print("Seu IMC Atual é {}, o Que De Acordo Com a OMS, Você Está Com o Peso Normal.".format(imc))

elif imc>=25 and imc<=29.9:
    print("Seu IMC Atual é {}, o Que De Acordo Com a OMS, Você Está Com Sobrepeso.".format(imc))

elif imc>=30 and imc<=50:
    print("Seu IMC Atual é {}, o Que De Acordo Com a OMS, Você Está Obeso.".format(imc))