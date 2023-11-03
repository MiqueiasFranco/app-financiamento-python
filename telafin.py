import PySimpleGUI as sg

sg.theme('DarkAmber')
layout = [
    [sg.Text('FAÇA SEU FINANCIAMENTO!')],
    [sg.Text('SALÁRIO ATUAL R$'), sg.InputText(key="salario")],
    [sg.Text('VALOR DO IMÓVEL R$'), sg.InputText(key="valor")],
    [sg.Text('PRAZO :'), sg.InputText(key="prazo")],
    [sg.Button("calcular"), sg.Button('cancel')],
    [sg.Text("", key="texto_resultado")],
]

window = sg.Window('CONSTRUTORA MK', layout)
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'cancel':
        break

    elif event == "calcular":
        salario = int(values["salario"])
        imovel = int(values['valor'])
        prazo = int(values['prazo'])
        calculoPerc = salario * 30 / 100
        calculoParcelas = imovel / (prazo * 12)
        if calculoParcelas > calculoPerc:
            window["texto_resultado"].update("não autorizado...valor do imóvel incompativel com o salário")

        elif calculoParcelas < calculoPerc:
            window["texto_resultado"].update(
                f"Parabéns... suas parcelas serão de {calculoParcelas:.2f} durante {prazo} anos !!")

        else:

            window["texto_resultado"].update("Escolha uma opção válida")


    continue
window.close()
