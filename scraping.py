from selenium import webdriver
from selenium.webdriver.chrome.options import Options  
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import csv
import re
import time
import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from seleniumwire import webdriver as wiredriver
from selenium.webdriver.chrome.service import Service as ChromeService


TIMER_SLEEP = 2
# Configurações do Chrome
chrome_options = Options()
# Descomente a linha abaixo se você quiser executar o Chrome em modo headless (sem interface gráfica)
# chrome_options.add_argument("--headless")

# Configurações do Selenium Wire
# proxy_address = 'https://179.83.82.10'  # Substitua pelo endereço do seu proxy
# seleniumwire_options = {
#     'backend': 'seleniumwire',
#     'proxy': {
#         'http': proxy_address,
#         'https': proxy_address,
#         'no_proxy': 'localhost,127.0.0.1',  # Domínios que devem ser acessados diretamente sem usar o proxy
#     }
# }


# # # Configuração do serviço do ChromeDriver
# # service = webdriver.chrome.service.Service('chromedriver.exe')

# # # Inicialize o driver do Chrome com as opções do Chrome e do Selenium Wire
# driver = wiredriver.Chrome(service=service, chrome_options=chrome_options, seleniumwire_options=seleniumwire_options)

# # Inicialize o servidor proxy do Selenium Wire
# proxy = driver.request_interceptor


# # Abra a página de login
# url = 'https://sales.ticketsforfun.com.br/#/authentication/login'
# driver.get(url)
# # Defina a função JavaScript a ser executada no navegador
# js_script = """
# function interceptXHR() {
#     console.log("Executando script");
#     try {
#         // Interceptar as requisições XHR
#         var originalOpen = window.XMLHttpRequest.prototype.open;
#         var originalSend = window.XMLHttpRequest.prototype.send;

#         window.XMLHttpRequest.prototype.open = function(method, url) {
#             // Salvar a URL da requisição para uso posterior
#             this._url = url;
#             originalOpen.apply(this, arguments);
#         };

#         window.XMLHttpRequest.prototype.send = function(data) {
#             // Verificar se a URL da requisição corresponde ao padrão desejado
#             if (this._url && this._url.startsWith('https://services.tix.byinti.com/neofront-v3/authentication/send-pin-code?')) {
                
#                 // Modificar a URL da requisição
#                 var modifiedUrl = this._url.replace('email=jalmirrosa6%40gmail.com', 'email=igorbzreis%40gmail.com');
                
#                 // Chamar o método originalOpen para aplicar a modificação
#                 originalOpen.call(this, 'GET', modifiedUrl, true);

#                 // Agora, chamar o método originalSend com os dados modificados
#                 originalSend.call(this, data);

#                 console.log("Requisição modificada e enviada:", modifiedUrl);
#             } else {
#                 // Se não for a requisição desejada, chamar o método originalSend sem modificação
#                 originalSend.call(this, data);
#             }
#         };
#     } catch (error) {
#         console.error('Erro na interceptação XHR:', error.message);
#     }
# }



# function addClickListenersToButtons() {
#     try {
#         // Adicionar um ouvinte de evento de clique a todos os botões
#         var buttons = document.querySelectorAll('button');
#         buttons.forEach(function(button) {
#             button.addEventListener('click', function(event) {
#                 console.log("Botão clicado! Texto do botão: " + event.target.innerText);
#                 // Chamar a função de interceptação de requisições ao clicar em um botão
#                 interceptXHR();
#             });
#         });
#     } catch (error) {
#         console.error('Erro ao adicionar ouvinte de evento de clique:', error.message);
#     }
# }

# // Executar a função de interceptação de requisições ao carregar a página
# interceptXHR();

# // Executar a função de adicionar ouvinte de evento de clique ao carregar a página
# addClickListenersToButtons();

# """


# # Execute o script JavaScript no navegador
# driver.execute_script(js_script)

# # Caminho do seu driver do Selenium (exemplo usando o Chrome)
# # Certifique-se de baixar o driver correspondente à sua versão do navegador

# # Aguarde alguns segundos para a página carregar completamente
# time.sleep(5)

