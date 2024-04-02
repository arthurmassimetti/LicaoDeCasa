Para começar, o Selenium é uma biblioteca de Python que usa elementos de paginas ou partes de algum site para analisar e fazer movimentos definidos pelo DEV
Como funciona?:
para usar o Selenium é preciso fazer a inspeção da pagina, usando f12 ou inspecionar, você pode tanto como usar elementos do CSS, Xpath, Full Xpath entre outros
ele usurfrui dos elementos diretamente na pagina, podem ser modificados e torna-los unicos na pagina, por exemplo: 
Full Xpath: /html/body/div[1]/div[1]/header/div[2]/nav/ul/li[7]/a/svg
isso pode ser mudado, se você analisar o codigo que foi dado, ele vai entrando cada vez mais dentro do codigo por partes
por body, divs, spains, headers entre outros...
você pode clicar, usando o .click()
pode escrever usando o selenium.write("oque será escrito")
ou então pode interagir com links ou documentos

o Selenium possui diversos recursos para interação em pagina, possibilitando que o usuario faça oque quiser dentro da pagina, desde
teste de clicks, até inserção de dados em grande escala

por ser uma biblioteca em Python, é necessario fazer a instalação da biblioteca, utilizando o pip install selenium, ou para usuarios linux
pip3 install selenium

sabendo usar e criar, você pode criar sistemas automaticos de preenchimento, pode criar processos automaticos para sites abertos na internet

vale lembrar: você não irá conseguir utilizar o Selenium para sites hospedados em maquinas virtuais, já que impossibilita a inspeção de
elementos da pagina, mas para tudo há um jeito, você pode utilizar tanto como a plataforma UiPath para criar seus proprios elementos
ou então você pode utilizar o PyAutoGUI, que é uma biblioteca para interação de mouse, podendo utilizar cores, coordenadas de tela, é utilizado
totalmente por coordenadas, você indica onde será feito o click e a partir disso você utiliza o biblioteca inteira

Portanto, o Selenium é uma biblioteca que utiliza obrigatoriamente elementos de inspeção da pagina
