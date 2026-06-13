---
brief: Este manual describe cómo optimizar el uso de batería de un juego Defold.
github: https://github.com/defold/doc
layout: manual
locale: es
title: Optimizar el uso de batería de un juego Defold
toc:
- Optimizar el uso de batería
- Desactivar el acelerómetro
- Optimizaciones específicas de plataforma
- Android Device Performance Framework
---

# Optimizar el uso de batería
El uso de batería es una preocupación principalmente si tu objetivo son dispositivos móviles o portátiles. Un uso alto de CPU o GPU agotará rápidamente la batería y sobrecalentará el dispositivo.

Consulta los manuales sobre cómo [optimizar el rendimiento en runtime](/es/manuals/optimization-speed) de un juego para aprender a reducir el uso de CPU y GPU.

## Desactivar el acelerómetro
Si estás creando un juego móvil que no usa el acelerómetro del dispositivo, se recomienda [desactivarlo en *game.project*](/es/manuals/project-settings/#use-accelerometer) para reducir el número de eventos de input generados.

# Optimizaciones específicas de plataforma

## Android Device Performance Framework

Android Dynamic Performance Framework es un conjunto de API que permite a los juegos interactuar más directamente con los sistemas de energía y temperatura de los dispositivos Android. Es posible monitorear el comportamiento dinámico en sistemas Android y optimizar el rendimiento del juego a un nivel sostenible que no sobrecaliente los dispositivos. Usa la [extensión Android Dynamic Performance Framework](https://defold.com/extension-adpf/) para monitorear y optimizar el rendimiento de tu juego Defold para dispositivos Android.