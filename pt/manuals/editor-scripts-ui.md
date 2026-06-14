---
brief: Este manual explica como criar elementos de UI no editor usando Lua
github: https://github.com/defold/doc
layout: manual
locale: pt
title: 'Scripts do editor: UI'
toc:
- Editor scripts e UI
- Hello world
- Conceitos básicos
- Componentes
- Props
- Alinhamento
- Componentes integrados
- Componentes de layout
- Componentes de apresentação de dados
- Componentes de entrada
- Componentes relacionados a diálogos
- Componentes utilitários
- Reatividade {reactivity}
- Regras da reatividade
- Hooks
- '**use_state**'
- '**use_memo**'
---

# Editor scripts e UI

Este manual explica como criar elementos interativos de UI no editor usando editor scripts escritos em Lua. Para começar com editor scripts, veja o [manual de Editor Scripts](/pt/manuals/editor-scripts). Você encontra a referência completa da API do editor [aqui](/ref/stable/editor-lua/). Atualmente, só é possível criar diálogos interativos, embora queiramos expandir o suporte a scripting de UI para o restante do editor no futuro.

## Hello world

Toda a funcionalidade relacionada a UI existe no módulo `editor.ui`. Este é o exemplo mais simples de um editor script com UI personalizada para começar:
```lua
local M = {}

function M.get_commands()
    return {
        {
            label = "Do with confirmation",
            locations = {"View"},
            run = function()
                local result = editor.ui.show_dialog(editor.ui.dialog({
                    title = "Perform action?",
                    buttons = {
                        editor.ui.dialog_button({
                            text = "Cancel",
                            cancel = true,
                            result = false
                        }),
                        editor.ui.dialog_button({
                            text = "Perform",
                            default = true,
                            result = true
                        })
                    }
                }))
                print('Perform action:', result)
            end
        }
    }
end

return M

```

Este trecho de código define um comando **View → Do with confirmation**. Quando você o executa, verá o seguinte diálogo:

![Diálogo Hello world](/manuals/images/editor_scripts/perform_action_dialog.png)

Por fim, depois de pressionar <kbd>Enter</kbd> (ou clicar no botão `Perform`), você verá a seguinte linha no console do editor:
```
Perform action:	true
```

## Conceitos básicos

### Componentes

O editor fornece vários **componentes** de UI que podem ser compostos para criar a UI desejada. Por convenção, todos os componentes são configurados usando uma única tabela chamada **props**. Os componentes em si não são tabelas, mas **userdata imutável** usado pelo editor para criar a UI.

### Props

**Props** são tabelas que definem entradas para componentes. Props devem ser tratadas como imutáveis: alterar a tabela de props in-place não fará o componente renderizar novamente, mas usar uma tabela diferente fará. A UI é atualizada quando a instância do componente recebe uma tabela de props que não é shallow-equal à anterior.

### Alinhamento

Quando o componente recebe alguns limites na UI, ele consome todo o espaço, mas isso não significa que a parte visível do componente será esticada. Em vez disso, a parte visível usará o espaço de que precisa e então será alinhada dentro dos limites atribuídos. Portanto, a maioria dos componentes integrados define uma prop `alignment`.

Por exemplo, considere este componente label:
```lua
editor.ui.label({
    text = "Hello",
    alignment = editor.ui.ALIGNMENT.RIGHT
})
```
A parte visível é o texto `Hello`, e ele é alinhado dentro dos limites atribuídos ao componente:

![Alinhamento](/manuals/images/editor_scripts/alignment.png)

## Componentes integrados

O editor define vários componentes integrados que podem ser usados em conjunto para construir a UI. Os componentes podem ser agrupados aproximadamente em 3 categorias: layout, apresentação de dados e entrada.

### Componentes de layout

Componentes de layout são usados para posicionar outros componentes próximos uns dos outros. Os principais componentes de layout são **`horizontal`**, **`vertical`** e **`grid`**. Esses componentes também definem props como **padding** e **spacing**, em que padding é o espaço vazio entre a borda dos limites atribuídos e o conteúdo, e spacing é o espaço vazio entre filhos:

