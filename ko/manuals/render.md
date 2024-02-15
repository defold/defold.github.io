---
layout: manual
language: ko
github: https://github.com/defold/doc
title: Defold manual
---

# Rendering
엔진에 의해 화면에 나타나는 모든 오브젝트(sprites, models, tiles, particles, GUI nodes)는 렌더링 파이프라인에 의해 그려집니다. 이 메뉴얼은 파이프 라인이 어떻게 동작하며 이것을 어떻게 프로그래밍 하면 되는지 설명합니다.

기본적으로 Defold는 모든 2D 오브젝트를 특정 블렌딩과 적당한 Z depth로 적절하게 비트맵을 그려주므로 정렬(ordering)과 블렌딩(blending) 이상의 렌더링에 대하여 고민할 필요가 없습니다. 이 파이프라인은 대부분의 2D 게임에서 잘 동작하지만, 또 다른 특별한 요구사항이 있을 수 있습니다. Defold에서는 이런 경우에 맞춤형 렌더링 파이프라인을 작성할 수 있습니다.

## The default renderer
렌더링 파이프라인의 핵심은 렌더 스크립트(render script)입니다. 이 파일은 init(), update(), on_message() 함수를 사용하는 보통의 Lua 스크립트이며 OpenGL 렌더링 API 와 소통하는데 주로 사용됩니다. 프로젝트의 "Builtins" 폴더 안에서 기본 렌더 오브젝트("default.render")와 기본 렌더 스크립트("default.render_script")를 찾을 수 있습니다. 렌더 오브젝트는 현재의 렌더 스크립트에 대한 참조를 포함하고 있습니다.

> Defold는 휴대장치에서 OpenGL ES 2.0 기반으로 렌더링 됩니다. 데스크탑에서는 보통의 Open GL을 사용하므로 OpenGL ES 2.0에서 지원하지 않는 기능을 사용하여 쉐이더를 작성하는 것이 가능하지만 이는 데스크탑과 휴대장치간의 상호 호환을 깨트릴 수 있습니다.

![Builtin render](/manuals/images/rendering/rendering_builtins.png)

![Default render](/manuals/images/rendering/rendering_default_render.png)

커스텀 렌더러를 설정하는 방법은 아래와 같습니다.

1. "default.render" 파일과 "default.render_script" 파일을 복사합니다.
2. 복사한 파일들을 당신의 프로젝트의 아무데나 ("render" 폴더 같은 곳)에 붙여 넣기 합니다.
3. 복사한 "default.render" 파일을 연 후 (이름 바꿔도 됨) **script** 속성을 변경하여 복사한 렌더 스크립트 파일을 참조합니다.
4. *game.project* 설정 파일에서 **Bootstrap** 항목 아래의 **render** 속성을 변경하여 위에서 복사한 "default.render" 오브젝트를 참조합니다.

물론 그냥 처음부터 렌더 스크립트 파일을 새로 생성해도 되지만, Defold와 OpenGL ES 렌더링을 처음 다뤄보는 사용자라면 기존 스크립트에서 복사해서 편집하는 방식이 좋은 접근법입니다.

> 렌더 스크립트는 게임의 라이프사이클 내에서 특별한 위치에 있습니다. 자세한 내용은 [Application lifecycle](/ko/manuals/application-lifecycle) 문서에서 찾을 수 있습니다.

## Render predicates
render predicates(렌더 술어 or 조건자)는 오브젝트의 그리기 순서(draw order)를 제어할 수 있습니다. predicate는 메터리얼 태그의 선택을 기반으로 무엇을 그릴 것인지 선언합니다. 화면에 그려지는 각 오브젝트는 메터리얼을 포함하고 있으며, 오브젝트를 어떻게 정확히 화면에 그릴지, 어떤 쉐이더 프로그램을 실행할지를 제어합니다. 메터리얼에서는, 메터리얼과 연관된 한 개 이상의 태그를 지정할 수 있습니다. 이것은 게임을 빌드할 때 비트 필드(bit field)로 컴파일 되지만, 에디터상에서는 보통의 텍스트 태그로 나타납니다. 렌더 스크립트에서 한두개 렌더 predicate를 만들고 이 predicate가 속할 태그를 지정해 보세요. 마지막으로 predicate를 그릴 때에는, predicate에 지정된 목록과 일치하는 태그를 포함한 메터리얼이 있는 각 오브젝트가 그려집니다. 메터리얼에 대한 더 자세한 설명은 [Material](/ko/manuals/material) 문서에서 찾을 수 있습니다.

