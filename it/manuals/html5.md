---
brief: Questo manuale descrive il processo di creazione di un gioco HTML5, insieme ai problemi noti e alle limitazioni.
github: https://github.com/defold/doc
layout: manual
locale: it
title: Sviluppo con Defold per la piattaforma HTML5
toc:
- anchor: html5-development
  title: Sviluppo HTML5
- anchor: heap-size
  title: Dimensione dellheap
- anchor: testing-html5-build
  title: Test di una build HTML5
- anchor: creating-html5-bundle
  title: Creazione di un bundle HTML5
- anchor: known-issues-and-limitations
  title: Problemi noti e limitazioni
- anchor: customizing-html5-bundle
  title: Personalizzazione di un bundle HTML5
- anchor: downscale-fit-and-fit
  title: Downscale Fit e Fit
- Stretch
- No Scale
- anchor: tokens
  title: Token
- anchor: extra-parameters
  title: Parametri aggiuntivi
- anchor: file-operations-in-html5
  title: Operazioni sui file in HTML5
- anchor: passing-arguments-to-an-html5-game
  title: Passaggio di argomenti a un gioco HTML5
- anchor: engine-arguments
  title: Argomenti del motore
- anchor: query-arguments-in-the-url
  title: Argomenti di query nellURL
- anchor: optimizations
  title: Ottimizzazioni
- FAQ
---

# Sviluppo HTML5 {#html5-development}

Defold supporta la creazione di giochi per la piattaforma HTML5 tramite il normale menu di creazione dei bundle, come per le altre piattaforme. Inoltre, il gioco risultante viene incorporato in una normale pagina HTML, il cui aspetto può essere personalizzato tramite un semplice sistema di modelli.

Il file *game.project* contiene le impostazioni specifiche per HTML5:

![Impostazioni del progetto](/manuals/images/html5/html5_project_settings.png)

## Dimensione dell'heap {#heap-size}

