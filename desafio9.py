#Elabore um programa que calcule o valor a ser pago por um produto
#Considerando que o seu preço normal e condição de pagamento:

# Á vista dinheiro/cheque: 10% de desconto
# Á vista no cartão: 5% de desconto 
# Em até 2x no cartão: Preço normal
#3x ou mais no cartão: 20% de juros 

#Entrada do usuário
preco_normal = float (input ('Digite o preço normal do produto: R$'))
print('''Formas de pagamento: 
[1] Á vista dinheiro/cheque 
[2] Á vista no cartão
[3] Em até 2x no cartão 
[4] 3x ou mais no cartão''')
opcao = int (input('Digite a opção de pagamento:'))

#Calcula o valor a ser pago

if opcao == 1:
    valor_final = preco_normal * 0.90 #10 % de desconto
elif opcao == 2:
    valor_final = preco_normal *0.95 #5% de desconto
elif opcao == 3:
    valor_final = preco_normal #preço normal
elif opcao == 4:
    parcelas = input('Quantas parcelas?')
    if parcelas >= 3:
        valor_final = preco_normal * 1.20 # 20% de juros
    else:
        valor_final = preco_normal
        valor_parcela = valor_final / parcelas
        print('Sua compra será parcela em{}x de R${:.2f} com juros'.format())
else:
    valor_final = preco_normal
    print('Opção inválida de pagamento !')

#Exibe o valor final a ser pago
print('O valor final a ser pago é R${:.2f}'.format(valor_final))
