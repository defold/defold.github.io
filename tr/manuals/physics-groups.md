---
brief: Fizik motoru, fizik nesnelerinizi gruplandırmanızı ve nasıl çarpışacaklarını filtrelemenizi sağlar.
github: https://github.com/defold/doc
layout: manual
locale: tr
title: Defold'da çarpışma grupları
toc:
- Grup ve maske
- Çarpışmaları algılama
---

# Grup ve maske

Fizik motoru, fizik nesnelerinizi gruplandırmanızı ve nasıl çarpışacaklarını filtrelemenizi sağlar. Bu işlem, adlandırılmış _çarpışma grupları_ (collision groups) aracılığıyla yapılır. Oluşturduğunuz her çarpışma nesnesinin (collision object) diğer nesnelerle nasıl çarpışacağını iki özellik kontrol eder: *Group* ve *Mask*.

İki nesne arasındaki bir çarpışmanın algılanabilmesi için her iki nesnenin de *Mask* alanında diğer nesnenin grubunu belirtmesi gerekir.

![Fizik çarpışma grubu](/manuals/images/physics/collision_group.png)

*Mask* alanı birden fazla grup adı içerebilir; bu da karmaşık etkileşim senaryolarına olanak tanır.

## Çarpışmaları algılama
Grup ve maske ayarları birbiriyle eşleşen iki çarpışma nesnesi çarpıştığında fizik motoru, oyunlarda çarpışmalara tepki vermek için kullanılabilecek [çarpışma iletileri](/tr/manuals/physics-messages) üretir.