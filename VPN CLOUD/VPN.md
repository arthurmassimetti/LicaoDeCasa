# Guia de Atualização de Versão no Projeto - Docker Compose

Este documento detalha o processo completo para atualizar a versão de um projeto usando `docker-compose`, via terminal no Ubuntu acessado por VPN. Inclui comandos, etapas prévias, dicas e boas práticas.

---

## 0. Etapas Iniciais no Docker Desktop

Antes de qualquer processo via terminal, siga as instruções abaixo:

1. **Abra o Docker Desktop** em sua máquina.

   * O Docker precisa estar **ativo** para permitir o login no repositório Docker da Compliance.

2. **Login no Repositório da Compliance**:

   * Utilize a **chave de acesso (usuário e senha)** previamente fornecida para autenticar no repositório privado.

3. **Verifique a imagem hospedada no repositório** (ambiente HML ou PRD):

   * Por exemplo, se a última imagem é `55`, a nova imagem gerada deve ser `56`.
   * Gere e envie a nova imagem com o incremento de versão.

4. **Conecte-se à VPN da empresa** e acesse os servidores configurados para seu usuário:

   * Para Oracle e NetSuite: `conector-oracle-hml`
   * Para Infor: `conector-infor-hml`

> Observação: o mesmo procedimento se aplica posteriormente para o ambiente de produção (PRD), respeitando o mesmo fluxo e com maior cautela.

---

## 1. Alterar versão no `build.bat` ou `build.sh`

* Localize os arquivos `build.bat` (Windows) ou `build.sh` (Linux).
* Edite **apenas um dos dois** com a **nova versão** (somente a numeração).

**Dica:** Pode ser feito direto pelo terminal com `vim` ou `nano`.

### Exemplo (usando `vim`):

```bash
vim build.sh
```

Depois de editar:

* Salve com `:wq` no `vim`.

**Atenção:**
**Não** execute `docker rmi`, pois isso **remove a imagem**. Esse comando **não faz parte do processo de atualização**.

---

## 2. Acessar VPN e o ambiente Ubuntu

1. Conecte-se à VPN.
2. No terminal, digite:

```bash
conector-oracle-hml
```

3. Entre como root:

```bash
sudo su
```

---

## 3. Navegar até o diretório do projeto

Use `cd` e `TAB` para autocompletar os caminhos:

```bash
cd /compli[TAB]
cd [nome-da-pasta-do-projeto]
```

Para listar os arquivos:

```bash
ls
```

Localize o arquivo `docker-compose.yml` (ou apenas `docker-compose`).

---

## 4. Editar o arquivo `docker-compose.yml`

Abra o arquivo:

```bash
vim docker-compose.yml
```

Se aparecer "Read Only", pressione:

* `e` (edit anyway)

Ative o modo de inserção:

* Pressione `Insert`

**Nota:** Apenas com `Insert` ativado é possível editar o arquivo.

### Altere a versão desejada

* Normalmente os nomes das imagens estão destacados.
* Copie o nome do serviço ou container correspondente.

Para sair e salvar:

* Pressione `Esc`
* Digite `:wq` e pressione `Enter`

---

## 5. Atualizar a imagem do container

### Baixar a nova imagem:

```bash
docker-compose pull [nome-do-serviço]
```

**Dica:** Utilize o nome copiado do `docker-compose.yml`.

### Subir o container atualizado:

```bash
docker-compose up -d [nome-do-serviço]
```

### Reiniciar manualmente (se necessário):

```bash
docker restart [nome-do-container]
```

> Exemplo: reinicie apenas um serviço específico sem afetar os demais containers.

---

## Observações finais

* Sempre valide se a aplicação subiu corretamente com `docker ps`.
* Se ocorrer algum erro, visualize os logs com:

```bash
docker-compose logs -f [nome-do-serviço]
```

---

**Parabéns!** Agora você está pronto para atualizar versões de containers Docker com segurança e organização.

> Documentado por \[Seu Nome]
