---
brief: Ce manuel répertorie tout ce que vous rencontrez en travaillant dans Defold, avec une brève description.
github: https://github.com/defold/doc
layout: manual
locale: fr
title: Glossaire Defold
toc:
- anchor: defold-glossary
  title: Glossaire Defold
- anchor: animation-set
  title: Jeu danimations
- anchor: atlas
  title: Atlas
- anchor: builtins
  title: Ressources intégrées
- anchor: camera
  title: Caméra
- anchor: collision-object
  title: Objet de collision
- anchor: component
  title: Composant
- anchor: collection
  title: Collection
- anchor: collection-factory
  title: Factory de collection
- anchor: collection-proxy
  title: Proxy de collection
- anchor: cubemap
  title: Texture cubique
- anchor: debugging
  title: Débogage
- anchor: display-profiles
  title: Profils daffichage
- anchor: factory
  title: Factory
- anchor: font
  title: Police
- anchor: fragment-shader
  title: Shader de fragments
- anchor: gamepads
  title: Manettes de jeu
- anchor: game-object
  title: Objet de jeu
- anchor: gui
  title: GUI
- anchor: gui-script
  title: Script GUI
- anchor: hot-reload
  title: Rechargement à chaud
- anchor: input-binding
  title: Associations dentrées
- anchor: label
  title: Étiquette
- anchor: library
  title: Bibliothèque
- anchor: lua-language
  title: Langage Lua
- anchor: lua-module
  title: Module Lua
- anchor: material
  title: Matériau
- anchor: message
  title: Message
- anchor: model
  title: Modèle
- anchor: particlefx
  title: ParticleFX
- anchor: profiling
  title: Profilage
- anchor: render
  title: Rendu
- anchor: render-script
  title: Script de rendu
- anchor: script
  title: Script
- anchor: sound
  title: Son
- anchor: sprite
  title: Sprite
- anchor: texture-profiles
  title: Profils de texture
- anchor: tile-map
  title: Tilemap
- anchor: tile-source
  title: Source de tuiles
- anchor: vertex-shader
  title: Shader de sommets
---

# Glossaire Defold {#defold-glossary}

Ce glossaire donne une brève description de tous les éléments que vous rencontrez dans Defold. Dans la plupart des cas, vous trouverez un lien vers une documentation plus approfondie.

## Jeu d'animations {#animation-set}