![Render predicate](/manuals/images/rendering/rendering_predicate.png)

## The render script
렌더 스크립트가 어떻게 동작하는지 더 이해하기 위해서 기본 내장된 스크립트를 조금 수정한 버전으로 자세히 살펴 보도록 하겠습니다. init() 이 시작되면 predicate, view, clear color를 설정하는데, 이 변수들은 실제 렌더링 중에 사용됩니다.

#### init()
```lua
function init(self)
    -- render predicate를 정의합니다. 각 predicate는 자기 스스로 드로우되고 이 드로우들 사이에서 OpenGL의 상태를 변경 할 수 있습니다.
    self.predicates = create_predicates("tile", "gui", "text", "particle", "model")

    -- Create and fill data tables will be used in update()
    local state = create_state()
    self.state = state
    local camera_world = create_camera(state, "camera_world", true)
    init_camera(camera_world, get_stretch_projection)
    local camera_gui = create_camera(state, "camera_gui")
    init_camera(camera_gui, get_gui_projection)
    update_state(state)
end
```

> 커스텀한 프로젝트 셋팅을 어떻게 정의하고 사용할지에 대한 정보는 [Project settings](/ko/manuals/project-settings) 문서에서 찾을 수 있습니다.  게임 카메라가 동작하는 방법에 대해 알고 싶다면 [Camera](/ko/manuals/camera) 문서를 참고하세요.

#### update()
update() 함수는 매 프레임 마다 호출됩니다. 이 함수는 OpenGL ES API(OpenGL Embedded Systems API)를 사용하여 실제 드로잉을 처리합니다. update() 함수에서 무슨일이 벌어지는지 이해하기 위해서는 OpenGL이 동작하는 방법을 이해해야만 합니다. OpenGL ES에는 훌륭한 리소스가 많이 있으며 https://www.khronos.org/opengles/ 공식 사이트가 이해를 위한 좋은 출발점이 될 수 있습니다.

다음 예제에는 3D 모델을 올바르게 그리는데 필요한 설정을 하는 내장 스크립트에 대한 주요사항이 포함되어 있습니다. 위에서 보았듯이, self.predicates.model predicate가 구성되고 다른 곳에서 이 predicate에 해당하는 메터리얼이 정의되어 3D 모델 컴포넌트에 반영되었습니다. update() 코드는 이 predicate에 대한 특정한 처리를 필요로 합니다.

```lua
function update(self)
    local state = self.state
     if not state.valid then
        if not update_state(state) then
            return
        end
    end

    local predicates = self.predicates
    -- clear screen buffers
    --
    render.set_depth_mask(true)
    render.set_stencil_mask(0xff)
    render.clear(state.clear_buffers)

    local camera_world = state.cameras.camera_world
    render.set_viewport(0, 0, state.window_width, state.window_height)
    render.set_view(camera_world.view)
    render.set_projection(camera_world.proj)


    -- render models
    --
    render.set_blend_func(render.BLEND_SRC_ALPHA, render.BLEND_ONE_MINUS_SRC_ALPHA)
    render.enable_state(render.STATE_CULL_FACE)
    render.enable_state(render.STATE_DEPTH_TEST)
    render.set_depth_mask(true)
    render.draw(predicates.model_pred)
    render.set_depth_mask(false)
    render.disable_state(render.STATE_DEPTH_TEST)
    render.disable_state(render.STATE_CULL_FACE)

     -- render world (sprites, tilemaps, particles etc)
     --
    render.set_blend_func(render.BLEND_SRC_ALPHA, render.BLEND_ONE_MINUS_SRC_ALPHA)
    render.enable_state(render.STATE_DEPTH_TEST)
    render.enable_state(render.STATE_STENCIL_TEST)
    render.enable_state(render.STATE_BLEND)
    render.draw(predicates.tile)
    render.draw(predicates.particle)
    render.disable_state(render.STATE_STENCIL_TEST)
    render.disable_state(render.STATE_DEPTH_TEST)

    -- debug
    render.draw_debug3d()

    -- render GUI
    --
    local camera_gui = state.cameras.camera_gui
    render.set_view(camera_gui.view)
    render.set_projection(camera_gui.proj)
    render.enable_state(render.STATE_STENCIL_TEST)
    render.draw(predicates.gui, camera_gui.frustum)
    render.draw(predicates.text, camera_gui.frustum)
    render.disable_state(render.STATE_STENCIL_TEST)
end
```

