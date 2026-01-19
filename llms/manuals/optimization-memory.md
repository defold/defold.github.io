# Optimizing memory usage {#manuals:optimization-memory}

## Texture compression
The use of texture compression will not only reduce the size of resources within your game archive, but compressed textures may also reduce the amount of GPU memory required.

## Dynamic loading
Most game have at least some content that is used infrequently. From a memory usage stand point it does not make sense to have such content loaded in memory at all times, but rather load and unload it when it is needed. This will obviously be a trade-off between having something readily accessible at the cost of runtime memory and loading something at the cost of loading time.

Defold has several different ways of loading content dynamically:

* [Collection proxies](collection-proxy.md)
* [Dynamic collection factories](collection-factory.md)
* [Dynamic factories](factory.md)
* [Live Update](live-update.md)

## Optimize component counters
Defold will allocate memory for components and resources once when a collection is created, to reduce memory fragmentation. The amount of memory that is allocated depends on the configuration of various components counters in *game.project*. Use the [profiler](profiling.md) to get accurate component and resource usage and configure your game to use max values that are closer to the real count of components and resources. This will reduce the amount of memory your game is using (refer to information about component [max count optimizations](project-settings.md)).

## Optimize GUI node count
Optimize GUI node counts by setting the max number of nodes in the GUI file to only what is needed. The `Current Nodes` field of the [GUI component properties](gui.md) will show the number of nodes used by the GUI component.

## Heap size (HTML5)
The heap size of a Defold HTML5 game can be configured from the [`heap_size` field](project-settings.md) in *game.project*. Make sure to optimize memory usage of your game and set a minimal heap size.

For small games, 32 MB is an achievable heap size. For larger games, aim for 64–128 MB. If, for example, you're at 58 MB and further optimization isn't feasible, you can settle on 64 MB without overthinking it. There’s no strict target size — it depends on the game. Just aim for smaller sizes, ideally in steps of powers of two.

To check current heap usage you can launch your game and play the game in the most "resource heavy" level or section and monitor memory usage:
```lua
if html5 then
    local mem = tonumber(html5.run("HEAP8.length") / 1024 / 1024)
    print(mem)
end
```

You can also open the developer tools of your browser and write the following in the console:
```js
HEAP8.length / 1024 / 1024
```

If the memory usage remains at 32 MB, that's great! If not, follow the steps to [optimize the size of the engine itself and large assets such as sounds and textures](optimization-size.md).