---
brief: Este manual oferece uma visão geral dos componentes e de como usá-los.
github: https://github.com/defold/doc
layout: manual
locale: pt
title: Componentes de objeto de jogo
toc:
- Componentes
- Tipos de componente
- Ativando e desativando componentes
- Propriedades de componentes
- Posição, rotação e escala de componentes
- Ordem de desenho dos componentes
- Predicados do script de renderização
- Valor z do componente
---

#  Componentes

{% include shared/pt/components.md %}

## Tipos de componente

O Defold oferece suporte aos seguintes tipos de componente:

* [Fábrica de coleção](/pt/manuals/collection-factory) - Cria coleções
* [Proxy de coleção](/pt/manuals/collection-proxy) - Carrega e descarrega coleções
* [Objeto de colisão](/pt/manuals/physics) - Física 2D e 3D
* [Câmera](/pt/manuals/camera) - Altera o viewport e a projeção do mundo do jogo
* [Fábrica](/pt/manuals/factory) - Cria objetos de jogo
* [GUI](/pt/manuals/gui) - Renderiza uma interface gráfica de usuário
* [Rótulo](/pt/manuals/label) - Renderiza um trecho de texto
* [Luz](/pt/manuals/light) - Adiciona dados de luz para shaders
* [Mesh](/pt/manuals/mesh) Mostra uma malha 3D (com criação e manipulação em runtime)
* [Modelo](/pt/manuals/model) Mostra um modelo 3D (com animações opcionais)
* [Particle FX](/pt/manuals/particlefx) -  Cria partículas
* [Script](/pt/manuals/script) - Adiciona lógica de jogo
* [Som](/pt/manuals/sound) - Reproduz som ou música
* [Sprite](/pt/manuals/sprite) - Mostra uma imagem 2D (com animação flipbook opcional)
* [Tilemap](/pt/manuals/tilemap) - Mostra uma grade de tiles

Componentes adicionais podem ser adicionados por extensões:

* [Rive model](/extension-rive) - Renderiza uma animação Rive
* [Spine model](/extension-spine) - Renderiza uma animação Spine


## Ativando e desativando componentes

Os componentes de um objeto de jogo são ativados quando o objeto de jogo é criado. Se quiser desativar um componente, faça isso enviando uma mensagem [`disable`](/ref/go/#disable) ao componente:

```lua
-- desativa o componente com id 'weapon' no mesmo objeto de jogo deste script
msg.post("#weapon", "disable")

-- desativa o componente com id 'shield' no objeto de jogo 'enemy'
msg.post("enemy#shield", "disable")

-- desativa todos os componentes no objeto de jogo atual
msg.post(".", "disable")

-- desativa todos os componentes no objeto de jogo 'enemy'
msg.post("enemy", "disable")
```

Para ativar um componente novamente, você pode enviar uma mensagem [`enable`](/ref/go/#enable) ao componente:

```lua
-- ativa o componente com id 'weapon'
msg.post("#weapon", "enable")
```

## Propriedades de componentes

Os tipos de componente do Defold têm propriedades diferentes. O [painel Properties](/pt/manuals/editor/#the-editor-views) no editor mostrará as propriedades do componente atualmente selecionado no [painel Outline](/pt/manuals/editor/#the-editor-views). Consulte os manuais dos diferentes tipos de componente para saber mais sobre as propriedades disponíveis.

## Posição, rotação e escala de componentes

Componentes visuais geralmente têm propriedades de posição e rotação e, na maioria das vezes, também uma propriedade de escala. Essas propriedades podem ser alteradas no editor e, em quase todos os casos, não podem ser alteradas em runtime (a única exceção é a escala de componentes sprite e label, que pode ser alterada em runtime).

Se você precisa alterar a posição, rotação ou escala de um componente em runtime, modifique em vez disso a posição, rotação ou escala do objeto de jogo ao qual o componente pertence. Isso tem o efeito colateral de afetar todos os componentes no objeto de jogo. Se você quiser manipular apenas um componente específico entre muitos anexados a um objeto de jogo, recomenda-se mover o componente em questão para um objeto de jogo separado e adicioná-lo como objeto de jogo filho do objeto de jogo ao qual o componente pertencia originalmente.

## Ordem de desenho dos componentes

A ordem de desenho dos componentes visuais depende de duas coisas:

### Predicados do script de renderização
Cada componente recebe um [material](/pt/manuals/material/), e cada material tem uma ou mais tags. O script de renderização, por sua vez, definirá vários predicados, cada um correspondente a uma ou mais tags de material. Os [predicados do script de renderização são desenhados um por um](/pt/manuals/render/#render-predicates) na função *update()* do script de renderização, e os componentes correspondentes às tags definidas em cada predicado serão desenhados. O script de renderização padrão primeiro desenha sprites e tilemaps em uma passagem, depois efeitos de partículas em outra passagem, ambos em espaço de mundo. Em seguida, o script de renderização desenha componentes GUI em uma passagem separada em espaço de tela.

### Valor z do componente
Todos os objetos de jogo e componentes são posicionados em espaço 3D com posições expressas como objetos `vector3`. Quando você visualiza o conteúdo gráfico do seu jogo em 2D, os valores X e Y determinam a posição de um objeto ao longo dos eixos de "largura" e "altura", e a posição Z determina a posição ao longo do eixo de "profundidade". A posição Z permite controlar a visibilidade de objetos sobrepostos: um sprite com valor Z de 1 aparecerá na frente de um sprite na posição Z 0. Por padrão, o Defold usa um sistema de coordenadas que permite valores Z entre -1 e 1:

![modelo](/manuals/images/graphics/z-order.png)

Os componentes correspondentes a um [predicado de renderização](/pt/manuals/render/#render-predicates) são desenhados juntos, e a ordem em que são desenhados depende do valor z final do componente. O valor z final de um componente é a soma dos valores z do próprio componente, do objeto de jogo ao qual ele pertence e do valor z de quaisquer objetos de jogo pais.

<div class='sidenote' markdown='1'>
A ordem em que vários componentes GUI são desenhados **não** é determinada pelo valor z dos componentes GUI. A ordem de desenho dos componentes GUI é controlada pela função [gui.set_render_order()](/ref/gui/#gui.set_render_order:order).
</div>

Exemplo: dois objetos de jogo A e B. B é filho de A. B tem um componente sprite.

| O quê    | Valor Z |
|----------|---------|
| A        | 2       |
| B        | 1       |
| B#sprite | 0.5     |

![](/manuals/images/graphics/component-hierarchy.png)

Com a hierarquia acima, o valor z final do componente sprite em B é 2 + 1 + 0.5 = 3.5.

<div class='important' markdown='1'>
Se dois componentes tiverem exatamente o mesmo valor z, a ordem é indefinida, e você pode acabar com componentes piscando para frente e para trás ou componentes sendo renderizados em uma ordem em uma plataforma e em outra ordem em outra plataforma.

O script de renderização define um plano próximo e um plano distante para valores z. Qualquer componente com valor z fora desse intervalo não será renderizado. O intervalo padrão é -1 a 1, mas [ele pode ser alterado facilmente](/pt/manuals/render/#default-view-projection). A precisão numérica dos valores Z com limites próximo e distante de -1 e 1 é muito alta. Ao trabalhar com assets 3D, talvez seja necessário alterar os limites próximo e distante da projeção padrão em um script de renderização personalizado. Veja o [manual de renderização](/pt/manuals/render/) para mais informações.
</div>


{% include shared/pt/component-max-count-optimizations.md %}