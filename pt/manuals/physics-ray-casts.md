---
brief: Ray casts são usados para ler o mundo de física ao longo de um raio linear. Este manual explica como isso funciona.
github: https://github.com/defold/doc
layout: manual
locale: pt
title: Ray casts no Defold
toc:
- Ray casts
---

## Ray casts

Ray casts são usados para ler o mundo de física ao longo de um raio linear. Para lançar um raio no mundo de física, você fornece uma posição inicial e final, além de [um conjunto de grupos de colisão](/pt/manuals/physics-groups) contra os quais testar.

Se o raio atingir um objeto de física, você receberá informações sobre o objeto atingido. Raios intersectam objetos dinâmicos, cinemáticos e estáticos. Eles não interagem com gatilhos.

```lua
function update(self, dt)
  -- solicita ray cast
  local my_start = vmath.vector3(0, 0, 0)
  local my_end = vmath.vector3(100, 1000, 1000)
  local my_groups = { hash("my_group1"), hash("my_group2") }

  local result = physics.raycast(my_start, my_end, my_groups)
  if result then
      -- age sobre o acerto (veja a mensagem 'ray_cast_response' para todos os valores)
      print(result.id)
  end
end
```

<div class='sidenote' markdown='1'>
Ray casts ignoram objetos de colisão que contêm o ponto inicial do raio. Essa é uma limitação do Box2D.
</div>