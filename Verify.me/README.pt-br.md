# Projeto Verify.me - Marco Boschetti
[![en](https://img.shields.io/badge/lang-en-red.svg)](https://github.com/MarcoBosc/MarcoBosc-Portfolio/blob/main/Verify.me/README.md)
[![pt-br](https://img.shields.io/badge/lang-pt--br-green.svg)](https://github.com/MarcoBosc/MarcoBosc-Portfolio/blob/main/Verify.me/README.pt-br.md)

# Escopo do Projeto
Este projeto visa desenvolver uma aplicação que permita aos usuários enviar documentos de identificação, como RG ou CNH, juntamente com informações adicionais, como nome completo e uma foto, para verificação de autenticidade. A aplicação então processará esses documentos e retornará uma validação sobre se os documentos correspondem à identidade do usuário. Essa ferramenta será útil para diversas finalidades, como autenticação de identidade em transações online, verificação de idade em aplicativos de compra, entre outras. O projeto será desenvolvido em uma arquitetura na AWS, utilizando tecnologias como Amazon Textract, Rekognition, Api Gateway e outros. Todos os serviços serão alocados na região Norte da Virgínia (us-east-1).

### Funcionalidades do projeto
- [x] Campos para envio dos dados necessários(Nome completo, RG/CNH, foto com o documento).
- [x] Retorno visual da detecção de fraude.

## Tecnologias
[Amazon Textract](https://aws.amazon.com/pt/textract/) é um serviço da Amazon Web Services (AWS) que utiliza tecnologia de Machine Learning para extrair texto e dados de documentos. Ele é capaz de identificar e extrair informações de documentos em diversos formatos, como PDFs, imagens e até mesmo documentos digitalizados, facilitando a automação de processos de documentos.

[Amazon Rekognition](https://aws.amazon.com/pt/rekognition/), por outro lado, é um serviço de análise de imagens e vídeos que também utiliza Machine Learning. Ele permite identificar objetos, pessoas, texto em imagens e até mesmo emoções faciais. Isso torna possível automatizar tarefas como identificação de rostos em fotos, detecção de conteúdo impróprio em vídeos e muito mais.

## Arquitetura
<p align="center" width="100%">
    <img width="60%" src="../imgs/Verify.me.png">
</p>

A arquitetura do projeto trabalha da seguinte maneira:
- O usuário acessa a aplicação através da url do bucket público onde contém toda a aplicação web.
- Ao submeter um teste de verificação de identidade, a aplicação envia uma requisição do tipo "POST" para o [API Gateway](https://aws.amazon.com/pt/api-gateway/) e aguarda sua resposta de maneira assíncrona através do método [fetch()](https://developer.mozilla.org/en-US/docs/Web/API/fetch) do javascript, essa requisção contém todos os itens adicionados pelo usuário(RG/CNH, nome completo e foto com o documento).
- Com isso o API Gateway irá acionar o [lambda](https://aws.amazon.com/pt/lambda/), que será responsável por acionar o Amazon Textract e Rekognition para realizar a verificação de identidade através da biblioteca de python boto3.
- Nesse momento o lambda irá retornar se ele foi detectada ou não uma fraude, ou seja, se os dados enviados são ou não da mesma pessoa.
- O API Gateway retorna para a aplicação a resposta do Lambda
- A aplicação mostra na tela se o usuário está ou não cometendo uma possível fraude.

## METODOLOGIA
A infraestrutura do projeto será alocada na nuvem através do uso do [terraform](https://www.terraform.io), onde o estado de cada um dos recursos utilizados na AWS será armazenado em um bucket s3 chamado verify-me-infra-remote-state-bucket. Esses estados serão utilizados para armazenar o tf.state dos recursos, com isso, poderemos subir e destruir a infraestrutura em segundos graças ao [terraform](https://www.terraform.io). Também utilizaremos o [GitHub Actions](https://docs.github.com/pt/actions) para criar pipelines de CI/CD(Integração Contínua e Entreca Contínua) que é uma prática fundamental para incrementar a qualidade do software.

### Replicando o projeto.
Primeiramente, você precisa ter um [usuário do IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html) configurada em sua conta da AWS, com suas AccessKey e SecretAccessKeys. Para replicação do projeto, você pode optar por usar ou não o Github Actions.

### Com Github Actions
- Crie um repositório no github para o projeto.
- Na Aba Settings, localize o campo "Secrets and variables" no menu lateral.
- Clique Na Opção Actions e configure suas credenciais da AWS no botão "New repository secret".
<p align="center" width="100%">
    <img width="60%" src="../imgs/configureCredentials.png">
</P>
- O nome de seus secrets devem ser AWS_ACCESS_KEY_ID e AWS_SECRET_ACCESS_KEY, e o secret deve ser suas respectivas credenciais.
- Suba o diretório Verify.me no repositório, isso irá executar a pipeline chamada Terraform Deploy
- Na Aba Actions, você pode monitorar o status da pipeline.
- Pronto! Agora basta acessar o link do seu bucket com o app e testá-lo normalmente.

Para destruir o projeto, basta clicar para executar a pipeline chamada Terraform Destroy, então o terraform irá automaticamente destruir toda a infraestrutura criada na execução da pipeline Terraform Deploy.

### Sem Github Actions

Com o [terraform instalado](https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli) em sua máquina, basta abrir o terminal e acessar o diretório do projeto Verify.me e digitar os seguintes comandos:
- Inicie o terraform em seu diretório local:
    ```
    terraform init
    ```

- (Opcional) Valide se está tudo certo com as configurações dos arquivos .tf:
    ```
    terraform validate
    ```

- Crie um plano de execução da infraestrutura
    ```
    terraform plan
    ```

- Executa todos os passos definidos pelo terraform plan, também cria o arquivo.tfstate.
    ```
    terraform apply -auto-approve
    ```

- Pronto! Agora basta acessar o link do seu bucket com o app e testá-lo normalmente.

Para destruir o projeto, basta executar o comando:
    ```
    terraform destroy -auto-approve
    ```
Com isso, o terraform irá automaticamente destruir toda a infraestrutura criada na execução do comando "terraform apply -auto-approve".