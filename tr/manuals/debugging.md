---
brief: Bu kılavuz, Defold'da bulunan hata ayıklama olanaklarını açıklar.
github: https://github.com/defold/doc
layout: manual
locale: tr
title: Defold'da hata ayıklama
toc:
- anchor: debugging
  title: Hata ayıklama
---

# Hata ayıklama {#debugging}

Defold, inceleme özelliğine sahip bütünleşik bir Lua hata ayıklayıcısı (debugger) içerir. Yerleşik [profil çıkarma (profiling) araçlarıyla](/tr/manuals/profiling) birlikte, oyun mantığınızdaki yazılım hatalarının nedenini bulmanıza veya performans sorunlarını analiz etmenize yardımcı olabilecek güçlü bir araçtır. Defold, motorun kendisinin çöktüğü nadir durumlar için de çökme günlükleri sağlar.

Lua hata ayıklayıcısı, yerel hata ayıklama ve görüntüsüz (headless) derlemelerde kullanılabilir. Yayıma yönelik derlemeler ve Web derlemeleri, hata ayıklayıcı bağlamayı desteklemez.

* [Oyun mantığınızda hata ayıklama](/tr/manuals/debugging-game-logic) hakkında daha fazla bilgi edinin.
* [VS Code kurulum örneği](/tr/manuals/debugging-game-logic/#vs-code) dahil [harici bir hata ayıklayıcıyı bağlama](/tr/manuals/debugging-game-logic/#native-dap-connections) hakkında bilgi edinin.
* [Yerel kodda (native code) hata ayıklama](/tr/manuals/debugging-native-code) hakkında daha fazla bilgi edinin.
* Lua veya geliştirme araçlarıyla [oyun penceresini MP4 dosyasına kaydetme](/tr/manuals/recording) hakkında bilgi edinin.