![Padding e Spacing](/manuals/images/editor_scripts/padding_and_spacing.png)

O editor define constantes de padding e spacing `small`, `medium` e `large`. Em relação a spacing, `small` é destinado ao espaçamento entre subelementos diferentes de um elemento de UI individual, `medium` é para espaçamento entre elementos de UI individuais, e `large` é o espaçamento entre grupos de elementos. O spacing padrão é `medium`. Um valor de padding `large` significa padding das bordas da janela até o conteúdo, `medium` é padding das bordas de um elemento de UI significativo, e `small` é padding das bordas de pequenos elementos de UI como menus de contexto e tooltips (ainda não implementados).

Um contêiner **`horizontal`** posiciona seus filhos um depois do outro horizontalmente, sempre fazendo a altura de cada filho preencher o espaço disponível. Por padrão, a largura de cada filho é mantida no mínimo, embora seja possível fazê-lo ocupar o máximo de espaço possível definindo a prop `grow` como `true` em um filho.

Um contêiner **`vertical`** é semelhante ao horizontal, mas com os eixos trocados.

Por fim, **`grid`** é um componente contêiner que distribui seus filhos em uma grade 2D, como uma tabela. A configuração `grow` em uma grid se aplica a linhas ou colunas, portanto ela é definida não em um filho, mas na tabela de configuração de coluna. Além disso, filhos em uma grid podem ser configurados para ocupar várias linhas ou colunas com as props `row_span` e `column_span`. Grids são úteis para criar formulários com várias entradas:
```lua
editor.ui.grid({
    padding = editor.ui.PADDING.LARGE, -- adiciona padding ao redor das bordas do diálogo
    columns = {% raw %}{{}, {grow = true}}{% endraw %}, -- faz a 2a coluna crescer
    children = {
        {
            editor.ui.label({ 
                text = "Level Name",
                alignment = editor.ui.ALIGNMENT.RIGHT
            }),
            editor.ui.string_field({})
        },
        {
            editor.ui.label({ 
                text = "Author",
                alignment = editor.ui.ALIGNMENT.RIGHT
            }),
            editor.ui.string_field({})
        }
    }
})
```
O código acima produzirá o seguinte formulário de diálogo:

![Diálogo New Level](/manuals/images/editor_scripts/new_level_dialog.png)

### Componentes de apresentação de dados

O editor define 4 componentes de apresentação de dados:
- **`label`** — rótulo de texto, destinado a ser usado com entradas de formulário.
- **`icon`** — um ícone; atualmente, só pode ser usado para apresentar um pequeno conjunto de ícones predefinidos, mas pretendemos permitir mais ícones no futuro.
- **`heading`** — elemento de texto destinado a apresentar uma linha de título, por exemplo em um formulário ou diálogo. O enum `editor.ui.HEADING_STYLE` define vários estilos de título que incluem os títulos `H1`-`H6` do HTML, bem como estilos específicos do editor, `DIALOG` e `FORM`.
- **`paragraph`** — elemento de texto destinado a apresentar um parágrafo. A principal diferença em relação a `label` é que paragraph oferece suporte a quebra de linha: se os limites atribuídos forem pequenos demais horizontalmente, o texto quebrará linha e possivelmente será encurtado com `"..."` se não couber na visualização.

### Componentes de entrada

Componentes de entrada são feitos para que o usuário interaja com a UI. Todos os componentes de entrada oferecem suporte à prop `enabled` para controlar se a interação está habilitada ou não, e definem várias props de callback que notificam o editor script sobre a interação.

