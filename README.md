# Projeto de Web Scraping dos dados do site da Receita Federal do Brasil
Este projeto tem como objetivo extrair dados disponíveis no site da Receita Federal do Brasil (RFB), realizar transformações necessárias e carregar os dados em um ambiente local para análise posterior.
# Funcionalidades
1. Extração de Dados
   
O módulo de extração utiliza a biblioteca requests para realizar solicitações HTTP GET e a biblioteca BeautifulSoup para analisar documentos HTML. Ele acessa a página da web da RFB que contém os arquivos .zip dos dados a serem extraídos.

2. Download e Extração de Arquivos
    
Os arquivos .zip são baixados da web utilizando a função download_files_locally. Em seguida, o conteúdo desses arquivos é extraído e armazenado localmente utilizando a biblioteca zipfile.

3. Transformação de Dados (Não Implementada)

A etapa de transformação de dados não foi implementada neste projeto, mas poderia ser adicionada posteriormente para limpeza, formatação e agregação dos dados conforme necessário.

4. Carregamento de Dados

Os dados extraídos e transformados (se aplicável) são armazenados localmente em um diretório especificado.

# Contribuições
Contribuições são bem-vindas! Se você encontrar bugs, problemas ou deseja adicionar novos recursos, fique à vontade para abrir uma issue ou enviar um pull request.

# Autores
Amanda M. A. Antônio

# Licença
Este projeto é licenciado sob a Licença MIT.
