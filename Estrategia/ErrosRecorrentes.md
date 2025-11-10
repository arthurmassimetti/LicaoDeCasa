# Documentação de Diagnóstico — Sentinela de Movimentação

## Contexto

A Sentinela é responsável por monitorar e orquestrar o fluxo de movimentação de arquivos dentro do sistema de edição. Quando ocorre um **erro de movimentação**, uma das causas mais comuns está relacionada ao caminho incorreto do **`FullPath`** dos arquivos.

Este documento descreve os principais comandos SQL e verificações para diagnóstico e correção de problemas de movimentação, status e renderização.

---

## ⚙️ Consultas Principais

### 1. **Verificação do Arquivo no MediaArchive**

```sql
SELECT * FROM "MediaArchive" ma;
```

 **Objetivo:** listar os registros de mídia (arquivos) controlados pelo sistema.

 **Verificar:** se o campo `FullPath` está correto. Caminhos inválidos ou inconsistentes costumam causar falhas na Sentinela.

---

### 2. **Status do Sprint (Mesa de Edição)**

```sql
SELECT * FROM "ActionSprints" as2;
```

 **Objetivo:** acompanhar o status das tarefas na **mesa de edição**.

 **Uso comum:** confirmar se o sprint está ativo, pausado ou encerrado. Pode ajudar a entender se a Sentinela está tentando mover arquivos de um sprint já finalizado.

---

### 3. **Movimentação Interna de Arquivos**

```sql
SELECT * FROM "EditionActions" ea;
```

 **Objetivo:** visualizar as ações de movimentação dentro das pastas de edição.

 **Dica:** essa tabela reflete todas as alterações de status de tarefas e movimentações de arquivos. Pode ser usada para forçar uma atualização manual de status, caso necessário.

---

### 4. **Distribuição de Renderização (Máquinas Render)**

```sql
SELECT * FROM "Machines" m  
WHERE "Name" IN ('RENDER-01','RENDER-02','RENDER-03','RENDER-04');
```

 **Objetivo:** verificar a distribuição de cargas entre as máquinas de renderização.

 **LoadNumber da BO:** indica quantos arquivos cada render está processando. A suíte pode, em alguns casos, adicionar vídeos extras ou gerar discrepâncias entre o número de arquivos na pasta e o número registrado no banco.

---

##  Ajustes no Número de Arquivos

Caso o número de arquivos processados esteja incorreto, deve-se ajustar manualmente conforme a regra abaixo:

| Quantidade de Arquivos | Ajuste Necessário |
| ---------------------- | ----------------- |
| 1 arquivo              | `-3`              |
| 2 arquivos             | `-2`              |
| 3 arquivos             | `-1`              |

 **Exemplo:** se a pasta contém 2 arquivos, mas o banco indica um valor incorreto, atualize o campo `LoadNumber` para refletir `-2`.

---

##  Boas Práticas de Diagnóstico

* Verifique se os caminhos (`FullPath`) estão consistentes com a estrutura real de diretórios.
* Compare o número de arquivos físicos na pasta com o número registrado em banco.
* Analise os logs da Sentinela para identificar se o erro ocorre antes ou depois da tentativa de movimentação.
* Use as tabelas `EditionActions` e `ActionSprints` para rastrear a origem do erro (status, pastas incorretas, tarefas interrompidas, etc.).

---

##  Resumo

| Área           | Tabela           | Função Principal                                     |
| -------------- | ---------------- | ---------------------------------------------------- |
| Arquivos       | `MediaArchive`   | Verifica caminhos e metadados dos arquivos           |
| Mesa de Edição | `ActionSprints`  | Verifica status do sprint                            |
| Movimentações  | `EditionActions` | Controla mudanças de status e movimentações internas |
| Renderização   | `Machines`       | Distribui e valida a carga entre as máquinas         |

---

 **Em caso de erro persistente:**

1. Corrija manualmente o `FullPath` no banco, se necessário.
2. Ajuste o `LoadNumber` conforme a quantidade real de arquivos.
3. Reexecute a Sentinela e monitore os logs para confirmar se a movimentação foi normalizada.
