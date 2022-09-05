from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Variável media recebe uma imagem para o envio
# Var media get a image for send

media = "Caminho-da-sua-imagem/Path-of-your-image"

class WhatsappBot:
    def __init__(self):
        # Parte 1 - A mensagem que você quer enviar (Exemplo: Esta mensagem é um teste)
        # Part 1 - The message you want to send (Exemple: This message is a test)
        self.mensagem = """Esta mensagem é um teste/This message is a test"""
        self.mensagem.split("\n")

        # Parte 2 - Nome dos grupos ou pessoas a quem você deseja enviar a mensagem (Exemplo:  Fulano)
        # Part 2 - Name of the groups or people that you want to send a message (Exemple: so-and-so)
        self.grupos_ou_pessoas = ['Fulando/so-and-so']

        # Uso do driver para o WhatsApp web
        # Driver usage for WhatsApp web
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(
            executable_path=r'C:\whatsbot\chromedriver.exe', chrome_options=options)

    # Função principal do envio de mensagem
    # Main function of sending message
    def EnviarMensagens(self):
        self.driver.get('https://web.whatsapp.com')
        time.sleep(45)
        for grupo_ou_pessoa in self.grupos_ou_pessoas:

            # Parte que o programa pesquisa o nome da pessoa desejada e envia a mensagem de texto
            # Part that the program searches for the name of the desired person and sends the text message
            campo_pesquisa = self.driver.find_element(By.XPATH, "//div[@title='Caixa de texto de pesquisa']")
            time.sleep(3)
            campo_pesquisa.click()
            campo_pesquisa.send_keys(f"{grupo_ou_pessoa}")
            time.sleep(3)
            campo_grupo = self.driver.find_element(By.XPATH,
                f"//span[@title='{grupo_ou_pessoa}']")
            time.sleep(3)
            campo_grupo.click()
            time.sleep(3)
            chat_box = self.driver.find_element(By.CLASS_NAME, 'p3_M1')
            time.sleep(3)
            chat_box.click()
            chat_box.send_keys(self.mensagem)
            botao_enviar = self.driver.find_element(By.XPATH,
                "//span[@data-icon='send']")

            # Parte que envia uma imagem 
            # Part that sends image
            time.sleep(3)
            botao_enviar.click()
            enviarMidia = self.driver.find_element(By.XPATH, "//span[@data-icon='clip']")
            enviarMidia.click()
            attach = self.driver.find_element(By.XPATH, "//input[@type='file']")
            attach.send_keys(media)
            time.sleep(5)
            send = self.driver.find_element(By.CLASS_NAME, '_1w1m1')
            send.click()
            time.sleep(5)


bot = WhatsappBot()
bot.EnviarMensagens()