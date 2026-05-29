---
brief: Este manual descreve como otimizar o uso de memória de um jogo Defold.
github: https://github.com/defold/doc
layout: manual
locale: pt
title: Otimizando o uso de memória de um jogo Defold
toc:
- Otimizando o uso de memória
- Compressão de texturas
- Carregamento dinâmico
- Otimizar contadores de componentes
- Otimizar a contagem de nodes de GUI
---

# Otimizando o uso de memória

## Compressão de texturas
O uso de compressão de texturas não apenas reduz o tamanho dos recursos dentro do arquivo do jogo, mas texturas comprimidas também podem reduzir a quantidade de memória de GPU necessária.

## Carregamento dinâmico
A maioria dos jogos tem pelo menos algum conteúdo usado com pouca frequência. Do ponto de vista de uso de memória, não faz sentido manter esse conteúdo carregado na memória o tempo todo; é melhor carregá-lo e descarregá-lo quando necessário. Isso obviamente envolve uma troca entre ter algo prontamente acessível ao custo de memória em tempo de execução e carregar algo ao custo de tempo de carregamento.

O Defold tem várias formas diferentes de carregar conteúdo dinamicamente:

* [Proxies de coleção](/pt/manuals/collection-proxy/)
* [Fábricas de coleção dinâmicas](/pt/manuals/collection-factory/#dynamic-loading-of-factory-resources)
* [Fábricas dinâmicas](/pt/manuals/factory/#dynamic-loading-of-factory-resources)
* [Live Update](/pt/manuals/live-update/)

## Otimizar contadores de componentes
O Defold aloca memória para componentes e recursos uma vez quando uma coleção é criada, para reduzir a fragmentação de memória. A quantidade de memória alocada depende da configuração de vários contadores de componentes em *game.project*. Use o [perfilador](/pt/manuals/profiling/) para obter uso preciso de componentes e recursos e configurar seu jogo para usar valores máximos mais próximos da contagem real de componentes e recursos. Isso reduzirá a quantidade de memória usada pelo seu jogo (consulte as informações sobre [otimizações de contagem máxima](/pt/manuals/project-settings/#component-max-count-optimizations) de componentes).

## Otimizar a contagem de nodes de GUI
Otimize as contagens de nodes de GUI definindo o número máximo de nodes no arquivo GUI apenas para o necessário. O campo `Current Nodes` das [propriedades do componente GUI](https://defold.com/pt/manuals/gui/#gui-properties) mostrará o número de nodes usados pelo componente GUI.

{% include shared/pt/optimization-memory-html5.md %}