---
brief: Bu kılavuz, 2B grafiklerin nasıl içe aktarılacağını ve kullanılacağını açıklar.
github: https://github.com/defold/doc
layout: manual
locale: tr
title: 2B grafikleri içe aktarma ve kullanma
toc:
- 2B grafikleri içe aktarma
- Defold varlıkları oluşturma
- Defold varlıklarını kullanma
---

# 2B grafikleri içe aktarma

Defold, 2B oyunlarda sık kullanılan birçok görsel bileşen (component) türünü destekler. Defold ile durağan ve animasyonlu sprite bileşenleri, kullanıcı arayüzü (UI) bileşenleri, parçacık efektleri, karo haritaları ve bit eşlem yazı tipleri oluşturabilirsiniz. Bu görsel bileşenlerden herhangi birini oluşturabilmek için önce kullanmak istediğiniz grafikleri içeren görüntü dosyalarını içe aktarmanız gerekir. Görüntü dosyalarını içe aktarmak için dosyaları bilgisayarınızdaki dosya sisteminden sürükleyip Defold düzenleyicisindeki *Assets panelinde* uygun bir yere bırakmanız yeterlidir.

![Dosyaları içe aktarma](/manuals/images/graphics/import.png)

<div class='sidenote' markdown='1'>
Defold, PNG ve JPEG görüntü biçimlerindeki görüntüleri destekler. Diğer görüntü biçimlerinin kullanılmadan önce dönüştürülmesi gerekir.
</div>


## Defold varlıkları oluşturma

Görüntüler Defold'a içe aktarıldıktan sonra Defold'a özgü varlıklar (asset) oluşturmak için kullanılabilir:

![atlas](/manuals/images/icons/atlas.png) Atlas
: Atlas, daha büyük bir doku (texture) görüntüsünde otomatik olarak birleştirilen ayrı görüntü dosyalarının bir listesini içerir. Atlaslar durağan görüntüler ve birlikte bir kare dizisi animasyonu (flipbook animation) oluşturan görüntü kümeleri olan animasyon grupları (*Animation Groups*) içerebilir.

  ![atlas](/manuals/images/graphics/atlas.png)

Atlas kaynağı hakkında daha fazla bilgi için [Atlas kılavuzuna](/tr/manuals/atlas) bakın.

![karo kaynağı](/manuals/images/icons/tilesource.png) Karo kaynağı
: Karo kaynağı (tile source), eşit aralıklı bir ızgara üzerinde sıralanmış daha küçük alt görüntülerden oluşacak şekilde önceden hazırlanmış bir görüntü dosyasına başvurur. Bu tür birleşik görüntüler için yaygın olarak kullanılan başka bir terim de _sprite sayfası_ (sprite sheet) ifadesidir. Karo kaynakları, animasyonun ilk ve son karosuyla tanımlanan kare dizisi animasyonları içerebilir. Karolara otomatik olarak çarpışma şekilleri eklemek için bir görüntü kullanmak da mümkündür.

  ![karo kaynağı](/manuals/images/graphics/tilesource.png)

Karo kaynağı hakkında daha fazla bilgi için [Karo kaynağı kılavuzuna](/tr/manuals/tilesource) bakın.

![bit eşlem yazı tipi](/manuals/images/icons/font.png) Bit eşlem yazı tipi
: Bit eşlem yazı tipinin (bitmap font) glifleri (glyph), PNG biçimindeki bir yazı tipi sayfasında bulunur. Bu tür yazı tipleri, TrueType veya OpenType yazı tipi dosyalarından oluşturulan yazı tiplerine göre performans artışı sağlamaz; ancak doğrudan görüntü içinde istenilen grafikleri, renklendirmeleri ve gölgeleri içerebilir.

Bit eşlem yazı tipleri hakkında daha fazla bilgi için [Yazı tipleri kılavuzuna](/tr/manuals/font/#bitmap-bmfonts) bakın.

  ![BMfont](/manuals/images/font/bm_font.png)


## Defold varlıklarını kullanma

Görüntüleri Atlas ve Tile Source dosyalarına dönüştürdükten sonra bunları çeşitli görsel bileşen türleri oluşturmak için kullanabilirsiniz:

![sprite](/manuals/images/icons/sprite.png)
: Sprite bileşeni, ekranda gösterilen durağan bir görüntü veya kare dizisi animasyonudur.

  ![sprite](/manuals/images/graphics/sprite.png)

Sprite bileşenleri hakkında daha fazla bilgi için [Sprite kılavuzuna](/tr/manuals/sprite) bakın.

![karo haritası](/manuals/images/icons/tilemap.png) Karo haritası
: Karo haritası (tilemap) bileşeni, bir karo kaynağından gelen karoları (görüntü ve çarpışma şekilleri) bir araya getirerek bir harita oluşturur. Karo haritaları atlas kaynaklarını kullanamaz.

  ![karo haritası](/manuals/images/graphics/tilemap.png)

Karo haritaları hakkında daha fazla bilgi için [Karo haritası kılavuzuna](/tr/manuals/tilemap) bakın.

![parçacık efekti](/manuals/images/icons/particlefx.png) Parçacık efekti
: Bir parçacık yayıcısından (emitter) oluşturulan parçacıklar, bir atlas veya karo kaynağındaki durağan bir görüntüden ya da kare dizisi animasyonundan oluşur.

  ![parçacıklar](/manuals/images/graphics/particles.png)

Parçacık efektleri hakkında daha fazla bilgi için [Parçacık efekti kılavuzuna](/tr/manuals/particlefx) bakın.

![GUI](/manuals/images/icons/gui.png) GUI
: GUI kutu düğümleri ve daire dilimi düğümleri, atlaslardaki ve karo kaynaklarındaki durağan görüntüleri ve kare dizisi animasyonlarını kullanabilir.

  ![GUI](/manuals/images/graphics/gui.png)

GUI hakkında daha fazla bilgi için [GUI kılavuzuna](/tr/manuals/gui) bakın.