# # Permita que o usuário interaja com a página
# input("Interaja com a página. Pressione Enter quando terminar.")

# # Fechar o navegador
# driver.quit()










# # Configuração do serviço do ChromeDriver
TIMER_SLEEP = 2
chrome_options = Options()
chrome_service = ChromeService(executable_path='chromedriver.exe')
chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--headless")
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

# 1° Acesse o link - 
url = "https://busca.inpi.gov.br/pePI/jsp/marcas/Pesquisa_num_processo.jsp"
driver.get(url)
wait = WebDriverWait(driver, 10)
continuar_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[contains(text(), 'Continuar...')]")))
continuar_link.click()
url = "https://busca.inpi.gov.br/pePI/jsp/marcas/Pesquisa_num_processo.jsp"
driver.get(url)
time.sleep(5)

# CODIGO QUE VAI SE REPETIR
def buscar_marca(num_pedido):
    print(f"Esperando {TIMER_SLEEP} segundos...")
    time.sleep(TIMER_SLEEP)
    num_processo = ""
    nome_marca = ""
    situacao = ""
    apresentacao = ""
    natureza = ""
    classificacao_nice = ""
    data_de_deposito = ""
    classificacao_de_viena = ""
    texto_do_despacho = ""
    
    url = "https://busca.inpi.gov.br/pePI/jsp/marcas/Pesquisa_num_processo.jsp"
    driver.get(url)

    try:
        # 2° Busque o input com name="NumPedido" e insira o código
        # num_pedido = "927361949"  # Substitua pelo número de pedido desejado
        input_num_pedido = driver.find_element(By.NAME, "NumPedido")
        input_num_pedido.send_keys(num_pedido)
        input_num_pedido.send_keys(Keys.RETURN)
    except Exception as e:
        print("823 - Erro ao procurar por processo - ", e)

    try:
        # Encontre o elemento <a> com o atributo href contendo "/pePI/servlet/MarcasServletController?Action=detail&amp"
        elemento_a = driver.find_element(By.XPATH,f"//a[contains(text(), '{num_pedido}')]")
        href = elemento_a.get_attribute("href")
        driver.get(href)
    except Exception as e:
        print("753 - Não encontrado na busca - ", e)

    try:
    # 4° Na página aberta, faça um crawler das informações da penúltima tabela
    # Aguarde até que a penúltima tabela seja visível
        tabelas = wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "table")))

        informacoes = {}
        # Localize os elementos <td> que contêm os rótulos
        rotulos = driver.find_elements(By.XPATH,"//td[contains(font, 'Nº do Processo:') or contains(font, 'Marca:') or contains(font, 'Situação:') or contains(font, 'Apresentação:') or contains(font, 'Natureza:') or contains(font, 'Apostila :')]")
        # Itere sobre os rótulos e capture os valores correspondentes
        for rotulo in rotulos:
            chave = rotulo.find_element(By.XPATH, "font").text.strip().replace(":", "")
            valor = rotulo.find_element(By.XPATH, "following-sibling::td/font").text.strip()
            informacoes[chave] = valor

        # Exiba as informações coletadas
        for chave, valor in informacoes.items():
            num_processo = informacoes['Nº do Processo']
            nome_marca = informacoes['Marca']
            situacao = informacoes['Situação']
            apresentacao = informacoes['Apresentação']
            natureza = informacoes['Natureza']

            # print(f"{chave}: {valor}")
    except Exception as e:
        print(f"423 - Erro ao coletar informações da tabela: {num_pedido} - ", e)

    # CAPTURAR CLASSIFICAÇÃO NICE
    try:
        class_nice = driver.find_element(By.XPATH, '//*[@id="principal"]/div[3]/div/div/table/tbody/tr/td[1]/font/a')
        classificacao_nice = class_nice.text
        # print("Classificacao NICE: ", class_nice.text)
    except Exception as e:
        print("831 - Erro ao capturar classificação NICE - ", e)

    #CAPTURAR A DATA DE DEPOSITO
    try:
       # Encontre a tabela com o elemento font que contém 'Data de Depósito'
        table_element = driver.find_element(By.XPATH, "//table[contains(.//font, 'Data de Depósito')]")

        # Em seguida, encontre o primeiro elemento th dentro do tbody
        th_element = table_element.find_element(By.XPATH, ".//tbody/tr/th[1]")

        # Capture o texto do primeiro th
        data_de_deposito = th_element.text
    except Exception as e:
        print("712 - Erro ao capturar data de deposito - ", e)

    # CAPTURAR CLASSIFICAÇÃO DE VIENA
    try:
        # Encontre a tabela usando o XPath especificado
        tabela = driver.find_element(By.XPATH, "//*[@id='principal']/div[4]/div/div/table")
        # Encontre todas as linhas da tabela dentro do corpo (elementos <tr>)
        linhas = tabela.find_elements(By.XPATH, ".//tbody/tr")
        # Itere sobre as linhas para obter os valores
        valores_totais = []
        for linha in linhas:
            # Encontre as colunas em cada linha (elementos <td>)
            colunas = linha.find_elements(By.XPATH, ".//td")
            # Obtenha os valores de cada coluna
            valores = [coluna.text for coluna in colunas]

            valores_totais.append(valores)
            # Faça algo com os valores, por exemplo, imprima-os
            # print("Classificacao de VIENA: ", valores)

        classificacao_de_viena = valores_totais
    except Exception as e:
        print("483 - Erro ao capturar classificação de VIENA - ", e)



    try:
        # Definir o padrão de regex
        padrao = r"A marca reproduz ou imita os seguintes registros de terceiros[^;]*"
        correspondencias = re.search(padrao, driver.page_source)
        if correspondencias:
            texto_do_despacho = correspondencias.group(0)
            # print("Texto completo: ", texto_do_despacho)
            
        else:
            print("Padrão não encontrado na página.")

    except Exception as e:
        print("9123 - Erro ao capturar detalhe do despacho:", e)

    try:
        #SALVANDO IMAGEM
        time.sleep(1)
        url = driver.current_url
        match = re.search(r'CodPedido=(\d+)', url)
        cod_pedido = ""
        if match:
            cod_pedido = match.group(1)
            # print("CodPedido:", cod_pedido)

        linkimg = f"https://busca.inpi.gov.br/pePI/servlet/LogoMarcasServletController?Action=image&codProcesso={cod_pedido}".split("/")[-1]
        
        elemento_img = driver.find_element(By.CSS_SELECTOR, f"img[src*='{linkimg}']")
        # print(elemento_img, linkimg)

        with open(f'imgs/imgs_revista/{num_pedido}.png', 'wb') as file:
            file.write(elemento_img.screenshot_as_png)
    except Exception as e:
        print(f"923 - Processo {cod_pedido} sem imagem ")


    return num_processo, nome_marca, situacao, apresentacao, natureza, classificacao_nice, data_de_deposito, classificacao_de_viena, texto_do_despacho

