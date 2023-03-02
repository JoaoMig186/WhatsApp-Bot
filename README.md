# WhatsApp-Bot
Um bot de WhatsApp criado a partir de orientações de um tutorial no Youtube. 

Canal Dev Aprender: https://www.youtube.com/watch?v=ISYHWfWvp3E&t=1059s

Esse programa foi criado para atender uma necessidade específica. Era necessário enviar mensagens para quase 200 contatos. Então com a ajuda do tutorial já citado acima, criei um bot utilizando Python juntamente com o Framework Selenium e o driver ChromeDriver.

O programa contém comentários de suas funcionalidades tanto em inglês, quanto em português. 

- bot.py:

Ele funciona dentro do WhatsApp web procurando o nome do contato ou grupo que foi passado (lembrando que ele pode procurar diversos grupos ou contatos), clicando nele, abrindo a área de texto, escrevendo a mensagem e enviando. O processo funciona utilizando as funcionalidades do Selenium, que se baseia em procurar elementos html e css na tela através de seletores e interagindo com funções como click(). Para interagir com o WhatsApp em si, foi utilizado o driver ChromeDriver (chromedriver.exe). Lembrando que além de enviar textos, o programa também envia imagens, onde foi implementado por mim.

Todas as explicações técnicas se encontram nos comentários da própria aplicação.

- gerarLista.py:

Esse arquivo permite criar uma lista de contatos para copiar e colar. Ele enumera os nomes para maior facilidade no processo. Ao invés de escrever na mão a lista de contatos genéricos como "contato1, contato2, contato3..." basta subistituir a string "Fulano/so-and-so" por "contato" e alterar a range de (1, até o valor que quiser) para gerar a numeração dos contatos. Após isso, basta executar no console, copiar a lista gerada e colar no array em bot.py para o programa procurar os contatos gerados.

Todas as explicações técnicas se encontram nos comentários da própria aplicação.
