---
brief: Bu kılavuz, Defold düzenleyicisinin bir eklentinin kullanıcılarına otomatik tamamlama sunabilmesi için betik API tanımının nasıl oluşturulacağını açıklar.
github: https://github.com/defold/doc
layout: manual
locale: tr
title: Yerel kod eklentilerine düzenleyicide otomatik tamamlama ekleme
toc:
- Yerel kod eklentileri için otomatik tamamlama
- Betik API tanımı oluşturma
- Örnekler
---

# Yerel kod eklentileri için otomatik tamamlama

Defold düzenleyicisi, tüm Defold API işlevleri için otomatik tamamlama (auto-complete) önerileri sunar ve betiklerinizin gerektirdiği Lua modülleri için öneriler oluşturur. Ancak düzenleyici, yerel kod eklentilerinin (native extension) sunduğu işlevler için kendiliğinden otomatik tamamlama önerileri sunamaz. Bir yerel kod eklentisi, kendi API'si için de otomatik tamamlama önerilerini etkinleştirmek üzere ayrı bir dosyada API tanımı sağlayabilir.


## Betik API tanımı oluşturma

Betik API tanım dosyasının uzantısı `.script_api` şeklindedir. Dosyanın [YAML biçiminde](https://yaml.org/) olması ve eklenti dosyalarıyla birlikte bulunması gerekir. Betik API tanımı için beklenen biçim şöyledir:

```yml
- name: The name of the extension
  type: table
  desc: Extension description
  members:
  - name: Name of the first member
    type: Member type
    desc: Member description
    # if member type is "function"
    parameters:
    - name: Name of the first parameter
      type: Parameter type
      desc: Parameter description
    - name: Name of the second parameter
      type: Parameter type
      desc: Parameter description
    # if member type is "function"
    returns:
    - name: Name of first return value
      type: Return value type
      desc: Return value description
    examples:
    - desc: First example of member usage
    - desc: Second example of member usage

  - name: Name of the second member
    ...
```

Türler, `table, string , boolean, number, function` türlerinden herhangi biri olabilir. Bir değer birden fazla türde olabiliyorsa `[type1, type2, type3]` biçiminde yazılır.
<div class='sidenote' markdown='1'>
Türler şu anda düzenleyicide gösterilmez. Düzenleyici tür bilgilerini göstermeyi desteklediğinde kullanılabilmeleri için bunları yine de belirtmeniz önerilir.
</div>

## Örnekler

Gerçek kullanım örnekleri için aşağıdaki projelere bakın:

* [Facebook eklentisi](https://github.com/defold/extension-facebook/tree/master/facebook/api)
* [WebView eklentisi](https://github.com/defold/extension-webview/blob/master/webview/api/webview.script_api)