# Segundo radar

Explorador de temas e referências com filtros por região e editoria. Os filtros são heurísticas por palavras-chave, não apuração local automática.

Projeto criado na oficina Codesinfo · REC’n’Play, Recife, 13 de novembro de 2026.

- [Demonstração da oficina](https://segundo-radar.burgos.chatgpt.site/)
- Slug preservado: `segundo-radar`.
- Esta cópia é independente do ambiente de hospedagem original. Não contém chaves de API nem o histórico privado de desenvolvimento.

## Instalação e execução

Requisito: Python 3 para servir os arquivos (nenhum pacote adicional).

```sh
git clone https://github.com/BurgosNY/segundo-radar.git
cd segundo-radar
python3 -m http.server 8000 --bind 127.0.0.1 --directory dist
```

Abra http://localhost:8000. Para publicar, hospede o conteúdo de `dist/` em qualquer hospedagem estática.

## IA e chaves

A interface e o fluxo principal deste projeto **não precisam de chave de API**. Não adicione uma chave ao JavaScript do navegador. OpenAI não é uma dependência obrigatória.

## Coleta pontual

`python3 scripts/collect.py` busca RSS da Agência Brasil e substitui `dist/radar-data.json`. O arquivo histórico pode conter outras referências; o coletor atual **não reproduz todas elas**. Possui exclusões editoriais por palavras-chave e não agrega automaticamente Google Trends. Confira fontes e resultado antes de publicar. Não há agendamento.

## Limites e uso editorial

Protótipo de oficina, não produto auditado para produção. Revise resultados, datas, contexto e fontes antes de publicar. Demonstrações históricas não indicam que a informação continua atual. Marcas e materiais de terceiros mantêm seus direitos; consulte `ASSETS.md`.
