---
brief: このマニュアルでは、2D グラフィックスをインポートして使用する方法を説明します。
github: https://github.com/defold/doc
layout: manual
locale: ja
title: 2D グラフィックスのインポートと使用
toc:
- anchor: importing-2d-graphics
  title: 2D グラフィックスのインポート
- anchor: creating-defold-assets
  title: Defold アセットの作成
- anchor: using-defold-assets
  title: Defold アセットの使用
---

# 2D グラフィックスのインポート {#importing-2d-graphics}

Defold は、2D ゲームでよく使われるさまざまな種類の描画用コンポーネント（component）をサポートしています。Defold では、静止したスプライト（sprite）やアニメーションするスプライト、UI コンポーネント、パーティクルエフェクト（particle effect）、タイルマップ（tile map）、ビットマップフォント（bitmap font）を作成できます。これらの描画用コンポーネントを作成するには、まず使用するグラフィックスを含む画像ファイルをインポートする必要があります。画像ファイルをインポートするには、コンピューター上のファイルシステムからファイルをドラッグし、Defold エディターの *Assets ペイン* 内の適切な場所にドロップするだけです。

![ファイルのインポート](/manuals/images/graphics/import.png)

<div class='sidenote' markdown='1'>
Defold は PNG 形式と JPEG 形式の画像をサポートしています。ほかの形式の画像は、使用する前に変換する必要があります。
</div>


## Defold アセットの作成 {#creating-defold-assets}

Defold に画像をインポートすると、その画像を使って Defold 固有のアセット（asset）を作成できます。

![アトラス](/manuals/images/icons/atlas.png) アトラス
: アトラス（atlas）には個別の画像ファイルのリストが含まれ、それらの画像はより大きなテクスチャ画像に自動的にまとめられます。アトラスには静止画像と、連続した画像を切り替えるフリップブックアニメーション（flipbook animation）を構成する画像の集合である *アニメーショングループ（Animation Groups）* を含められます。

  ![アトラス](/manuals/images/graphics/atlas.png)

アトラスリソースについて詳しくは、[アトラスのマニュアル](/ja/manuals/atlas)を参照してください。

![タイルソース](/manuals/images/icons/tilesource.png) タイルソース
: タイルソース（tile source）は、小さな画像を均一なグリッドに並べて構成した画像ファイルを参照します。このように複数の画像をまとめた画像は、一般に _スプライトシート（sprite sheet）_ とも呼ばれます。タイルソースには、アニメーションの最初と最後のタイルで定義するフリップブックアニメーションを含められます。また、画像を使ってタイルにコリジョン形状（collision shape）を自動的に付加することもできます。

  ![タイルソース](/manuals/images/graphics/tilesource.png)

タイルソースリソースについて詳しくは、[タイルソースのマニュアル](/ja/manuals/tilesource)を参照してください。

![ビットマップフォント](/manuals/images/icons/font.png) ビットマップフォント
: ビットマップフォントは、PNG 形式のフォントシートにグリフ（glyph）を格納します。この種類のフォントは、TrueType または OpenType のフォントファイルから生成したフォントと比べてパフォーマンスは向上しませんが、任意のグラフィックス、色、影を画像に直接含められます。

ビットマップフォントについて詳しくは、[フォントのマニュアル](/ja/manuals/font/#bitmap-bmfonts)を参照してください。

  ![BMfont](/manuals/images/font/bm_font.png)


## Defold アセットの使用 {#using-defold-assets}

画像をアトラスファイルとタイルソースファイルに変換すると、それらを使ってさまざまな種類の描画用コンポーネントを作成できます。

![スプライト](/manuals/images/icons/sprite.png)
: スプライトは、画面に表示する静止画像またはフリップブックアニメーションです。

  ![スプライト](/manuals/images/graphics/sprite.png)

スプライトについて詳しくは、[スプライトのマニュアル](/ja/manuals/sprite)を参照してください。

![タイルマップ](/manuals/images/icons/tilemap.png) タイルマップ
: タイルマップコンポーネントは、タイルソースから取得したタイル（画像とコリジョン形状）を組み合わせてマップを作成します。タイルマップではアトラスをソースとして使用できません。

  ![タイルマップ](/manuals/images/graphics/tilemap.png)

タイルマップについて詳しくは、[タイルマップのマニュアル](/ja/manuals/tilemap)を参照してください。

![パーティクルエフェクト](/manuals/images/icons/particlefx.png) パーティクルエフェクト
: パーティクルエミッター（particle emitter）から生成されるパーティクルは、アトラスまたはタイルソースの静止画像またはフリップブックアニメーションで構成されます。

  ![パーティクル](/manuals/images/graphics/particles.png)

パーティクルエフェクトについて詳しくは、[パーティクルエフェクトのマニュアル](/ja/manuals/particlefx)を参照してください。

![GUI](/manuals/images/icons/gui.png) GUI
: GUI のボックスノード（box node）と、円や扇形を表示するパイノード（pie node）では、アトラスやタイルソースの静止画像とフリップブックアニメーションを使用できます。

  ![GUI](/manuals/images/graphics/gui.png)

GUI について詳しくは、[GUI のマニュアル](/ja/manuals/gui)を参照してください。