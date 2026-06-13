---
brief: Este manual describe cómo depurar una build usando Android Studio.
github: https://github.com/defold/doc
layout: manual
locale: es
title: Depuración en Android
toc:
- Depuración en Android
- Android Studio
- Notas
- Carpeta de trabajo de Native Extension
---

# Depuración en Android

Aquí describimos cómo depurar una build usando [Android Studio](https://developer.android.com/studio/), el IDE oficial para el sistema operativo Android de Google.


## Android Studio

* Prepara el bundle configurando la opción `android.debuggable` en *game.project*

	![android.debuggable](/manuals/images/extensions/debugging/android/game_project_debuggable.png)

* Crea el bundle de la app en modo debug en una carpeta de tu elección.

	![bundle_android](/manuals/images/extensions/debugging/android/bundle_android.png)

* Inicia [Android Studio](https://developer.android.com/studio/)

* Elige `Profile or debug APK`

	![debug_apk](/manuals/images/extensions/debugging/android/android_profile_or_debug.png)

* Elige el bundle APK que acabas de crear

	![select_apk](/manuals/images/extensions/debugging/android/android_select_apk.png)

* Selecciona el archivo `.so` principal y asegúrate de que tenga símbolos de depuración

	![select_so](/manuals/images/extensions/debugging/android/android_missing_symbols.png)

* Si no los tiene, sube un archivo `.so` sin strip (`unstripped`). (el tamaño es de unos 20mb)

* Los mapeos de rutas ayudan a reasignar las rutas individuales desde donde se creó el ejecutable (en la nube) a una carpeta real en tu disco local.

* Selecciona el archivo .so, luego agrega un mapeo a tu disco local

	![path_mapping1](/manuals/images/extensions/debugging/android/path_mappings_android.png)

	![path_mapping2](/manuals/images/extensions/debugging/android/path_mappings_android2.png)

* Si tienes acceso al código fuente del motor, agrega también un mapeo de ruta para eso.

* Asegúrate de hacer checkout de la versión que estás depurando actualmente

	defold$ git checkout 1.2.148

* Presiona `Apply changes`

* Ahora deberías ver el código fuente mapeado en tu proyecto

	![source](/manuals/images/extensions/debugging/android/source_mappings_android.png)

* Agrega un breakpoint

	![breakpoint](/manuals/images/extensions/debugging/android/breakpoint_android.png)

* Presiona `Run` -> `Debug "Appname"` e invoca el código donde esperas detenerte

	![breakpoint](/manuals/images/extensions/debugging/android/callstack_variables_android.png)

* Ahora puedes avanzar por el callstack e inspeccionar las variables


## Notas

### Carpeta de trabajo de Native Extension

Actualmente, el flujo de trabajo es un poco problemático para el desarrollo. Esto se debe a que el nombre de la carpeta de trabajo
es aleatorio en cada build, lo que invalida el mapeo de rutas en cada build.

Sin embargo, funciona bien para una sesión de depuración.

Los mapeos de rutas se almacenan en el archivo `.iml` del proyecto en el proyecto de Android Studio.

Es posible obtener la carpeta de trabajo desde el ejecutable

```sh
$ arm-linux-androideabi-readelf --string-dump=.debug_str build/armv7-android/libdmengine.so | grep /job
```

La carpeta de trabajo se nombra así: `job1298751322870374150`, cada vez con un número aleatorio.