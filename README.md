# Documentação do Projeto: Detector de BaiduNetdisk

Este projeto tem como objetivo detectar a instalação do **BaiduNetdisk** (um serviço de armazenamento em nuvem) no sistema operacional Windows, verificar a presença de arquivos executáveis e pastas relacionadas à aplicação, e gerar um arquivo de log com essas informações. Além disso, a documentação também explica a funcionalidade de remoção de acentos no texto do log gerado.

## Estrutura do Projeto

O script principal realiza as seguintes ações:

1. **Detecção de instalação**: Verifica os diretórios comuns onde o BaiduNetdisk pode estar instalado.
2. **Verificação de executáveis**: Procura pelo executável principal da aplicação nos diretórios encontrados.
3. **Verificação de pastas adicionais**: Verifica a presença de pastas de configuração, cache, logs e recursos associadas ao BaiduNetdisk.
4. **Remoção de acentos**: Normaliza e remove os acentos de todos os textos que aparecem no log gerado.
5. **Geração de Log**: Gera um arquivo de log no diretório `C:\Windows\Temp\` com as informações encontradas.

## Funcionalidades

### 1. Função `remover_acentos(texto)`
Remove acentos e caracteres especiais de um texto. Utiliza a normalização Unicode para remover caracteres com acentos.

**Parâmetros**:
- `texto` (str): Texto de entrada, que pode conter acentos.

**Retorno**:
- Retorna o texto sem acentos.

### 2. Função `detectar_baidunetdisk()`
Detecta se o BaiduNetdisk está instalado no sistema e verifica a presença de executáveis e pastas relacionadas à aplicação.

**Processos realizados**:
- Verifica a presença das pastas de instalação comuns para o BaiduNetdisk.
- Procura os executáveis principais do BaiduNetdisk.
- Verifica a existência de pastas de configuração, cache, logs e recursos.
- Salva um arquivo de log com os resultados.

**Passos**:
1. Verifica a existência das pastas em caminhos comuns.
2. Procura por executáveis, como `BaiduNetdisk.exe` ou `BaiduNetdiskApp.exe`.
3. Checa a existência de outras pastas relacionadas (Config, Cache, Logs, Resources).
4. Se encontrado, gera um arquivo de log no diretório `C:\Windows\Temp\` com a descrição do que foi encontrado.
5. Se falhar ao salvar o log, exibe uma mensagem de erro.

## Dependências

O script utiliza as seguintes bibliotecas:
- `os`: Para manipulação de caminhos e arquivos no sistema.
- `unicodedata`: Para a remoção de acentos de caracteres.

## Como Executar

Para executar o script, siga os passos abaixo:

1. Clone ou baixe o repositório do projeto.
2. Certifique-se de ter um ambiente Python configurado.
3. Execute o script em um terminal ou prompt de comando:

```bash
python baidunetdisk_detector.py
```

Após a execução, será gerado um arquivo de log em `C:\Windows\Temp\Baidu_Detector.txt` com as informações encontradas sobre a instalação do BaiduNetdisk.

## Exemplo de Saída de Log

O arquivo gerado pode conter informações como:

```
Pasta encontrada: C:\Program Files\BaiduNetdisk
Executável encontrado: C:\Program Files\BaiduNetdisk\BaiduNetdisk.exe
Pasta de Configuração encontrada: C:\Program Files\BaiduNetdisk\Config
Pasta de Cache encontrada: C:\Program Files\BaiduNetdisk\Cache
Pasta de Logs encontrada: C:\Program Files\BaiduNetdisk\Logs
Pasta de Recursos encontrada: C:\Program Files\BaiduNetdisk\Resources
```

Caso o BaiduNetdisk não seja encontrado, o log será vazio ou conterá apenas a mensagem de falha.

## Tratamento de Erros

Caso ocorra algum erro durante a execução, como falha ao salvar o log ou ao acessar as pastas, será exibida a seguinte mensagem no console:

```
Erro ao salvar o log: [Mensagem de erro]
```

## Conclusão

Este script é útil para detectar a instalação do BaiduNetdisk em um sistema Windows e verificar a presença de seus arquivos e pastas associados. Ele facilita a administração de sistemas, especialmente quando se precisa verificar a instalação de aplicativos específicos sem a necessidade de interface gráfica.