자, 이제 단순하고 직관적인 렌더 스크립트가 완성되었습니다. 이 렌더 스크립트는 매 프레임마다 동일한 방식으로 화면을 그리지만, 만약 렌더 상태(render states)를 도입하여 다른 곳에서 렌더링 파이프라인(render pipeline)을 제어하려고 한다면 어떻게 해야 할까요?

#### on_message()
이 렌더 스크립트 또한 Defold의 메세지 전달 세상에서는 보통의 시민들과 다를 바 없습니다. 그냥 렌더 스크립트에 on_message() 함수를 정의하는 것으로 게임의 다른 파트에서 렌더 스크립트의 동작에 영향을 주도록 하면 됩니다. 렌더 스크립트에 정보를 보내는 외부 오브젝트에 대한 예제로는 카메라 컴포넌트가 있습니다(자세한 내용은 [Camera](/ko/manuals/camera) 문서 참고). 카메라 포커스가 있는 카메라 컴포넌트는 자동적으로 렌더 스크립트에 view와 projection을 보내고 있습니다. 반면 일반 스크립트에서 렌더 스크립트와 통신하려면 특수한 소켓인 @render를 사용하면 됩니다.

```lua
local MSG_CLEAR_COLOR =         hash("clear_color")
local MSG_WINDOW_RESIZED =      hash("window_resized")
local MSG_SET_VIEW_PROJ =       hash("set_view_projection")

function on_message(self, message_id, message)
    if message_id == MSG_CLEAR_COLOR then
        -- 어디선가 클리어 컬러(clear color) 메세지를 보냄
        self.clear_color = message.color
    elseif message_id == MSG_SET_VIEW_PROJ then
        -- 카메라 포커스를 가진 카메라 컴포넌트가 @render 소켓으로 set_view_projection 메세지를 보냄. 렌더링의 view(그리고 사용가능한 projection)를 설정하기 위한 카메라 정보를 사용할 수 있음
        camera.view = message.view
        self.camera_projection = message.projection or vmath.matrix4()
        update_camera(camera, state)
    end
end
```

위의 렌더 스크립트와 on_message() 함수를 사용하면, 아래처럼 메세지를 보내서 clear color를  멋진 다크 스틸 블루(dark steel blue) 색깔로 바꿀 수 있습니다.

```lua
msg.post("@render:", "clear_color", { color = vmath.vector4(0.3, 0.4, 0.5, 0) })
```

## System messages
@render 소켓은 몇 가지 내장 메세지를 가지고 있습니다. 우선, 윈도우 사이즈가 변경되었을 경우 엔진이 보내주는 window_resized 메세지가 있습니다. 데스크탑에서는 게임 창 크기가 조절될 경우, 모바일에서는 orientation이 바뀔 경우 이 메세지가 전달됩니다.

```lua
local MSG_WINDOW_RESIZED =      hash("window_resized")

function on_message(self, message_id, message)
  if message_id == MSG_WINDOW_RESIZED then
    -- 윈도우가 리사이징 됨. 새 크기가 message.width와 message.height에 포함됨
    ...
  end
end
```

또한 텍스트와 선을 그릴 수 있는 메세지도 있습니다.

```lua
-- (1000, 1000)좌표까지 흰색 선을 그림
msg.post("@render:", "draw_line", { start_point = vmath.vector3(0, 0, 0), end_point = vmath.vector3(1000, 1000, 0), color = vmath.vector4(1, 1, 1, 1) } )

-- 500, 500 좌표에 텍스트 메세지를 그림
msg.post("@render:", "draw_text", { text = "Hello world!", position = vmath.vector3(500, 500, 0) } )
```

이 메세지들은 디버깅 정보를 그리기 위해 만들어졌습니다. 디버그 메세지를 출력하거나 ray_casts나 vector나 프로그래밍을 위한 개발 통계 따위를 쉽게 시각화 하는데 유용하며, 아래의 설명처럼 렌더 스크립트와 관련이 있습니다.

* draw_line 메세지를 통해 씬(scene)에 추가된 모든 선(line)들은 render.draw_debug3d() 호출에 의해 그려집니다.

* draw_text 메세지를 통해 씬(scene)에 추가된 모든 텍스트(text)들은 내장된 "system_font"로 그려집니다. 시스템 폰트는 "text" 태그가 있는 메터리얼을 가지므로 위의 렌더 스크립트 내용중에서  "self.text_pred" predicate에 그려집니다.

> toggle_profile 메세지를 @system 소켓으로 보내서 접근 할 수 있는 비주얼 프로파일러(visual profiler)는 스크립트로 처리 가능한 렌더러와는 다른 파트이므로 당신의 렌더 스크립트와는 분리되어 그려집니다.