Il supporto HTML5 di Defold si basa su Emscripten (vedi http://en.wikipedia.org/wiki/Emscripten). In breve, crea un'area di memoria isolata per l'heap in cui opera l'applicazione. Per impostazione predefinita, il motore alloca una quantità abbondante di memoria (256MB), che dovrebbe essere più che sufficiente per un gioco tipico. Durante l'ottimizzazione, puoi scegliere di usare un valore inferiore. Per farlo, segui questi passaggi:

1. Imposta *heap_size* sul valore desiderato, espresso in megabyte.
2. Crea il tuo bundle HTML5 (vedi sotto)

## Test di una build HTML5 {#testing-html5-build}

Per eseguire i test, una build HTML5 richiede un server HTTP. Defold ne crea uno per te se scegli <kbd>Project ▸ Build HTML5</kbd>.

![Build HTML5](/manuals/images/html5/html5_build_launch.png)

Se vuoi testare il tuo bundle, caricalo sul tuo server HTTP remoto oppure crea un server locale, ad esempio usando Python nella cartella del bundle.
Python 2:

```sh
python -m SimpleHTTPServer
```

Python 3:

```sh
python -m http.server
```

oppure

```sh
python3 -m http.server
```

<div class='important' markdown='1'>
Non puoi testare il bundle HTML5 aprendo il file `index.html` in un browser. È necessario un server HTTP.
</div>

<div class='important' markdown='1'>
Se nella console compare l'errore `"wasm streaming compile failed: TypeError: Failed to execute ‘compile’ on ‘WebAssembly’: Incorrect response MIME type. Expected ‘application/wasm’."`, assicurati che il server utilizzi il tipo MIME `application/wasm` per i file `.wasm`.
</div>

## Creazione di un bundle HTML5 {#creating-html5-bundle}

Creare contenuti HTML5 con Defold è semplice e segue la stessa procedura delle altre piattaforme supportate: seleziona <kbd>Project ▸ Bundle... ▸ HTML5 Application...</kbd> dal menu:

![Creazione di un bundle HTML5](/manuals/images/html5/html5_bundle.png)

I bundle HTML5 supportano due architetture WebAssembly:

* `wasm-web` - il normale motore WebAssembly, senza thread.
* `wasm_pthread-web` - un motore WebAssembly che può utilizzare i thread.

Puoi includere una delle due architetture oppure entrambe. Quando sono incluse entrambe, il caricatore seleziona `wasm_pthread-web` se il browser e l'ambiente di hosting lo supportano, altrimenti utilizza `wasm-web`. Consulta il [manuale di Bob](/it/manuals/bob/#usage) per i nomi canonici delle piattaforme di destinazione.

<div class='important' markdown='1'>
Il motore con supporto dei thread richiede `SharedArrayBuffer` in una pagina sicura e [isolata dalle altre origini](https://developer.mozilla.org/en-US/docs/Web/API/Window/crossOriginIsolated). Servi il bundle tramite HTTPS (o localhost) e configura il server con intestazioni compatibili con l'isolamento tra origini, generalmente:

```txt
Cross-Origin-Opener-Policy: same-origin
Cross-Origin-Embedder-Policy: require-corp
```

Anche le risorse caricate dalla pagina da altre origini devono utilizzare intestazioni CORS o Cross-Origin-Resource-Policy compatibili. Un bundle che contiene solo `wasm_pthread-web` non può essere eseguito se questi requisiti non sono soddisfatti; includi `wasm-web` come alternativa se il gioco potrebbe essere ospitato su un sito che non supporta l'isolamento tra origini.
</div>

I bundle HTML5 di Defold richiedono un browser moderno con supporto WebAssembly. Internet Explorer 11 non è supportato.

Quando fai clic sul pulsante <kbd>Create bundle</kbd>, ti verrà chiesto di selezionare una cartella in cui creare l'applicazione. Al termine dell'esportazione, troverai tutti i file necessari per eseguirla.

## Problemi noti e limitazioni {#known-issues-and-limitations}

* Hot Reload - L'hot reload non funziona nelle build HTML5. Per ricevere aggiornamenti dall'editor, le applicazioni Defold devono eseguire un proprio piccolo server web, cosa che non è possibile in una build HTML5.
* Chrome
  * Build di debug lente - Nelle build di debug per HTML5, verifichiamo tutte le chiamate grafiche WebGL per rilevare errori. Purtroppo, questa operazione è molto lenta durante i test in Chrome. Puoi disabilitarla impostando il campo *Engine Arguments* di *game.project* su `--verify-graphics-calls=false`.
* Supporto dei gamepad - [Consulta la documentazione dei gamepad](/it/manuals/input-gamepads/#gamepads-in-html5) per le considerazioni specifiche e i passaggi che potrebbero essere necessari su HTML5.

## Personalizzazione di un bundle HTML5 {#customizing-html5-bundle}

Quando generi una versione HTML5 del tuo gioco, Defold fornisce una pagina web predefinita. Questa fa riferimento a risorse di stile e script che determinano come viene presentato il gioco.

A ogni esportazione dell'applicazione, questi contenuti vengono ricreati. Se desideri personalizzare uno di questi elementi, devi modificare le impostazioni del progetto. Per farlo, apri *game.project* nell'editor Defold e scorri fino alla sezione *html5*:

![Sezione HTML5](/manuals/images/html5/html5_section.png)

Puoi trovare maggiori informazioni su ciascuna opzione nel [manuale delle impostazioni del progetto](/it/manuals/project-settings/#html5).

<div class='important' markdown='1'>
Non puoi modificare i file del modello HTML/CSS predefinito nella cartella `builtins`. Per applicare le tue modifiche, copia e incolla il file necessario da `builtins` e selezionalo in *game.project*.
</div>

<div class='important' markdown='1'>
Non applicare bordi o spaziatura interna al canvas. In caso contrario, le coordinate dell'input del mouse saranno errate.
</div>

In *game.project* puoi disattivare il pulsante `Fullscreen` e il link `Made with Defold`.
Defold fornisce un tema scuro e uno chiaro per `index.html`. Il tema chiaro è quello predefinito, ma puoi cambiarlo modificando il file `Custom CSS`. Nel campo `Scale Mode` puoi inoltre scegliere tra quattro modalità di ridimensionamento predefinite.

<div class='important' markdown='1'>
I calcoli per tutte le modalità di ridimensionamento includono i DPI attuali dello schermo se attivi l'opzione `High Dpi` in *game.project* (sezione `Display`)
</div>

### Downscale Fit e Fit {#downscale-fit-and-fit}

Nella modalità `Fit`, il canvas viene ridimensionato per mostrare l'intero canvas del gioco sullo schermo mantenendo le proporzioni originali. L'unica differenza di `Downscale Fit` è che il ridimensionamento avviene solo se le dimensioni interne della pagina web sono inferiori a quelle del canvas originale del gioco; il canvas non viene ingrandito quando la pagina web è più grande.

![Sezione HTML5](/manuals/images/html5/html5_fit.png)

### Stretch

Nella modalità `Stretch`, il canvas viene ridimensionato per riempire completamente lo spazio interno della pagina web.

![Sezione HTML5](/manuals/images/html5/html5_stretch.png)

### No Scale
Con la modalità `No Scale`, le dimensioni del canvas sono esattamente quelle definite nel file *game.project*, nella sezione `[display]`.

![Sezione HTML5](/manuals/images/html5/html5_no_scale.png)

## Token {#tokens}

Per creare il file `index.html` utilizziamo il [linguaggio di modelli Mustache](https://mustache.github.io/mustache.5.html). Durante la creazione di una build o di un bundle, i file HTML e CSS vengono elaborati da un compilatore in grado di sostituire determinati token con valori che dipendono dalle impostazioni del progetto. Questi token sono sempre racchiusi tra doppie o triple parentesi graffe (`{% raw %}{{TOKEN}}{% endraw %}` o `{% raw %}{{{TOKEN}}}{% endraw %}`), a seconda che le sequenze di caratteri debbano essere sottoposte a escape oppure no. Questa funzionalità può essere utile se modifichi spesso le impostazioni del progetto o se intendi riutilizzare il materiale in altri progetti.

<div class='sidenote' markdown='1'>
Puoi trovare maggiori informazioni sul linguaggio di modelli Mustache nel [manuale](https://mustache.github.io/mustache.5.html).
</div>

Qualsiasi impostazione di *game.project* può essere usata come token. Ad esempio, se vuoi usare il valore `Width` della sezione `Display`:

![Sezione Display](/manuals/images/html5/html5_display.png)

Apri *game.project* come testo e controlla `[section_name]` e il nome del campo che vuoi usare. Puoi quindi utilizzarlo come token: `{% raw %}{{section_name.field}}{% endraw %}` o `{% raw %}{{{section_name.field}}}{% endraw %}`.

![Sezione Display](/manuals/images/html5/html5_game_project.png)

Ad esempio, nel codice JavaScript del modello HTML:

```javascript
function doSomething() {
    var x = {% raw %}{{display.width}}{% endraw %};
    // ...
}
```

Sono disponibili anche i seguenti token personalizzati:

DEFOLD_SPLASH_IMAGE
: Inserisce il nome del file dell'immagine iniziale oppure `false` se `html5.splash_image` in *game.project* è vuoto


```css
{% raw %}{{#DEFOLD_SPLASH_IMAGE}}{% endraw %}
		background-image: url("{% raw %}{{DEFOLD_SPLASH_IMAGE}}{% endraw %}");
{% raw %}{{/DEFOLD_SPLASH_IMAGE}}{% endraw %}
```

exe-name
: Il nome del progetto senza simboli non consentiti


DEFOLD_CUSTOM_CSS_INLINE
: Il punto in cui viene inserito direttamente il contenuto del file CSS specificato nelle impostazioni di *game.project*.


```html
<style>
{% raw %}{{{DEFOLD_CUSTOM_CSS_INLINE}}}{% endraw %}
</style>
```

<div class='important' markdown='1'>
È importante che questo blocco inline compaia prima del caricamento dello script principale dell'applicazione. Poiché include tag HTML, questa macro deve essere racchiusa tra triple parentesi graffe `{% raw %}{{{TOKEN}}}{% endraw %}` per evitare che le sequenze di caratteri vengano sottoposte a escape.
</div>

DEFOLD_SCALE_MODE_IS_DOWNSCALE_FIT
: Questo token è `true` se `html5.scale_mode` è `Downscale Fit`.

DEFOLD_SCALE_MODE_IS_FIT
: Questo token è `true` se `html5.scale_mode` è `Fit`.

DEFOLD_SCALE_MODE_IS_NO_SCALE
: Questo token è `true` se `html5.scale_mode` è `No Scale`.

DEFOLD_SCALE_MODE_IS_STRETCH
: Questo token è `true` se `html5.scale_mode` è `Stretch`.

DEFOLD_HEAP_SIZE
: La dimensione dell'heap specificata in *game.project* con `html5.heap_size`, convertita in byte.

DEFOLD_ENGINE_ARGUMENTS
: Gli argomenti del motore specificati in *game.project* con `html5.engine_arguments`, separati dal simbolo `,`.

build-timestamp
: Il timestamp della build corrente in secondi.


## Parametri aggiuntivi {#extra-parameters}

Se crei un modello personalizzato, puoi modificare i parametri del caricatore del motore assegnando valori nell'oggetto globale `CUSTOM_PARAMETERS`. Il modello integrato fornisce un blocco `<script id="engine-setup">` intenzionalmente vuoto per queste personalizzazioni.
<div class='important' markdown='1'>
Mantieni il blocco `engine-setup` dopo lo script che carica `dmloader.js` e prima del blocco `engine-start` che chiama `EngineLoader.load()`.
</div>
Ad esempio:

```html
    <script id="engine-setup" type="text/javascript">
        CUSTOM_PARAMETERS.disable_context_menu = false;
        CUSTOM_PARAMETERS.unsupported_webgl_callback = function() {
            console.log("Oh-oh. WebGL not supported...");
        };
    </script>
```

`CUSTOM_PARAMETERS` può contenere, tra gli altri, i seguenti campi:

```
'archive_location_filter':
    Filter function that will run for each archive path.

'unsupported_webgl_callback':
    Function that is called if WebGL is not supported.

'engine_arguments':
    List of arguments (strings) that will be passed to the engine.

'custom_heap_size':
    Number of bytes specifying the memory heap size.

'disable_context_menu':
    Disables the right-click context menu on the canvas element if true.

'retry_time':
    Pause in seconds before retry file loading after error.

'retry_count':
    How many attempts we do when trying to download a file.

'can_not_download_file_callback':
    Function that is called if you can't download file after 'retry_count' attempts.

'resize_window_callback':
    Function that is called when resize/orientationchanges/focus events happened

'start_success':
    Function that is called just before main is called upon successful load.

'update_progress':
    Function that is called as progress is updated. Parameter progress is updated 0-100.
```

## Operazioni sui file in HTML5 {#file-operations-in-html5}

Le build HTML5 supportano operazioni sui file come `sys.save()`, `sys.load()` e `io.open()`, ma la gestione interna di queste operazioni è diversa rispetto alle altre piattaforme. Quando JavaScript viene eseguito in un browser, non esiste un vero e proprio concetto di file system e l'accesso ai file locali è bloccato per motivi di sicurezza. Emscripten (e quindi Defold) usa invece [IndexedDB](https://developer.mozilla.org/en-US/docs/Web/API/IndexedDB_API/Using_IndexedDB), un database interno al browser che permette di memorizzare dati in modo persistente, per creare un file system virtuale nel browser. La differenza importante rispetto all'accesso al file system sulle altre piattaforme è che può esserci un leggero ritardo tra la scrittura in un file e l'effettiva memorizzazione della modifica nel database. La console per sviluppatori del browser consente generalmente di ispezionare il contenuto di IndexedDB.


## Passaggio di argomenti a un gioco HTML5 {#passing-arguments-to-an-html5-game}

A volte è necessario fornire argomenti aggiuntivi a un gioco prima o durante il suo avvio. Potrebbe trattarsi, ad esempio, di un ID utente, di un token di sessione o del livello da caricare all'avvio del gioco. Puoi farlo in diversi modi, alcuni dei quali sono descritti qui.

### Argomenti del motore {#engine-arguments}

Puoi specificare argomenti aggiuntivi del motore durante la sua configurazione e il suo caricamento. Questi argomenti possono essere recuperati durante l'esecuzione tramite `sys.get_config_string()`. Assegna gli argomenti direttamente a `CUSTOM_PARAMETERS.engine_arguments` nel blocco `engine-setup` di `index.html`:


```html
    <script id="engine-setup" type="text/javascript">
        CUSTOM_PARAMETERS.engine_arguments = [
            "--config=example.foo1=bar1",
            "--config=example.foo2=bar2"
        ];
    </script>
```

L'assegnazione di un nuovo array sostituisce tutti gli argomenti del motore configurati in *game.project*. Per conservare questi argomenti e aggiungerne un altro, usa invece `CUSTOM_PARAMETERS.engine_arguments.push("--config=example.foo3=bar3")`.

Puoi anche aggiungere `--config=example.foo1=bar1, --config=example.foo2=bar2` al campo *Engine Arguments* nella sezione HTML5 di *game.project*. I valori separati da virgole vengono aggiunti a `CUSTOM_PARAMETERS.engine_arguments` nel file `dmloader.js` generato.

Durante l'esecuzione, puoi ottenere i valori in questo modo:

```lua
local foo1 = sys.get_config_string("example.foo1")
local foo2 = sys.get_config_string("example.foo2")
print(foo1) -- bar1
print(foo2) -- bar2
```


### Argomenti di query nell'URL {#query-arguments-in-the-url}

Puoi passare argomenti come parametri di query nell'URL della pagina e leggerli durante l'esecuzione:

```
https://www.mygame.com/index.html?foo1=bar1&foo2=bar2
```

```lua
local url = html5.run("window.location")
print(url)
```

Una funzione ausiliaria completa per ottenere tutti i parametri di query come tabella Lua:

```lua
local function get_query_parameters()
    local url = html5.run("window.location")
    -- get the query part of the url (the bit after ?)
    local query = url:match(".*?(.*)")
    if not query then
        return {}
    end

    local params = {}
    -- iterate over all key value pairs
    for kvp in query:gmatch("([^&]+)") do
        local key, value = kvp:match("(.+)=(.+)")
        params[key] = value
    end
    return params
end

function init(self)
    local params = get_query_parameters()
    print(params.foo1) -- bar1
end
```

## Ottimizzazioni {#optimizations}
I giochi HTML5 hanno generalmente requisiti rigorosi in termini di dimensioni del download iniziale, tempo di avvio e utilizzo della memoria, affinché si carichino rapidamente e funzionino bene anche su dispositivi poco potenti e con connessioni Internet lente. Per ottimizzare un gioco HTML5, si consiglia di concentrarsi sui seguenti aspetti:

* [Utilizzo della memoria](/it/manuals/optimization-memory)
* [Dimensioni del motore](/it/manuals/optimization-size)
* [Dimensioni del gioco](/it/manuals/optimization-size)

## FAQ
{% include shared/it/html5-faq.md %}