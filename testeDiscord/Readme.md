### Bom dia gente, estes são meus codigo
---
*veja abaixo*

```JavaScript
       try {
            const [findMaxProcessId] = await app.utils.funcoes.maxProcessId(multorg, empId, tipObjIntegr, sequencia)
            const maxProcessId = findMaxProcessId.PROCESS_ID_INFOR
            const countQuery = await app.utils.funcoes.mountQueryCountInfor(multorg, tipObjIntegr);
            const resultCount = await app.middleware.infor.countAvailablePrids({query:countQuery, processoId:maxProcessId, empIdInfor, numEmpInfor, multorg, agendId, tipObjIntegr, tipObjIntegrDescr:"item"}) //resultado das querys
            let modelExtracao = await pool.query(`
                SELECT M.ID MOD_EXPORT_ID, M.TIPO_OBJ_INTEGR_ID, M.SEQUENCIA, M.CONSULTA, M.DEPARA_VALOR, M.QTDE_REG_LOTE QTD_LOTE_INFOR, M.CRITERIO, M.DESCRICAO, P.QTDE_POR_LOTE QTD_LOTE_CSF, M.TABELA FROM V_MODELO_EXTRACAO_INFOR M, PARAM_QTDE_LOTE P
                WHERE M.TIPO_OBJ_INTEGR_ID = P.TIPOOBJINTEGR_ID AND M.MULTORG_ID = P.MULTORG_ID AND M.TIPO_OBJ_INTEGR_ID = ? AND P.MULTORG_ID = ?
                ORDER BY M.SEQUENCIA`, [tipObjIntegr,multorg]
            );
```

---
### veja agora como executar

```bash
cd infor /npm start logs --lines 100
```

![renderer (5)](https://github.com/user-attachments/assets/b56343e8-ec86-4e96-8d4c-22c7ce85af7c)

---

[Profile.pdf](https://github.com/user-attachments/files/17654016/Profile.pdf)

---

[Apresentacao.pptx](https://github.com/user-attachments/files/17654018/Apresentacao.pptx)
