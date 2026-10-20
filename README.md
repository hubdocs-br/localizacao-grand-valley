# Localização Grand Valley — Mapa interativo

Mapa interativo do **Grand Valley Club Resort** (Alto Perequê, Porto Belo/SC), feito com MapLibre.
Publicado no Netlify: chimerical-stardust-6c82f5.netlify.app

> Repositório **privado**. Contém material comercial (fotos, plantas e implantação). Não tornar público sem autorização.

## O que tem no mapa

- Demarcação do terreno (KMZ) e implantação ilustrada encaixada no terreno
- Logo do Grand Valley com contorno dourado e botão **Ver fotos** (galeria com 11 imagens)
- Rua de acesso ligada à Av. José Neoli Cruz
- 6 torres: Aurora, Brisa, Colina, Duna, Enseada e Flora
- Planta do pavimento tipo da Torre Flora sobre o prédio
- Barra de horário (nascer → pôr do sol) com sombra das torres pela posição real do sol e rosa dos ventos
  - Altura usada: 38 andares × ~3 m = 114 m (estimativa)
- Pontos de interesse da região com distâncias até o Grand Valley
- Simulador de valorização (cenário de 18% a.a., entrega em 2032 — projeção, não garantia)
- Contato: botão flutuante **Rofran Construtora · (47) 9 8922-5867** (WhatsApp)

## Pastas

| Pasta | Conteúdo |
|---|---|
| `publicar/` | `index.html` único (fotos embutidas, código protegido). **É o que vai para o Netlify** — arraste a pasta `publicar` em Deploys. |
| `mestre/` | `mapa_grand_valley_cores.html` — arquivo-fonte editável (código aberto). Toda alteração começa aqui. |
| `versao_leve/` | Versão em pasta (index.html + img/) compactada em zip. Precisa de servidor http. |
| `kmz/` | Terreno, torres e rua exportados do mapa (abrem no Google Earth / Meu Mapas). |
| `imagens/` | Implantação ilustrada (render), logo/pino e planta da Torre Flora com fundo transparente. |
| `ferramentas/` | Scripts que geram `publicar/` e `versao_leve/` a partir do mestre. |

## Como gerar a versão de publicar

```bash
npm i -g javascript-obfuscator
pip install pillow
# ajuste os caminhos no início de build_all.sh e rode:
bash ferramentas/build_all.sh
```

## Observações

- Os encaixes do render e da planta da Flora são visuais/ilustrativos, não levantamento técnico.
- Preço, disponibilidade e condições comerciais não fazem parte do mapa.
