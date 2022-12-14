# Política de commit

## Tipos de Commit

|   Tipo de commit   |             Título             |       Descrição                                                                                            |
|--------------------|--------------------------------|------------------------------------------------------------------------------------------------------------|
|  "feat"            |  Features                      |  Nova Feature                                                                                              |
|  "fix"             |  Concerto de bugs              |  Concerto de um bug                                                                                        |
|  "docs"            |  Documentação                  |  Documente apenas as mudanças                                                                              |
|  "style"           |  Estilos                       |  Alterações que não afetam significamente o código (espaço em branco, formatação, falta de ponto e vírgula)|     
|  "refactor"        |  Refatoração de código         |  Uma alteração de código que não corrige um bug nem adiciona um recurso                                    |
|  "perf"            |  Melhorias de performace       |  Mudança de código que aumenta a performace do software                                                    |
|  "test"            |  Testes                        |  Adição de testes que estavam faltando ou correção de testes já existentes                                 |
|  "build"           |  Construção de código          |  Mudanças que alteram a estrutura do sistema ou as dependências externas                                   |
|  "ci"              |  Integrações contínuas         |  Alterações em nossos arquivos e scripts de configuração de CI                                             |
|  "chore"           |  Tarefas                       |  Outras mudanças que não midificam src ou os arquivos de testes                                            |
|  "revert"          |  Reversões                     |  Reverte um commit anterior                                                                                |
|  "initial"         |  Inicial                       |  Commit inicial                                                                                            |


* Os commits devem ser escritos em português, no gerúndio
* Devem ser objetivos e possuírem títulos de no máximo 72 caracteres
* Composição = (#Número da issue) + mensagem

## Exemplo

(#20) Criação do readme

* Caso mais de uma pessoa tenha participado, não se esqueça de incluir um coautor na mensagem

## Exemplo

|(#20) Criação do readme                                          |
|-----------------------------------------------------------------|
|Co-authored-by: Nome do coautor <e-maildocoautor@email.com>      |
