



# AWSRedshift
  
Módulo para trabalhar com banco de dados Redshift.  

*Read this in other languages: [English](Manual_AWSRedshift.md), [Português](Manual_AWSRedshift.pr.md), [Español](Manual_AWSRedshift.es.md)*
  
![banner](imgs/Banner_AWSRedshift.png)
## Como instalar este módulo
  
Para instalar o módulo no Rocketbot Studio, pode ser feito de duas formas:
1. Manual: __Baixe__ o arquivo .zip e descompacte-o na pasta módulos. O nome da pasta deve ser o mesmo do módulo e dentro dela devem ter os seguintes arquivos e pastas: \__init__.py, package.json, docs, example e libs. Se você tiver o aplicativo aberto, atualize seu navegador para poder usar o novo módulo.
2. Automático: Ao entrar no Rocketbot Studio na margem direita você encontrará a seção **Addons**, selecione **Install Mods**, procure o módulo desejado e aperte instalar.  


## Descrição do comando

### Conectar
  
Configure a conexão redshift, pode usar um identificador para alternar entre outras conexões.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Url do servidor|Url do servidor, pode ser um IP ou um domínio|example cluster.abc123xyz789.us-west-1.redshift.amazonaws.com|
|Porta|Porta de conexão, padrão 5439|5439|
|Base de dados|Nome da base de dados|database_name|
|Usuário|Usuário do base de dados|Rocketbot|
|Senha|Senha do usuário|secr3t_p@ss|
|Resultado|Variável onde o resultado da conexão é armazenado|conectado|

### Consulta Redshift
  
Realiza uma consulta Redshift (Select, insert, delete, etc)
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Query|Query to execute|select * from db|
|Resultado|Variável onde o resultado da consulta é armazenado|resultado|

### Fechar conexão
  
Fecha uma conexão de Redshift por sessão
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
