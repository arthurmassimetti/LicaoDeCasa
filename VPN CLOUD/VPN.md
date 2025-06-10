# 🛠️ Guia de Atualização de Versão no Projeto - Docker Compose

Este documento detalha o processo completo para atualizar a versão de um projeto usando `docker-compose`, via terminal no Ubuntu acessado por VPN. Inclui comandos, atalhos, dicas e boas práticas.

---

## 📄 1. Alterar versão no `build.bat` ou `build.sh`

- Localize os arquivos `build.bat` (Windows) ou `build.sh` (Linux).
- Edite **apenas um dos dois** com a **nova versão** (somente a numeração).

> 💡 **Dica:** Pode ser feito direto pelo terminal com `vim` ou `nano`.

### Exemplo (usando `vim`):

```bash
vim build.sh
```

🔁 **Depois de editar:**
- Salve com `:wq` no `vim`.

> ⚠️ **Atenção:**  
**Não** execute `docker rmi`, pois isso **remove a imagem**. Esse comando **não faz parte do processo de atualização**.

---

## 🌐 2. Acessar VPN e o ambiente Ubuntu

1. Conecte-se à VPN da empresa.
2. Abra o terminal e digite:

```bash
conector-oracle-hml
```

3. Entre como root para fazer alterações:

```bash
sudo su
```

---

## 📁 3. Navegar até o diretório do projeto

Use `cd` e `TAB` para autocompletar os caminhos:

```bash
cd /compli[TAB]
cd [nome-da-pasta-do-projeto]
```

Listar os arquivos:

```bash
ls
```

Localize o arquivo:
- O nome normalmente é `docker-compose.yml` ou `docker-compose`.

---

## ✏️ 4. Editar o arquivo `docker-compose.yml`

Abra o arquivo no modo edição:

```bash
vim docker-compose.yml
```

Se aparecer a mensagem de "Read Only", pressione a tecla:
- `e` (de "edit anyway")

Ative o modo de inserção:
- Pressione `Insert`

> ℹ️ **Nota:** Apenas com `Insert` ativado você poderá editar o arquivo.

### Altere a versão desejada

- Normalmente os nomes estão em azul (sugestão: versão da imagem Docker).
- Copie o nome do serviço ou container.

Saia da edição:
- Pressione `Esc`
- Digite `:wq` e pressione `Enter` (write and quit)

---

## 🚀 5. Atualizar a imagem do container

### Comando para baixar a nova imagem:

```bash
docker-compose pull [nome-do-serviço]
```

> 💡 **Dica:** O nome copiado do `docker-compose.yml` deve ser usado aqui.

### Comando para subir o container atualizado:

```bash
docker-compose up -d [nome-do-serviço]
```

> ✅ Isso irá subir a nova versão no modo **detached (-d)**.

### 🔄 Reiniciar manualmente o container (se necessário)

Se for preciso **reiniciar o container manualmente** após a atualização ou algum ajuste, utilize:

```bash
docker restart [nome-do-container]
```

> 🛠️ **Exemplo de uso:**  
> Reinicie apenas uma parte específica do conector sem afetar o restante do ambiente.

---

## ⚠️ Observações finais

- Sempre valide se a aplicação subiu corretamente após o `up -d`.
- Utilize `docker ps` para ver os containers ativos.
- Se algo der errado, verifique os logs com:

```bash
docker-compose logs -f [nome-do-serviço]
```

---

**✨ Parabéns!** Agora você está pronto para atualizar serviços Docker com segurança e organização. 

> Documentado com carinho por [Seu Nome].
