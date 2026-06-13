---
brief: Los ray casts se usan para leer el mundo físico a lo largo de un rayo lineal. Este manual explica cómo funciona.
github: https://github.com/defold/doc
layout: manual
locale: es
title: Ray casts en Defold
toc:
- Ray casts
---

## Ray casts

Los ray casts se usan para leer el mundo físico a lo largo de un rayo lineal. Para lanzar un rayo en el mundo físico, proporcionas una posición inicial y final, además de [un conjunto de grupos de colisión](/es/manuals/physics-groups) contra los que hacer la prueba.

Si el rayo alcanza un objeto físico, recibirás información sobre el objeto alcanzado. Los rayos se intersecan con objetos dinámicos, cinemáticos y estáticos. No interactúan con triggers.

```lua
function update(self, dt)
  -- solicitar un ray cast
  local my_start = vmath.vector3(0, 0, 0)
  local my_end = vmath.vector3(100, 1000, 1000)
  local my_groups = { hash("my_group1"), hash("my_group2") }

  local result = physics.raycast(my_start, my_end, my_groups)
  if result then
      -- actuar sobre el impacto (consulta el mensaje 'ray_cast_response' para ver todos los valores)
      print(result.id)
  end
end
```

<div class='sidenote' markdown='1'>
Los ray casts ignorarán los objetos de colisión que contengan el punto de inicio del rayo. Esta es una limitación de Box2D.
</div>