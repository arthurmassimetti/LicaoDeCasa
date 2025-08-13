---

title: Versionamento
sidebar\_position: 3
description: Guia de versionamento por RM, fluxo HML → PRD (main) e exceções para urgências.
--------------------------------------------------------------------------------------------

## Visão Geral do Fluxo

![Fluxo de Versionamento (Imagem 1)](/img/versionamento/fluxo.png)

---

## Regras de Nomeação e Branches Principais

* **Branches principais**

  * `hml` → Homologação
  * `main` → Produção (PRD)
* **Convention de branches de feature (por RM)**

  * Criar **uma branch por atividade RM**.
  * Nomear usando o **número do RM**.

---

## Fluxo Padrão (RM → HML → PRD)

```mermaid
graph TD
    A[Pegar atividade com número (RM)] --> B[Criar branch com nome do RM]
    B --> C[Finalizar desenvolvimento]
    C --> D[Enviar para branch HML]
    D --> E[Validação em HML]
    E -->|Validação OK| F[Promover para main (PRD)]
```

**Como funciona:**

1. Ao receber a atividade, crie uma branch a partir do `hml` usando o número do RM.
2. Desenvolva a feature na branch criada.
3. Envie para a branch `hml` para homologação.
4. Após testes e aprovação, promova para a branch `main` (produção).

---

## Fluxo de Urgência (PRD Direto)

```mermaid
graph TD
    A[Identificar demanda urgente em Produção] --> B[Trabalhar direto na main]
    B --> C[Aplicar correção]
    C --> D[Publicar em Produção]
    D --> E[Retropropagar alteração para HML]
```

**Como funciona:**

1. Em casos críticos cobrados diretamente em produção, a correção pode ser feita na branch `main`.
2. Após publicar em produção, aplique a mesma alteração na `hml` para manter as branches alinhadas.

\:::danger Atenção
O fluxo de urgência deve ser utilizado **apenas** em casos críticos e com aprovação do time.
\:::