![Jeu d'animations](/manuals/images/icons/animationset.png) Une ressource de jeu d'animations contient une liste de fichiers glTF ou d'autres fichiers .animationset dans lesquels lire les animations. Ajouter un fichier .animationset à un autre est pratique si vous partagez des sous-ensembles d'animations entre plusieurs modèles. Consultez le [manuel de l'animation de modèles](/fr/manuals/model-animation/) pour plus de détails.

## Atlas {#atlas}

![Atlas](/manuals/images/icons/atlas.png) Un atlas est un ensemble d'images distinctes regroupées dans une planche plus grande pour des raisons de performances et de mémoire. Les atlas peuvent contenir des images fixes ou des séries d'images animées image par image. Ils sont utilisés par différents composants (components) pour partager des ressources graphiques. Consultez la [documentation sur les atlas](/fr/manuals/atlas) pour plus d'informations.

## Ressources intégrées {#builtins}

![Ressources intégrées](/manuals/images/icons/builtins.png) Le dossier builtins du projet est un dossier en lecture seule qui contient des ressources utiles fournies par défaut. Vous y trouverez le moteur de rendu, le script de rendu et les matériaux par défaut, entre autres. Si vous devez personnaliser l'une de ces ressources, il vous suffit de la copier dans votre projet et de la modifier selon vos besoins.

## Caméra {#camera}

![Caméra](/manuals/images/icons/camera.png) Le composant caméra aide à déterminer quelle partie du monde de jeu (game world) doit être visible et comment elle doit être projetée. Un cas d'utilisation courant consiste à attacher une caméra à l'objet de jeu (game object) du joueur, ou à utiliser un objet de jeu distinct doté d'une caméra qui suit le joueur avec un algorithme de lissage. Consultez la [documentation sur les caméras](/fr/manuals/camera) pour plus d'informations.

## Objet de collision {#collision-object}

![Objet de collision](/manuals/images/icons/collision-object.png) Les objets de collision sont des composants qui ajoutent des propriétés physiques aux objets de jeu (comme la forme dans l'espace, le poids, le frottement et la restitution). Ces propriétés régissent les collisions de l'objet de collision avec les autres objets de collision. Les types d'objets de collision les plus courants sont les objets cinématiques, les objets dynamiques et les déclencheurs. Un objet cinématique fournit des informations détaillées sur les collisions, auxquelles vous devez réagir manuellement ; un objet dynamique est simulé automatiquement par le moteur physique pour obéir aux lois de la physique newtonienne. Les déclencheurs sont des formes simples qui détectent si d'autres formes y sont entrées ou en sont sorties. Consultez la [documentation sur la physique](/fr/manuals/physics) pour plus de détails sur leur fonctionnement.

## Composant {#component}

Les composants servent à donner aux objets de jeu une représentation et/ou des fonctionnalités particulières, comme des graphismes, des animations, un comportement programmé ou du son. Ils ne peuvent pas exister seuls et doivent être contenus dans des objets de jeu. Defold propose de nombreux types de composants. Consultez [le manuel des éléments constitutifs](/fr/manuals/building-blocks) pour une description des composants.

## Collection {#collection}

![Collection](/manuals/images/icons/collection.png) Les collections sont le mécanisme de Defold pour créer des modèles, appelés « prefabs » dans d'autres moteurs, qui permettent de réutiliser des hiérarchies d'objets de jeu. Les collections sont des structures arborescentes qui contiennent des objets de jeu et d'autres collections. Une collection est toujours stockée dans un fichier et intégrée au jeu soit de manière statique, en la plaçant manuellement dans l'éditeur, soit de manière dynamique, en l'instanciant. Consultez [le manuel des éléments constitutifs](/fr/manuals/building-blocks) pour une description des collections.

## Factory de collection {#collection-factory}

![Factory de collection](/manuals/images/icons/collection-factory.png) Un composant collection factory sert à instancier dynamiquement des hiérarchies d'objets de jeu dans un jeu en cours d'exécution. Consultez le [manuel des factories de collection](/fr/manuals/collection-factory) pour plus de détails.

## Proxy de collection {#collection-proxy}

![Collection](/manuals/images/icons/collection.png) Un proxy de collection (collection proxy) sert à charger et à activer des collections à la volée pendant l'exécution d'une application ou d'un jeu. Les proxys de collection sont le plus souvent utilisés pour charger les niveaux au moment où ils vont être joués. Consultez la [documentation sur les proxys de collection](/fr/manuals/collection-proxy) pour plus de détails.

## Texture cubique {#cubemap}

![Texture cubique](/manuals/images/icons/cubemap.png) Une texture cubique (cubemap) est un type particulier de texture composé de six textures différentes appliquées sur les faces d'un cube. Elle est utile pour le rendu de boîtes de ciel et de différents types de cartes de réflexion et d'éclairage.

## Débogage {#debugging}

À un moment donné, votre jeu se comportera de manière inattendue et vous devrez trouver ce qui ne va pas. Apprendre à déboguer est tout un art et, heureusement, Defold dispose d'un débogueur intégré pour vous aider. Consultez le [manuel du débogage](/fr/manuals/debugging) pour plus d'informations.

## Profils d'affichage {#display-profiles}

![Profils d'affichage](/manuals/images/icons/display-profiles.png) Le fichier de ressource des profils d'affichage sert à définir les dispositions de l'interface graphique selon l'orientation, le rapport largeur/hauteur ou le modèle de l'appareil. Il vous aide à adapter votre interface utilisateur à tous les types d'appareils. Pour en savoir plus, consultez le [manuel des dispositions](/fr/manuals/gui-layouts).

## Factory {#factory}

![Factory](/manuals/images/icons/factory.png) Dans certaines situations, vous ne pouvez pas placer manuellement tous les objets de jeu nécessaires dans une collection : vous devez les créer dynamiquement, à la volée. Par exemple, un joueur peut tirer des balles, et chaque projectile doit être instancié dynamiquement et lancé lorsque le joueur appuie sur la gâchette. Pour créer des objets de jeu dynamiquement (à partir d'un ensemble d'objets préalloués), vous utilisez un composant factory. Consultez le [manuel des factories](/fr/manuals/factory) pour plus de détails.

## Police {#font}

![Fichier de police](/manuals/images/icons/font.png) Une ressource de police est créée à partir d'un fichier de police TrueType ou OpenType. Elle définit la taille à laquelle la police doit être rendue et le type de décoration (contour et ombre) à appliquer au rendu. Les polices sont utilisées par les composants GUI et label. Consultez le [manuel des polices](/fr/manuals/font/) pour plus de détails.

## Shader de fragments {#fragment-shader}

![Shader de fragments](/manuals/images/icons/fragment-shader.png) Il s'agit d'un programme exécuté sur le processeur graphique pour chaque pixel (fragment) d'un polygone lorsque celui-ci est dessiné à l'écran. Le shader de fragments a pour rôle de déterminer la couleur de chaque fragment obtenu. Pour cela, il effectue des calculs, des lectures de texture (une ou plusieurs), ou une combinaison de lectures et de calculs. Consultez le [manuel des shaders](/fr/manuals/shader) pour plus d'informations.

## Manettes de jeu {#gamepads}

![Manettes de jeu](/manuals/images/icons/gamepad.png) Un fichier de ressource de manettes de jeu définit comment les entrées d'un modèle précis de manette sont associées aux déclencheurs d'entrée de manette sur une plateforme donnée. Consultez le [manuel des entrées](/fr/manuals/input) pour plus de détails.

## Objet de jeu {#game-object}

![Objet de jeu](/manuals/images/icons/game-object.png) Les objets de jeu sont des objets simples qui ont leur propre durée de vie pendant l'exécution de votre jeu. Ce sont des conteneurs, généralement dotés de composants visuels ou sonores, comme un son ou un sprite. Ils peuvent également être dotés d'un comportement grâce à des composants script. Vous créez les objets de jeu et les placez dans des collections dans l'éditeur, ou vous les instanciez dynamiquement à l'exécution à l'aide de factories. Consultez [le manuel des éléments constitutifs](/fr/manuals/building-blocks) pour une description des objets de jeu.

## GUI {#gui}

![Composant GUI](/manuals/images/icons/gui.png) Un composant GUI contient des éléments utilisés pour construire des interfaces utilisateur : du texte et des blocs colorés et/ou texturés. Ces éléments peuvent être organisés en structures hiérarchiques, pilotés par des scripts et animés. Les composants GUI servent généralement à créer des affichages tête haute, des systèmes de menus et des notifications à l'écran. Ils sont contrôlés par des scripts GUI qui définissent le comportement de l'interface graphique et contrôlent les interactions de l'utilisateur avec celle-ci. Pour en savoir plus, consultez la [documentation sur les interfaces graphiques](/fr/manuals/gui).

## Script GUI {#gui-script}

![Script GUI](/manuals/images/icons/script.png) Les scripts GUI servent à contrôler le comportement des composants GUI. Ils contrôlent les animations de l'interface graphique et la façon dont l'utilisateur interagit avec elle. Consultez le [manuel de Lua dans Defold](/fr/manuals/lua) pour plus de détails sur l'utilisation des scripts Lua dans Defold.

## Rechargement à chaud {#hot-reload}

L'éditeur Defold vous permet de mettre à jour le contenu d'un jeu déjà en cours d'exécution, sur ordinateur comme sur un appareil. Cette fonctionnalité est extrêmement puissante et peut grandement améliorer le flux de travail de développement. Consultez le [manuel du rechargement à chaud](/fr/manuals/hot-reload) pour plus d'informations.

## Associations d'entrées {#input-binding}

![Associations d'entrées](/manuals/images/icons/input-binding.png) Les fichiers d'associations d'entrées définissent comment le jeu doit interpréter les entrées matérielles (souris, clavier, écran tactile et manette de jeu). Le fichier associe les entrées matérielles à des _actions_ d'entrée de haut niveau, comme "jump" et "move_forward". Dans les composants script qui écoutent les entrées, vous pouvez programmer les actions que le jeu ou l'application doit effectuer en réponse à certaines entrées. Consultez la [documentation sur les entrées](/fr/manuals/input) pour plus de détails.

## Étiquette {#label}

![Étiquette](/manuals/images/icons/label.png) Le composant label vous permet d'attacher du texte à n'importe quel objet de jeu. Il affiche à l'écran, dans l'espace du jeu, un texte rendu avec une police particulière. Consultez le [manuel des étiquettes](/fr/manuals/label) pour plus d'informations.

## Bibliothèque {#library}

![Objet de jeu](/manuals/images/icons/builtins.png) Defold vous permet de partager des données entre projets grâce à un puissant mécanisme de bibliothèques. Vous pouvez l'utiliser pour mettre en place des bibliothèques partagées accessibles depuis tous vos projets, pour vous-même ou pour toute l'équipe. Pour en savoir plus sur ce mécanisme, consultez la [documentation sur les bibliothèques](/fr/manuals/libraries).

## Langage Lua {#lua-language}

Le langage de programmation Lua est utilisé dans Defold pour créer la logique du jeu. Lua est un langage de script puissant, efficace et très compact. Il prend en charge la programmation procédurale, la programmation orientée objet, la programmation fonctionnelle, la programmation pilotée par les données et la description de données. Vous pouvez en apprendre davantage sur ce langage sur le site officiel de Lua à l'adresse https://www.lua.org/ et dans le [manuel de Lua dans Defold](/fr/manuals/lua).

## Module Lua {#lua-module}

![Module Lua](/manuals/images/icons/lua-module.png) Les modules Lua vous permettent de structurer votre projet et de créer du code de bibliothèque réutilisable. Pour en savoir plus, consultez le [manuel des modules Lua](/fr/manuals/modules/)

## Matériau {#material}

![Matériau](/manuals/images/icons/material.png) Les matériaux définissent comment les différents objets doivent être rendus en spécifiant des shaders et leurs propriétés. Consultez le [manuel des matériaux](/fr/manuals/material) pour plus d'informations.

## Message {#message}

Les composants communiquent entre eux et avec d'autres systèmes par échange de messages. Ils répondent également à un ensemble de messages prédéfinis qui les modifient ou déclenchent des actions particulières. Vous envoyez des messages pour masquer des graphismes ou donner une impulsion à des objets physiques. Le moteur utilise aussi des messages pour signaler des événements aux composants, par exemple lorsque des formes physiques entrent en collision. Le mécanisme d'échange de messages nécessite un destinataire pour chaque message envoyé. Tout élément du jeu dispose donc d'une adresse unique. Pour permettre la communication entre les objets, Defold étend Lua avec un mécanisme d'échange de messages. Defold fournit également une bibliothèque de fonctions utiles.

Par exemple, le code Lua nécessaire pour masquer un composant sprite sur un objet de jeu se présente ainsi :

```lua
msg.post("#weapon", "disable")
```

Ici, `"#weapon"` est l'adresse du composant sprite de l'objet actuel. `"disable"` est un message auquel les composants sprite répondent. Consultez la [documentation sur l'échange de messages](/fr/manuals/message-passing) pour une explication approfondie de son fonctionnement.

## Modèle {#model}

![Modèle](/manuals/images/icons/model.png) Le composant de modèle 3D peut importer dans votre jeu des ressources de maillage, de squelette et d'animation au format glTF. Consultez le [manuel des modèles](/fr/manuals/model/) pour plus d'informations.

## ParticleFX {#particlefx}

![ParticleFX](/manuals/images/icons/particlefx.png) Les particules sont très utiles pour créer de beaux effets visuels, particulièrement dans les jeux. Vous pouvez les utiliser pour créer du brouillard, de la fumée, du feu, de la pluie ou des feuilles qui tombent. Defold contient un puissant éditeur d'effets de particules qui vous permet de créer et d'ajuster des effets tout en les exécutant en temps réel dans votre jeu. La [documentation sur ParticleFX](/fr/manuals/particlefx) vous explique en détail comment cela fonctionne.

## Profilage {#profiling}

De bonnes performances sont essentielles dans les jeux, et il est indispensable de pouvoir profiler les performances et la mémoire pour mesurer le comportement de votre jeu et repérer les goulets d'étranglement ainsi que les problèmes de mémoire à corriger. Consultez le [manuel du profilage](/fr/manuals/profiling) pour plus d'informations sur les outils de profilage disponibles pour Defold.

## Rendu {#render}

![Rendu](/manuals/images/icons/render.png) Les fichiers de rendu contiennent les paramètres utilisés pour afficher le jeu à l'écran. Ils définissent le script de rendu à employer ainsi que les matériaux à utiliser. Consultez le [manuel du rendu](/fr/manuals/render/) pour plus de détails.

## Script de rendu {#render-script}

![Script de rendu](/manuals/images/icons/script.png) Un script de rendu est un script Lua qui contrôle la manière dont le jeu ou l'application doit être rendu à l'écran. Un script de rendu par défaut couvre les cas les plus courants, mais vous pouvez écrire le vôtre si vous avez besoin de modèles d'éclairage personnalisés ou d'autres effets. Consultez le [manuel du rendu](/fr/manuals/render/) pour plus de détails sur le fonctionnement du pipeline de rendu, et le [manuel de Lua dans Defold](/fr/manuals/lua) pour plus de détails sur l'utilisation des scripts Lua dans Defold.

## Script {#script}

![Script](/manuals/images/icons/script.png)  Un script est un composant qui contient un programme définissant les comportements des objets de jeu. Les scripts vous permettent de préciser les règles de votre jeu et la façon dont les objets doivent réagir aux différentes interactions (avec le joueur comme avec d'autres objets). Tous les scripts sont écrits dans le langage de programmation Lua. Pour pouvoir travailler avec Defold, vous ou un membre de votre équipe devez apprendre à programmer en Lua. Consultez le [manuel de Lua dans Defold](/fr/manuals/lua) pour une présentation de Lua et plus de détails sur l'utilisation des scripts Lua dans Defold.

## Son {#sound}

![Son](/manuals/images/icons/sound.png) Le composant son est chargé de lire un son précis. Defold prend en charge les fichiers WAV, Ogg Vorbis et Ogg Opus. La prise en charge d'Opus doit être activée dans l'App Manifest. Consultez le [manuel du son](/fr/manuals/sound) pour plus d'informations.

## Sprite {#sprite}

![Sprite](/manuals/images/icons/sprite.png) Un sprite est un composant qui ajoute des graphismes aux objets de jeu. Il affiche une image provenant soit d'une source de tuiles, soit d'un atlas. Les sprites intègrent la prise en charge de l'animation image par image et de l'animation par os. Ils sont généralement utilisés pour les personnages et les objets.

## Profils de texture {#texture-profiles}

![Profils de texture](/manuals/images/icons/texture-profiles.png) Le fichier de ressource des profils de texture sert, lors de la création de bundles, à traiter et à compresser automatiquement les données d'image (dans les atlas, les sources de tuiles, les textures cubiques et les textures autonomes utilisées pour les modèles, les interfaces graphiques, etc.). Pour en savoir plus, consultez le [manuel des profils de texture](/fr/manuals/texture-profiles).

## Tilemap {#tile-map}

![Tilemap](/manuals/images/icons/tilemap.png) Les composants tilemap affichent des images provenant d'une source de tuiles dans une ou plusieurs grilles superposées. Ils servent le plus souvent à construire les environnements de jeu : sols, murs, bâtiments et obstacles. Une tilemap peut afficher plusieurs couches alignées les unes sur les autres avec un mode de fusion donné. Cela permet, par exemple, de placer du feuillage au-dessus des tuiles d'herbe de l'arrière-plan. Il est également possible de changer dynamiquement l'image affichée dans une tuile. Vous pouvez ainsi, par exemple, détruire un pont et le rendre infranchissable en remplaçant simplement les tuiles par d'autres qui représentent le pont détruit et contiennent la forme physique correspondante. Consultez la [documentation sur les tilemaps](/fr/manuals/tilemap) pour plus d'informations.

## Source de tuiles {#tile-source}

![Source de tuiles](/manuals/images/icons/tilesource.png) Une source de tuiles décrit une texture composée de plusieurs petites images de même taille. Vous pouvez définir des animations image par image à partir d'une séquence d'images d'une source de tuiles. Les sources de tuiles peuvent aussi calculer automatiquement des formes de collision à partir des données d'image. C'est très utile pour créer des niveaux composés de tuiles avec lesquels les objets peuvent entrer en collision et interagir. Les sources de tuiles sont utilisées par les composants tilemap (ainsi que sprite et ParticleFX) pour partager des ressources graphiques. Notez que les atlas sont souvent plus adaptés que les sources de tuiles. Consultez la [documentation sur les tilemaps](/fr/manuals/tilemap) pour plus d'informations.

## Shader de sommets {#vertex-shader}

![Shader de sommets](/manuals/images/icons/vertex-shader.png) Le shader de sommets calcule la géométrie à l'écran des formes polygonales primitives d'un composant. Pour tout type de composant visuel, qu'il s'agisse d'un sprite, d'une tilemap ou d'un modèle, la forme est représentée par un ensemble de positions de sommets de polygones. Le programme du shader de sommets traite chaque sommet (dans l'espace du monde) et calcule la coordonnée résultante que doit avoir chaque sommet d'une primitive. Consultez le [manuel des shaders](/fr/manuals/shader) pour plus d'informations.