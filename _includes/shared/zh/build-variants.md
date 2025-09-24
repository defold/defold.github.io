## 构建变体

当您打包游戏时，需要选择希望使用的引擎类型。您有三个基本选项：

  * Debug
  * Release
  * Headless

这些不同版本也被称为 `构建变体`

<div class='sidenote' markdown='1'>
当您选择 <kbd>Project ▸ Build</kbd> 时，您将始终获得调试版本。
</div>

### Debug

这种类型的可执行文件通常在游戏开发过程中使用，因为它包含几个有用的调试功能：

* 分析器 - 用于收集性能和使用计数器。了解如何使用分析器，请参阅[分析器手册](/manuals/profiling/)。
* 日志记录 - 启用日志记录时，引擎将记录系统信息、警告和错误。引擎还将输出来自 Lua `print()` 函数的日志，以及使用 `dmLogInfo()`、`dmLogError()` 等的原生扩展日志记录。了解如何阅读这些日志，请参阅[游戏和系统日志手册](https://defold.com/manuals/debugging-game-and-system-logs/)。
* 热重载 - 热重载是一个强大的功能，它允许开发者在游戏运行时重新加载资源。了解如何使用此功能，请参阅[热重载手册](https://defold.com/manuals/hot-reload/)。
* 引擎服务 - 可以通过多个不同的开放 TCP 端口和服务连接到游戏调试版本并与之交互。这些服务包括热重载功能、远程日志访问和上述分析器，还包括其他远程与引擎交互的服务。在[开发者文档](https://github.com/defold/defold/blob/dev/engine/docs/DEBUG_PORTS_AND_SERVICES.md)中了解有关引擎服务的更多信息。

### Release

此变体禁用了调试功能。当游戏准备发布到应用商店或以其他方式与玩家共享时，应选择此选项。出于多种原因，不建议发布启用了调试功能的游戏：

* 调试功能在二进制文件中占用一些空间，而[尽量保持发布游戏的二进制文件大小尽可能小是一种最佳实践](https://defold.com/manuals/optimization/#optimize-application-size)。
* 调试功能也会占用一些 CPU 时间。如果用户使用低端硬件，这可能会影响游戏性能。在手机上，增加的 CPU 使用量还会导致发热和电池消耗。
* 调试功能可能会暴露游戏中不应让玩家看到的信息，无论从安全、作弊还是欺诈的角度来看。

### Headless

此可执行文件在没有图形和声音的情况下运行。这意味着您可以在 CI 服务器上运行游戏的单元/冒烟测试，甚至可以将其作为云中的游戏服务器使用。
