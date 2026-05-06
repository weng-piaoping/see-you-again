# Ren'Py 配置文件
# 这个文件控制游戏的全局设置

## 字体设置（使用思源黑体）
init python:
    # 默认语言：简体中文
    config.default_language = "schinese"
    
    # 思源黑体简体中文版
    # 字体：Noto Sans CJK SC（思源黑体 简体）
    # 许可：OFL 1.1（免费商用）
    custom_font = "fonts/NotoSansCJKsc-Regular.otf"
    config.keymap['skip'] = []
    # 设置字体替换
    config.font_replacement_map = dict()
    config.font_replacement_map["default.ttf"] = custom_font
    config.font_replacement_map["DejaVuSans.ttf"] = custom_font

    ## 文本设置
    # 使用思源黑体
    style.default.font = custom_font
    style.default.size = 28

    # 文本速度
    config.default_text_cps = 15
    
    # 自动前进速度（秒）
    config.default_afm_time = 15  # 15秒后自动前进
    # 音量
    config.default_music_volume = 0.8
    config.default_sfx_volume = 0.8

    ## 游戏分辨率
    config.screen_width = 1920
    config.screen_height = 1080
    config.window_title = "See You Again"
    config.window_icon = "gui/window_icon.png"
    config.version = "1.0.0"

    ## 存档设置
    config.save_directory = "demo-game"
    # 关闭自动存档
    config.has_autosave = False

    ## 游戏控制
    config.rollback_enabled = True
    config.rollback_length = 100
    config.allow_skipping = True
    
    ## 历史记录
    config.history_length = 30  # 保存最近30条对话
    config.history_current_dialogue = True

    ## 开发者选项
    config.developer = "auto"
    config.debug = False
    config.menu_include_disabled = True

# 覆盖系统确认提示文字
init -1 python:
    # gui 变量
    gui.ARE_YOU_SURE = _("确定吗？")
    gui.DELETE_SAVE = _("确定要删除此存档吗？")
    gui.OVERWRITE_SAVE = _("确定要覆盖此存档吗？")
    gui.LOADING = _("读取将丢失未保存的进度。\n确定要继续吗？")
    gui.QUIT = _("确定要退出游戏吗？")
    gui.MAIN_MENU = _("确定要返回主菜单吗？\n未保存的进度将丢失。")
    gui.END_REPLAY = _("确定要结束回想吗？")
    gui.SLOW_SKIP = _("确定要开始跳过吗？")
    gui.FAST_SKIP_SEEN = _("确定要跳至下一个选项吗？")
    gui.FAST_SKIP_UNSEEN = _("确定要跳过未读对话到下一个选项吗？")

    # layout 变量（这个才是实际使用的！）
    layout.ARE_YOU_SURE = _("确定吗？")
    layout.DELETE_SAVE = _("确定要删除此存档吗？")
    layout.OVERWRITE_SAVE = _("确定要覆盖此存档吗？")
    layout.LOADING = _("读取将丢失未保存的进度。\n确定要继续吗？")
    layout.QUIT = _("确定要退出游戏吗？")
    layout.MAIN_MENU = _("确定要返回主菜单吗？\n未保存的进度将丢失。")
    layout.END_REPLAY = _("确定要结束回想吗？")
    layout.SLOW_SKIP = _("确定要开始跳过吗？")
    layout.FAST_SKIP_SEEN = _("确定要跳至下一个选项吗？")
    layout.FAST_SKIP_UNSEEN = _("确定要跳过未读对话到下一个选项吗？")


## This section contains information about how to build your project into
## distribution files.
init python:

    ## The name that's used for directories and archive files. For example, if
    ## this is 'mygame-1.0', the windows distribution will be in the
    ## directory 'mygame-1.0-win', in the 'mygame-1.0-win.zip' file.
    build.directory_name = "see-you-again-1.0"

    ## The name that's uses for executables - the program that users will run
    ## to start the game. For example, if this is 'mygame', then on Windows,
    ## users can click 'mygame.exe' to start the game.
    build.executable_name = "see-you-again"

    ## If True, Ren'Py will include update information into packages. This
    ## allows the updater to run.
    build.include_update = False

    ## File patterns:
    ##
    ## The following functions take file patterns. File patterns are case-
    ## insensitive, and matched against the path relative to the base
    ## directory, with and without a leading /. If multiple patterns match,
    ## the first is used.
    ##
    ##
    ## In a pattern:
    ##
    ## /
    ##     Is the directory separator.
    ## *
    ##     Matches all characters, except the directory separator.
    ## **
    ##     Matches all characters, including the directory separator.
    ##
    ## For example:
    ##
    ## *.txt
    ##     Matches txt files in the base directory.
    ## game/**.ogg
    ##     Matches ogg files in the game directory or any of its subdirectories.
    ## **.psd
    ##    Matches psd files anywhere in the project.

    ## Classify files as None to exclude them from the built distributions.

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    build.classify('projects.txt', None)

    ## To archive files, classify them as 'archive'.

    # build.classify('game/**.png', 'archive')
    # build.classify('game/**.jpg', 'archive')

    ## Files matching documentation patterns are duplicated in a mac app
    ## build, so they appear in both the app and the zip file.

    build.documentation('*.html')
    build.documentation('*.txt')
    