Se você criar uma UI estática, basta definir callbacks que simplesmente modificam locals. Para UIs dinâmicas e interações mais avançadas, veja [reatividade](#reactivity).

Por exemplo, é possível criar um diálogo New File estático simples assim:
```lua
-- nome inicial do arquivo, será substituído pelo diálogo
local file_name = ""
local create_file = editor.ui.show_dialog(editor.ui.dialog({
    title = "Create New File",
    content = editor.ui.horizontal({
        padding = editor.ui.PADDING.LARGE,
        spacing = editor.ui.SPACING.MEDIUM,
        children = {
            editor.ui.label({
                text = "New File Name",
                alignment = editor.ui.ALIGNMENT.CENTER
            }),
            editor.ui.string_field({
                grow = true,
                text = file_name,
                -- Callback de digitação:
                on_value_changed = function(new_text)
                    file_name = new_text
                end
            })
        }
    }),
    buttons = {
        editor.ui.dialog_button({ text = "Cancel", cancel = true, result = false }),
        editor.ui.dialog_button({ text = "Create File", default = true, result = true })
    }
}))
if create_file then
    print("create", file_name)
end
```
Esta é uma lista de componentes de entrada integrados:
- **`string_field`**, **`integer_field`** e **`number_field`** são variações de um campo de texto de uma linha que permitem editar strings, inteiros e números.
- **`select_box`** é usado para selecionar uma opção de um array predefinido de opções com um controle dropdown.
- **`check_box`** é um campo de entrada booleano com callback `on_value_changed`
- **`button`** com callback `on_press`, que é invocado quando o botão é pressionado.
- **`external_file_field`** é um componente destinado a selecionar um caminho de arquivo no computador. Ele consiste em um campo de texto e um botão que abre uma caixa de diálogo de seleção de arquivo.
- **`resource_field`** é um componente destinado a selecionar um recurso no projeto.

Todos os componentes, exceto botões, permitem definir uma prop `issue` que exibe o problema relacionado ao componente (ou `editor.ui.ISSUE_SEVERITY.ERROR` ou `editor.ui.ISSUE_SEVERITY.WARNING`), por exemplo:
```lua
issue = {severity = editor.ui.ISSUE_SEVERITY.WARNING, message = "This value is deprecated"}
```
Quando issue é especificado, ele altera a aparência do componente de entrada e adiciona uma tooltip com a mensagem do problema.

Aqui está uma demonstração de todas as entradas com suas variantes de issue:

![Entradas](/manuals/images/editor_scripts/inputs_demo.png)

### Componentes relacionados a diálogos

Para mostrar um diálogo, você precisa usar a função `editor.ui.show_dialog`. Ela espera um componente **`dialog`** que define a estrutura principal dos diálogos Defold: `title`, `header`, `content` e `buttons`. O componente dialog é um pouco especial: você não pode usá-lo como filho de outro componente, porque ele representa uma janela, não um elemento de UI. `header` e `content`, porém, são componentes comuns.

Botões de diálogo também são especiais: eles são criados usando o componente **`dialog_button`**. Diferente de botões comuns, botões de diálogo não têm callback `on_pressed`. Em vez disso, definem uma prop `result` com um valor que será retornado pela função `editor.ui.show_dialog` quando o diálogo for fechado. Botões de diálogo também definem as props booleanas `cancel` e `default`: um botão com a prop `cancel` é acionado quando o usuário pressiona <kbd>Escape</kbd> ou fecha o diálogo com o botão de fechar do sistema operacional, e o botão `default` é acionado quando o usuário pressiona <kbd>Enter</kbd>. Um botão de diálogo pode ter as props `cancel` e `default` definidas como `true` ao mesmo tempo.

### Componentes utilitários

Além disso, o editor define alguns componentes utilitários:
- **`separator`** é uma linha fina usada para delimitar blocos de conteúdo
- **`scroll`** é um componente wrapper que mostra barras de rolagem quando o componente envolvido não cabe no espaço atribuído

## Reatividade {#reactivity}

Como componentes são **userdata imutável**, é impossível alterá-los depois que são criados. Como fazer a UI mudar com o tempo então? A resposta: **componentes reativos**.

<div class='sidenote' markdown='1'>
A UI de editor scripting se inspira na biblioteca [React](https://react.dev/), então conhecer UI reativa e React hooks ajudará.
</div>

Em termos simples, um componente reativo é um componente com uma função Lua que recebe dados (props) e retorna uma view (outro componente). A função de componente reativo pode usar **hooks**: funções especiais no módulo `editor.ui` que adicionam recursos reativos aos seus componentes. Por convenção, todos os hooks têm um nome que começa com `use_`.

Para criar um componente reativo, use a função `editor.ui.component()`.

Vamos ver este exemplo — um diálogo New File que só permite criar um arquivo se o nome de arquivo inserido não estiver vazio:

```lua
-- 1. dialog é um componente reativo
local dialog = editor.ui.component(function(props)
    -- 2. o componente define um estado local (nome do arquivo) com string vazia como padrão
    local name, set_name = editor.ui.use_state("")

    return editor.ui.dialog({ 
        title = props.title,
        content = editor.ui.vertical({
            padding = editor.ui.PADDING.LARGE,
            children = { 
                editor.ui.string_field({ 
                    value = name,
                    -- 3. digitação + Enter atualiza o estado local
                    on_value_changed = set_name 
                }) 
            }
        }),
        buttons = {
            editor.ui.dialog_button({ 
                text = "Cancel", 
                cancel = true 
            }),
            editor.ui.dialog_button({ 
                text = "Create File",
                -- 4. a criação é habilitada quando o nome existe
                enabled = name ~= "",
                default = true,
                -- 5. o resultado é o nome
                result = name
            })
        }
    })
end)

-- 6. show_dialog retornará um nome de arquivo não vazio ou nil ao cancelar
local file_name = editor.ui.show_dialog(dialog({ title = "New File Name" }))
if file_name then 
    print("create " .. file_name)
else
    print("cancelled")
end
```

Quando você executa um comando de menu que roda esse código, o editor mostra um diálogo com o diálogo `"Create File"` desabilitado no início, mas, quando você digita um nome e pressiona <kbd>Enter</kbd>, ele fica habilitado:

![Diálogo New File](/manuals/images/editor_scripts/reactive_new_file_dialog.png)

Então, como isso funciona? Na primeira renderização, o hook `use_state` cria um estado local associado ao componente e o retorna junto com um setter para esse estado. Quando a função setter é invocada, ela agenda uma nova renderização do componente. Nas renderizações subsequentes, a função de componente é invocada de novo, e `use_state` retorna o estado atualizado. O novo componente de view retornado pela função de componente é então comparado com o antigo, e a UI é atualizada onde mudanças foram detectadas.

Essa abordagem reativa simplifica muito a construção de UIs interativas e a manutenção da sincronia: em vez de atualizar explicitamente todos os componentes de UI afetados pela entrada do usuário, a view é definida como uma função pura da entrada (props e estado local), e o editor cuida de todas as atualizações.

### Regras da reatividade

O editor espera que funções de componentes reativos se comportem bem para funcionarem:

1. Funções de componente devem ser puras. Não há garantia de quando ou com que frequência a função de componente será invocada. Todos os efeitos colaterais devem ficar fora da renderização, por exemplo em callbacks
2. Props e estado local devem ser imutáveis. Não altere props. Se seu estado local é uma tabela, não a altere in-place; crie uma nova e passe-a ao setter quando o estado precisar mudar.
3. Funções de componente devem chamar os mesmos hooks na mesma ordem em todas as invocações. Não chame hooks dentro de loops, em blocos condicionais, depois de retornos antecipados etc. É uma boa prática chamar hooks no início da função de componente, antes de qualquer outro código.
4. Chame hooks apenas a partir de funções de componente. Hooks funcionam no contexto de um componente reativo, então só é permitido chamá-los na função de componente (ou em outra função chamada diretamente pela função de componente).

### Hooks

<div class='sidenote' markdown='1'>
Se você conhece [React](https://react.dev/), perceberá que hooks no editor têm semântica ligeiramente diferente em relação a dependências de hook.
</div>

O editor define 2 hooks: **`use_memo`** e **`use_state`**.

### **`use_state`**

Estado local pode ser criado de 2 formas: com um valor padrão ou com uma função inicializadora:
```lua
-- valor padrão
local enabled, set_enabled = editor.ui.use_state(true)
-- função inicializadora + args
local id, set_id = editor.ui.use_state(string.lower, props.name)
```
De forma semelhante, o setter pode ser invocado com um novo valor ou com uma função atualizadora:
```lua
-- função atualizadora
local function increment_by(n, by)
    return n + by
end

local counter = editor.ui.component(function(props)
    local count, set_count = editor.ui.use_state(0)
    
    return editor.ui.horizontal({
        spacing = editor.ui.SPACING.SMALL,
        children = {
            editor.ui.label({
                text = tostring(count),
                alignment = editor.ui.ALIGNMENT.LEFT,
                grow = true
            }),
            editor.ui.text_button({
                text = "+1",
                on_pressed = function() set_count(increment_by, 1) end
            }),
            editor.ui.text_button({
                text = "+5",
                on_pressed = function() set_count(increment_by, 5) end
            })
        }
    })
end)
```

Por fim, o estado pode ser **resetado**. O estado é resetado quando qualquer argumento de `editor.ui.use_state()` muda, verificado com `==`. Por isso, você não deve usar tabelas literais nem funções inicializadoras literais como argumentos do hook `use_state`: isso fará o estado ser resetado em toda nova renderização. Para ilustrar:
```lua
-- ❌ RUIM: inicializador de tabela literal causa reset do estado em toda nova renderização
local user, set_user = editor.ui.use_state({ first_name = props.first_name, last_name = props.last_name})

-- ✅ BOM: use função inicializadora fora da função de componente para criar estado de tabela
local function create_user(first_name, last_name) 
    return { first_name = first_name, last_name = last_name}
end
-- ...depois, na função de componente:
local user, set_user = editor.ui.use_state(create_user, props.first_name, props.last_name)


-- ❌ RUIM: função inicializadora literal causa reset do estado em toda nova renderização
local id, set_id = editor.ui.use_state(function() return string.lower(props.name) end)

-- ✅ BOM: use função inicializadora referenciada para criar o estado
local id, set_id = editor.ui.use_state(string.lower, props.name)
```

### **`use_memo`**

Você pode usar o hook `use_memo` para melhorar o desempenho. É comum realizar algumas computações nas funções de renderização, por exemplo para verificar se a entrada do usuário é válida. O hook `use_memo` pode ser usado em casos em que verificar se os argumentos da função de computação mudaram é mais barato do que invocar a função de computação. O hook chamará a função de computação na primeira renderização e reutilizará o valor computado em renderizações subsequentes se todos os argumentos de `use_memo` estiverem inalterados:
```lua
-- função de validação fora da função de componente
local function validate_password(password)
    if #password < 8 then
        return false, "Password must be at least 8 characters long."
    elseif not password:match("%l") then
        return false, "Password must include at least one lowercase letter."
    elseif not password:match("%u") then
        return false, "Password must include at least one uppercase letter."
    elseif not password:match("%d") then
        return false, "Password must include at least one number."
    else
        return true, "Password is valid."
    end
end

-- ...depois, na função de componente
local username, set_username = editor.ui.use_state('')
local password, set_password = editor.ui.use_state('')
local valid, message = editor.ui.use_memo(validate_password, password)
```
Neste exemplo, a validação de senha será executada a cada mudança de senha (por exemplo, ao digitar em um campo de senha), mas não quando o nome de usuário for alterado.

Outro caso de uso para `use_memo` é criar callbacks que depois são usados em componentes de entrada, ou quando uma função criada localmente é usada como valor de prop para outro componente — isso evita novas renderizações desnecessárias.