cabecalho = [
                'N° Processo',
                'Marca Indeferida',
                'Situação',
                'Apresentação',
                'Natureza',
                'Classe de Nice',
                'Classificação de Viena',
                'Data de Deposito',



                'N° Processo',
                'Marca Registrada',
                'Situação',
                'Apresentação',
                'Natureza',
                'Classe de Nice',
                'Classificação de Viena',
                'Data de Deposito',


                'Despacho',
                'Revista',
                'Visual',
                'Escrita',
                'Fonética'
            ]

def processo_ja_existe(processo_indeferido, processo_deferido, nome_arquivo):
    with open(nome_arquivo, 'r', newline='', encoding='utf-8') as arquivo_csv:
        leitor = csv.reader(arquivo_csv, delimiter='\t')
        
        # Pula o cabeçalho
        next(leitor, None)
        
        # Verifica se o número do processo já existe nas colunas 1 e 9
        for linha in leitor:
            if linha[0] == processo_indeferido or linha[8] == processo_deferido:
                return True
    return False

for revista in os.listdir('revistas'):
    print(f"Analisando revista {revista}")

    total_analisado = 0
    dados = []

    try:
        with open(f'revistas/{revista}', newline='', encoding='utf-8') as arquivo_csv:
            leitor_csv = csv.reader(arquivo_csv, delimiter="\t")   
            next(leitor_csv) 
            for linha in leitor_csv:
                processo_indeferido = linha[1]

                texto_complementar = linha[3]
                numeros_de_processo = re.findall(r'Processo (\d+)', texto_complementar)
                print("Processo Indeferido: ", processo_indeferido, "Processos deferidos: ", numeros_de_processo)
                
                
                # busco pelo processo indeferido
                num_processo_in, nome_marca_in, situacao_in, apresentacao_in, natureza_in, classificacao_nice_in, data_de_deposito_in, classificacao_de_viena_in, texto_do_despacho_in = buscar_marca(processo_indeferido)
                print("Marca indeferida: ", num_processo_in, nome_marca_in, situacao_in, apresentacao_in, natureza_in, classificacao_nice_in, data_de_deposito_in, classificacao_de_viena_in )
                # agora busco pelos processo deferido (marcasregistradas)
                
                for processo_deferido in numeros_de_processo:
                #crawler para buscar processos indeferidos
                    if not processo_ja_existe(processo_indeferido, processo_deferido,   f'{revista}_analisada.csv'):
                        num_processo, nome_marca, situacao, apresentacao, natureza, classificacao_nice, data_de_deposito, classificacao_de_viena, texto_do_despacho = buscar_marca(processo_deferido)
                        print("Marca deferida: ", num_processo, nome_marca, situacao, apresentacao, natureza, classificacao_nice, data_de_deposito, classificacao_de_viena)
                        
                        
                        dados.append(
                            [num_processo_in, nome_marca_in, situacao_in, apresentacao_in, natureza_in, classificacao_nice_in, classificacao_de_viena_in, data_de_deposito_in,
                            num_processo, nome_marca, situacao, apresentacao, natureza, classificacao_nice, classificacao_de_viena, data_de_deposito,
                            texto_do_despacho_in, revista, 0, 0, 0]
                        )

                        novo_registro = [num_processo_in, nome_marca_in, situacao_in, apresentacao_in, natureza_in, classificacao_nice_in, classificacao_de_viena_in, data_de_deposito_in,
                            num_processo, nome_marca, situacao, apresentacao, natureza, classificacao_nice, classificacao_de_viena, data_de_deposito,
                            texto_do_despacho_in, revista, 0, 0, 0]
                        
                        nome_arquivo = f'{revista}_analisada.csv'
                        arquivo_existe = os.path.exists(nome_arquivo)
                    
                        with open(nome_arquivo, 'a', newline='', encoding='utf-8') as arquivo_csv:
                            escritor = csv.writer(arquivo_csv, delimiter='\t')

                            if not arquivo_existe or arquivo_csv.tell() == 0:
                                escritor.writerow(cabecalho)

                            escritor.writerow(novo_registro)

                    else:
                        print(f"Processo {processo_indeferido} e processo {processo_deferido} já analisado!")


                    total_analisado += 1
                
                print("Total Analisado: ", total_analisado)
                
     
    except Exception as e:
        print(f"Erro ao analisar revista {revista}. Total Analisado: {total_analisado} -- ", e)
    


    print("Salvando informações...")

    # cabecalho = [
    #             'N° Processo',
    #             'Marca Indeferida',
    #             'Situação',
    #             'Apresentação',
    #             'Natureza',
    #             'Classe de Nice',
    #             'Classificação de Viena',
    #             'Data de Deposito',



    #             'N° Processo',
    #             'Marca Registrada',
    #             'Situação',
    #             'Apresentação',
    #             'Natureza',
    #             'Classe de Nice',
    #             'Classificação de Viena',
    #             'Data de Deposito',


    #             'Despacho',
    #             'Revista',
    #             'Visual',
    #             'Escrita',
    #             'Fonética'
    #         ]

    # nome_arquivo = f'{revista}_analisada.csv'
    # # Crie e escreva o arquivo CSV
    # with open(nome_arquivo, 'w', newline='', encoding='utf-8') as arquivo_csv:
    #     escritor = csv.writer(arquivo_csv, delimiter='\t')
    #     escritor.writerow(cabecalho)
    #     for linha in dados:
    #         escritor.writerow(linha)

