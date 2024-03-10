Esse é um bot do discord criado por mim na Disciplina ENG4431 (Coleta e Persistência de Dados) da PUC-Rio. O bot foi desenvolvido em python utilizando Flask, Selenium, Pymongo, BeautifulSoup e a API do ChatGPT. Dentro do repositório há um vídeo mostrando o funcionamento completo do bot, já que parte do WebScrapping do BOT dependia do site MangaLivre que já não está mais no ar e para rodar o bot também seria necessário um token de bot do discord, uma chave para o chatGPT e um banco de dados mongo. 
O Bot conta com todas as funcionalidades descritas abaixo:
- Comando para acessar a alguma info via WebScrapping;
- Integração com a API do Chat GPT para que possa conversar com o bot;
- LOG de comandos (que ficam salvos no MongoDB) com:
 --Nome do comando utilizado;
 --Nome do usuário que usou o comando;
 --Data de envio do comando;
- CRUD para os Logs
- Cadastro de usuários via formulário web (é preciso acessar a página no navegador)
- Login para usuários cadastrados
