
# 对话框名称框样式
style namebox:
    xalign 0.5
    xoffset 0
    yoffset -50
    ypadding 0
    xpadding 0
    background None

style ruby_text:
    size 18
    yoffset -30

## flash effects
transform flash_burst:
    alpha 0.9
    linear 0.05 alpha 0

transform flash_slow:
    alpha 0.8
    linear 0.15 alpha 0

transform power_die_out:
    block:
        # 第1次
        alpha 0.9
        linear 0.05 alpha 0
        pause 1.0
        # 第2次
        alpha 0.7
        linear 0.04 alpha 0
        pause 2.5
        # 第3次
        alpha 0.5
        linear 0.03 alpha 0
        pause 1.0
        repeat

## mosaic
transform mosaic_blur_at(z=1.0, x=0.5, y=1.0, alpha_val=1.0):
    xalign x
    yalign y
    zoom z
    alpha alpha_val
    block:
        blur 15
        pause 0.1
        blur 20
        pause 0.2
        blur 12
        pause 0.1
        repeat

transform mosaic_blur_slight:
    block:
        blur 15
        pause 0.3
        blur 10
        pause 0.5
        blur 15
        pause 0.2
        repeat

transform breathe_blur(blur_in=1.5, blur_out=1.0, hold=0.5):
    blur 0.0
    linear blur_in blur 15.0
    pause hold
    linear blur_out blur 0.0
    repeat

transform breathe_light(cycle=2.0):
    alpha 1.0
    linear cycle alpha 0.6
    pause 1.0
    linear cycle alpha 1.0
    repeat

transform blur_to_clear(duration=2.0):
    blur 20.0
    linear duration blur 0.0

transform clear_to_blur(duration=2.0):
    blur 0.0
    linear duration blur 20.0

# nightmare
transform nightmare_breath:
    blur 0
    linear 1.0 blur 5
    linear 0.8 blur 0
    repeat

transform nightmare_twist:
    rotate 0
    linear 0.5 rotate 3
    linear 0.3 rotate -3
    linear 0.4 rotate 0
    repeat

##shake
transform glitch_shake:
    block:
        xoffset renpy.random.randint(-12, 12)
        yoffset renpy.random.randint(-8, 8)
        pause 0.02
        xoffset renpy.random.randint(-8, 8)
        yoffset renpy.random.randint(-5, 5)
        pause 0.02
        xoffset renpy.random.randint(-4, 4)
        yoffset renpy.random.randint(-3, 3)
        pause 0.02
        xoffset 0
        yoffset 0
        pause renpy.random.uniform(0.05, 0.15)
        repeat
# ========================================
# 剪影效果（非动态）
# ========================================
# 基础剪影
transform silhouette(color="#000", alpha=1.0):
    matrixcolor SaturationMatrix(0.0) * TintMatrix(color)
    alpha alpha

# 预设剪影
transform sil_black:
    matrixcolor SaturationMatrix(0.0) * TintMatrix("#000")

transform sil_red:
    matrixcolor SaturationMatrix(0.0) * TintMatrix("#800000")

transform sil_blue:
    matrixcolor SaturationMatrix(0.0) * TintMatrix("#000080")

transform sil_white:
    matrixcolor SaturationMatrix(0.0) * TintMatrix("#ffffff")

transform sil_gray:
    matrixcolor SaturationMatrix(0.0) * TintMatrix("#444444")

# 带透明度
transform sil_black_50:
    matrixcolor SaturationMatrix(0.0) * TintMatrix("#000")
    alpha 0.5

transform sil_black_30:
    matrixcolor SaturationMatrix(0.0) * TintMatrix("#000")
    alpha 0.3

# ========================================
# 剪影渐变原图
# ========================================
# 从剪影渐变到原图（可自定义颜色和时长）
transform silhouette_to_normal(color="#000", duration=1.0):
    matrixcolor SaturationMatrix(0.0) * TintMatrix(color)
    linear duration matrixcolor IdentityMatrix()

# 从原图渐变到剪影
transform normal_to_silhouette(color="#000", duration=1.0):
    matrixcolor IdentityMatrix()
    linear duration matrixcolor SaturationMatrix(0.0) * TintMatrix(color)

# 预设：黑色剪影→原图
transform sil_to_normal:
    matrixcolor SaturationMatrix(0.0) * TintMatrix("#000")
    linear 1.0 matrixcolor IdentityMatrix()

# 预设：原图→黑色剪影
transform normal_to_sil:
    matrixcolor IdentityMatrix()
    linear 1.0 matrixcolor SaturationMatrix(0.0) * TintMatrix("#000")

# 预设：红色剪影→原图
transform red_sil_to_normal:
    matrixcolor SaturationMatrix(0.0) * TintMatrix("#800000")
    linear 1.0 matrixcolor IdentityMatrix()

# 预设：原图→红色剪影
transform normal_to_red_sil:
    matrixcolor IdentityMatrix()
    linear 1.0 matrixcolor SaturationMatrix(0.0) * TintMatrix("#800000")

# memory
screen memory_overlay():
    zorder 100  # 确保在最上层
    add Solid("#000000"):
        size (config.screen_width, config.screen_height)
        alpha 0.4

# ========================================
# 开场文字（主菜单前显示）
# ========================================
screen opening_disclaimer(txt):
    vbox:
        xalign 0.5
        yalign 0.5
        text txt:
            color "#FFFFFF"
            size 28
            text_align 0.5
            xalign 0.5
            xmaximum 1400
            line_spacing 10
            outlines [(2, "#000000", 0, 0)]

screen darkness_overlay():
    layer "master"  # 只在 master 层（背景、立绘、CG），不影响 screens
    zorder 100  # 在立绘之上
    # 黑色半透明层
    add Solid("#000000"):
        alpha darkness_level
        xsize config.screen_width
        ysize config.screen_height

# ========================================
# 快捷菜单（始终显示，但主菜单不显示）
# ========================================
screen quick_menu():
    zorder 200  # 确保在最上层
    
    # 只在游戏中显示，主菜单时隐藏
    if not renpy.get_screen("main_menu"):
        # 底部快捷按钮（贴底）
        hbox:
            xalign 0.5
            yalign 1.0
            yanchor 1.0
            spacing 30
            yoffset -10  # 稍微留点间距

            textbutton _("保存") action ShowMenu("save"):
                style "quick_text_button"

            textbutton _("读取") action ShowMenu("load"):
                style "quick_text_button"

            textbutton _("回看") action ShowMenu("history"):
                style "quick_text_button"

            textbutton _("设置") action ShowMenu("preferences"):
                style "quick_text_button"

            textbutton _("主菜单") action MainMenu():
                style "quick_text_button"

# 让 quick_menu 始终显示（开始游戏或读取存档后）
init python:
    config.overlay_screens.append("quick_menu")

# ========================================
# 对话框屏幕
# ========================================
# 渐变背景 shader（底部实心黑 → 顶部半透明）
init python:
    renpy.register_shader("textbox.gradient",
        variables="""
            uniform vec4 u_color_top;
            uniform vec4 u_color_bottom;
            uniform vec2 u_model_size;
            varying float v_position;
            attribute vec4 a_position;
        """,
        vertex_300="""
            v_position = a_position.y;
        """,
        fragment_300="""
            float t = v_position / u_model_size.y;
            gl_FragColor *= mix(u_color_bottom, u_color_top, t);
        """
    )

    # 垂直渐变shader（smoothstep版本：底部实心，顶部渐变到透明）
    renpy.register_shader("gradient.vertical_smooth",
        variables="""
            uniform vec4 u_color;
            uniform float u_gradient_size;
            uniform vec2 u_model_size;
            varying vec2 v_tex_coord;
        """,
        fragment_300="""
            float y = v_tex_coord.y;
            float gradient = u_gradient_size / u_model_size.y;
            
            // 顶部渐变到透明（y=1是顶部，y=0是底部）
            float alpha = smoothstep(0.0, gradient, y);
            
            gl_FragColor = u_color * alpha;
        """
    )

    # 水平渐变shader - 中间实心版（左右透明→中间实心→左右透明）
    renpy.register_shader("gradient.horizontal",
        variables="""
            uniform vec4 u_color;
            uniform float u_gradient_size;
            uniform vec2 u_model_size;
            varying vec2 v_tex_coord;
        """,
        fragment_300="""
            float x = v_tex_coord.x;
            float gradient = u_gradient_size / u_model_size.x;
            
            // 左侧渐变：0→gradient
            float left = smoothstep(0.0, gradient, x);
            // 右侧渐变：1-gradient→1
            float right = smoothstep(1.0, 1.0 - gradient, x);
            
            float alpha = left * right;
            gl_FragColor = u_color * alpha;
        """
    )

    # 水平渐变shader - 左侧实心版（左侧实心，右侧渐变）
    renpy.register_shader("gradient.horizontal_left",
        variables="""
            uniform vec4 u_color;
            uniform float u_gradient_size;
            uniform vec2 u_model_size;
            uniform float u_base_alpha;
            varying vec2 v_tex_coord;
        """,
        fragment_300="""
            float x = v_tex_coord.x;
            float gradient = u_gradient_size / u_model_size.x;
            
            // 右侧渐变到透明（左侧实心）
            float alpha = 1.0 - smoothstep(1.0 - gradient, 1.0, x);
            
            // 应用基础透明度
            gl_FragColor = u_color * (alpha * u_base_alpha);
        """
    )

# 垂直渐变背景 transform（smoothstep版本）
transform textbox_gradient(color="#000000F0", gradient_size=100):
    mesh True
    shader "gradient.vertical_smooth"
    u_color Color(color).rgba
    u_gradient_size gradient_size

# 水平渐变背景 transform - 中间实心版（用于choice）
transform gradient_h_bg(color="#000000C0", gradient_size=50):
    mesh True
    shader "gradient.horizontal"
    u_color Color(color).rgba
    u_gradient_size gradient_size

# 水平渐变背景 transform - 左侧实心版（用于namebox）
transform gradient_h_left(color="#000000C0", gradient_size=50, base_alpha=1.0):
    mesh True
    shader "gradient.horizontal_left"
    u_color Color(color).rgba
    u_gradient_size gradient_size
    u_base_alpha base_alpha

screen say(who, what):
    style_prefix "say"

    # 全屏容器
    fixed:
        xsize config.screen_width
        ysize config.screen_height
        yoffset 40

        # 垂直渐变背景（smoothstep版本：底部实心，顶部渐变）
        add Solid("#000000", xsize=config.screen_width, ysize=350):
            at textbox_gradient("#000000E0", 200)
            yalign 1.0
            yanchor 1.0
            yoffset 0
        # 对话框窗口（固定高度，从上往下）- 有namebox时左对齐
        if who:
            window:
                id "window"
                xalign 0.0
                yalign 1.0
                yanchor 1.0
                yoffset -100  # 整体上移
                xoffset int(config.screen_width * 0.15)
                background None
                ysize 180  # 固定高度

                vbox:
                    xalign 0.0
                    yalign 0.0  # 从上往下（不是居中）
                    spacing 10

                    # Namebox with gradient background (left solid, right gradient)
                    fixed:
                        xsize 300
                        ysize 40
                        
                        # 左侧实心，右侧渐变背景
                        # add Solid("#FFFFFF", xsize=150, ysize=40):
                        #     at gradient_h_left("#FFFFFF", 150, base_alpha=0.8)
                        #     alpha 0.1
                        
                        # 名称文字（左对齐）
                        text who:
                            style "name_text"
                            xalign 0.0
                            yalign 0.5
                            xoffset 0  # 左侧留白
                            min_width 300

                    text what id "what" style "say_dialogue"

        # 对话框窗口（固定高度，从上往下）- 无namebox时居中，但上方留相同padding
        else:
            window:
                id "window"
                yalign 1.0
                yanchor 1.0
                yoffset -100
                ysize 180  # 与有namebox时相同高度
                xsize config.screen_width
                background None
                left_padding 0
                right_padding 0

                text what id "what":
                    style None  # 禁用默认style，避免xalign 0.0覆盖
                    size 32
                    xalign 0.5  # 居中
                    yalign 0.0  # 从上往下
                    yoffset 70  # 上方留白（namebox高度40 + spacing 10）
                    text_align 0.5  # 居中
                    xmaximum 1500
                    color "#FFFFFF"
                    outlines []

screen say_transparent(who, what):
    window:
        id "window"
        background None
        xoffset 100
        yoffset -50 
        xalign 0.5
        yalign 1.0
        
        if who:
            vbox:
                text who:
                    color "#000000"
                    style "name_text"
                text what id "what":
                    color "#000000"
                    style "say_dialogue"
        else:
            text what id "what":
                color "#000000"
                size 32
                xalign 0.5
        
# ========================================
# 选项屏幕（居中）
# ========================================
screen choice(items):
    style_prefix "choice"

    # 居中容器
    vbox:
        xalign 0.5
        yalign 0.5
        spacing 15

        for i in items:
            # 每个选项：水平渐变背景 + 文字按钮
            fixed:
                xsize 450
                ysize 70
                
                # 水平渐变背景层（中间实心，左右透明）
                add Solid("#000000C0", xsize=420, ysize=55):
                    at gradient_h_bg("#000000C0", 60)
                    xalign 0.5
                    yalign 0.5
                
                # 文字按钮层
                textbutton i.caption action i.action:
                    xalign 0.5
                    yalign 0.5
                    background None
                    hover_background None
                    text_style "choice_button_text"
                    mouse "True"

# 选项按钮样式
style choice_button:
    xalign 0.5
    xpadding 40
    ypadding 15
    background None
    hover_background None
    xminimum 300

style choice_button_text:
    font "fonts/SourceHanSerifSC-Bold.otf"
    color "#FFFFFF"
    hover_color "#FFFFFF33"
    size 30
    text_align 0.5
    xalign 0.5

transform text_fade(delay=0, duration=2.0):
    alpha 0.0
    pause delay
    linear duration alpha 1.0
# ========================================
# 自定义主菜单
# ========================================
screen main_menu():
    # 播放背景音乐
    on "show" action Play("music", "audio/main_menu.mp3", loop=True)
    
    # 背景图
    add "images/bg/under_sky_main.png"
    text "See You Again":
        at text_fade(delay=2.0, duration=5.0)
        anchor (0.5, 1.0)
        align (0.5, 1.0)
        offset (0, -800)
        font "fonts/HuiWenMinCho.ttf"
        size 80
        color "#FFFFFFF0"
        outlines [(1.5, "#00000080", 1, 1)]
    
    text "HONKAI STAR RAIL PHAINAXA FANGAME / AUTHOR: ARY & AAAOI":
        anchor (0.5, 1.0)
        align (0.5, 1.0)
        offset (0, -30)
        font "fonts/HuiWenMinCho.ttf"
        size 20
        color "#FFFFFFF0"
        outlines [(0.5, "#00000080", 1, 1)]

    # 菜单按钮容器（居中）
    vbox:
        xalign 0.5
        yalign 0.6
        spacing 20
        
        # 开始游戏
        textbutton _("开始游戏"):
            action Jump("new_game")
            style "main_menu_button"
        
        # 读取存档
        textbutton _("读取存档"):
            action ShowMenu("load")
            style "main_menu_button"
        
        # CG 画廊
        textbutton _("CG 画廊"):
            action Jump("cg_gallery")
            style "main_menu_button"

        # 设置
        textbutton _("设置"):
            action ShowMenu("preferences")
            style "main_menu_button"
        
        # 退出游戏
        textbutton _("退出游戏"):
            action Quit(confirm=True)
            style "main_menu_button"
    


# ========================================
# CG 画廊页面
# ========================================
screen cg_gallery_screen():
    tag menu
    modal True
    
    # 背景
    add "images/bg/bg_gods.jpg"
    
    # 半透明遮罩（更不透明）
    # add "#000000C0"
    
    # 标题
    text _("CG 画廊"):
        xalign 0.5
        yalign 0.08
        color "#FFFFFF"
        size 36
        bold True
    
    # 进度显示
    text "[get_unlocked_cg_count()] / [get_total_cg_count()]":
        xalign 0.5
        yalign 0.14
        color "#FFFFFF"
        size 20
    
    # CG 网格
    grid 4 3:
        xalign 0.5
        yalign 0.55
        spacing 30
        
        for cg in CG_LIST:
            $ unlocked = is_cg_unlocked(cg["id"])
            
            button:
                xsize 350
                ysize 250
                background "#00000080"
                hover_background "#FFFFFF40"
                action (Show("cg_viewer", cg_image=cg["image"], cg_name=cg["name"]) if unlocked else NullAction())
                
                has vbox:
                    xalign 0.5
                    yalign 0.5
                    spacing 10
                    
                    if unlocked:
                        # 已解锁：显示缩略图
                        add cg["thumbnail"]:
                            xalign 0.5
                            xsize 300
                            fit "contain"
                        
                        text cg["name"]:
                            xalign 0.5
                            color "#FFFFFF"
                            size 18
                    else:
                        # 未解锁：显示占位文字
                        text _("未解锁"):
                            xalign 0.5
                            yalign 0.5
                            color "#FFFFFF"
                            size 24
                        
                        text cg["description"]:
                            xalign 0.5
                            color "#FFFFFF80"
                            size 16
    
    # 返回按钮
    textbutton _("返回"):
        xalign 0.5
        yalign 0.95
        style "main_menu_button"
        action Return()


# ========================================
# CG 查看器（全屏查看，纯图片）
# ========================================
screen cg_viewer(cg_image, cg_name):
    tag menu
    modal True
    
    # 全屏显示 CG（纯图片，无文字）
    add cg_image:
        xalign 0.5
        yalign 0.5
        fit "contain"
    
    # 点击任意位置返回
    button:
        xfill True
        yfill True
        background None
        action Show("cg_gallery_screen")


# 主菜单按钮样式
style main_menu_button:
    xalign 0.5
    ypadding 10
    xpadding 40
    background None
    hover_background None
    xsize 200

style main_menu_button_text:
    font "fonts/SourceHanSerifSC-Bold.otf"
    color "#000000"
    hover_color "#00000030"
    size 28
    xalign 0.5

screen big_text(txt):
    text txt:
        size 40
        bold False
        xalign 0.5
        yalign 0.5
        color "#FFFFFF"


# ========================================
# 确认对话框
# ========================================
screen yesno_prompt(message, yes_action, no_action):
    modal True

    window:
        xalign 0.5
        yalign 0.5
        xsize 500
        background "#000000CC"
        xpadding 30
        ypadding 30

        vbox:
            xalign 0.5
            yalign 0.5
            spacing 20

            text message:
                color "#FFFFFF"
                size 24
                text_align 0.5
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 20

                textbutton _("确定"):
                    action yes_action
                    style "confirm_button"

                textbutton _("取消"):
                    action no_action
                    style "confirm_button"


style confirm_button:
    xpadding 20
    ypadding 10
    background "#00000080"
    hover_background "#FFFFFF40"

style confirm_button_text:
    color "#FFFFFF"
    hover_color "#FFFFFF"
    size 22


# ========================================
# 历史记录屏幕
# ========================================
screen history():
    tag menu
    predict False
    
    use game_menu(_("历史")):
        frame:
            background None
            xfill True
            yfill True
            xpadding 30
            ypadding 24

            fixed:
                xfill True
                ysize 860
                yalign 0.5

                hbox:
                    xfill True
                    yfill True
                    spacing 10

                    viewport id "history_vp":
                        xsize 1600
                        yfill True
                        yinitial 1.0
                        mousewheel True
                        draggable True
                        pagekeys True

                        vbox:
                            spacing 10

                            if _history_list:
                                for h in _history_list:
                                    $ who_text = "" if h.who is None else str(h.who)
                                    $ what_text = "" if h.what is None else str(h.what)

                                    if who_text:
                                        text who_text:
                                            style "name_text"
                                            size 26
                                            xmaximum 1560

                                    text what_text:
                                        style "say_dialogue"
                                        size 28
                                        color "#FFFFFF"
                                        xmaximum 1560

                                    if h.rollback_identifier:
                                        textbutton _("回退到此处"):
                                            action RollbackToIdentifier(h.rollback_identifier)
                                            style "quick_text_button"

                                    null height 8
                            else:
                                text _("暂无对话记录"):
                                    color "#FFFFFF"
                                    size 24

                    vbar:
                        value YScrollValue("history_vp")
                        style "history_vbar"


# ========================================
# 存档界面
# ========================================
screen save():
    tag menu

    use file_slots(_("保存"))


screen load():
    tag menu

    use file_slots(_("读取"))


screen file_slots(title):
    default page_name_value = FilePageNameInputValue()

    use game_menu(title):

        fixed:
            order_reverse True

            # 页面按钮
            hbox:
                style_prefix "page"
                xalign 0.5
                yalign 1.0

                spacing 8

                for i in range(1, 10):
                    textbutton "[i]" action FilePage(i)

            # 存档槽
            grid 3 2:
                style_prefix "slot"
                xalign 0.5
                yalign 0.5

                spacing 10

                for i in range(6):
                    $ slot = i + 1

                    button:
                        action FileAction(slot)
                        xysize (275, 200)

                        vbox:
                            xfill True

                            # 缩略图占满
                            add FileScreenshot(slot):
                                xsize 275
                                ysize 140
                                xalign 0.5
                                yalign 0.5
                                fit "contain"

                            hbox:
                                xfill True
                                spacing 5

                                # 时间和名称
                                vbox:
                                    xalign 0.2
                                    text FileTime(slot, format=_("{#file_time}%Y-%m-%d %H:%M"), empty=_("空槽")):
                                        style "slot_time_text"
                                        size 18

                                    text FileSaveName(slot):
                                        style "slot_name_text"
                                        size 14

                                # 删除按钮
                                if FileLoadable(slot):
                                    textbutton "×":
                                        style "delete_button"
                                        action FileDelete(slot)
                                        xalign 1.0

                        key "save_delete" action FileDelete(slot)

style say_window:
    xalign 0.5
    yalign 1.0
    xfill True
    yminimum 200
    background None  # 背景由渐变层提供
    left_padding 80
    right_padding 200
    top_padding 25
    bottom_padding 25
    yoffset 0

style say_dialogue:
    font "fonts/SourceHanSerifSC-Medium.otf"
    text_align 0.0  # 文字居左
    xalign 0.0
    size 32
    xmaximum 1500
    xfill True

style name_text:
    font "fonts/SourceHanSerifSC-Bold.otf"
    color "#FFFFFF"
    size 32
    bold False
    text_align 0.0
    xalign 0.0
    yalign 0.5
    min_width 50  # 给 namebox 留足够的宽度

# 快捷按钮样式（纯文字，无背景）
style quick_text_button:
    background None
    hover_background None
    xpadding 10

style quick_text_button_text:
    color "#8c8c8c"
    hover_color "#FFFFFF"
    size 18

# 存档槽样式
style slot_button:
    xsize 275
    ysize 200
    background "#00000040"
    hover_background "#FFFFFF40"

style slot_time_text:
    color "#FFFFFF"
    size 16
    xalign 0.0
    text_align 0.0

style slot_name_text:
    color "#FFFFFF80"
    size 12
    xalign 0.5

# 删除按钮样式
style delete_button:
    background None
    hover_background "#ff000040"
    xpadding 10
    ypadding 4

style delete_button_text:
    color "#FFFFFF60"
    hover_color "#ff6666"
    size 24
    xalign 0.5

style page_button:
    xpadding 14
    ypadding 6
    background "#00000080"
    hover_background "#FFFFFF40"

style page_button_text:
    color "#FFFFFF"
    hover_color "#FFFFFF"
    size 28

style history_vbar is vscrollbar
style history_vbar:
    xsize 16
    unscrollable "hide"
    base_bar Solid("#FFFFFF20")
    thumb Solid("#FFFFFFCC")


# ========================================
# 游戏菜单框架
# ========================================
screen game_menu(title):
    layer "overlay"

    add "images/bg/bg_gods.jpg"

    frame:
        style "game_menu_outer_frame"

        has hbox

        # 标题
        frame:
            style "game_menu_navigation_frame"

            vbox:
                style_prefix "game_menu_nav"
                yoffset 40
                xfill True
                xalign 0.5

                button:
                    style "game_menu_nav_button"
                    action Return()

                    fixed:
                        xfill True
                        ysize 56

                        text _("返回"):
                            style "game_menu_nav_button_text"
                            xalign 0.5
                            yalign 0.5

                button:
                    style "game_menu_nav_button"
                    action ShowMenu("history")
                    selected (title == _("历史"))

                    fixed:
                        xfill True
                        ysize 56

                        if title == _("历史"):
                            add Solid("#FFFFFFCC"):
                                xsize 3
                                ysize 56
                                xalign 0.0

                        text _("回看"):
                            style "game_menu_nav_button_text"
                            xalign 0.5
                            yalign 0.5

                button:
                    style "game_menu_nav_button"
                    action ShowMenu("preferences")
                    selected (title == _("设置"))

                    fixed:
                        xfill True
                        ysize 56

                        if title == _("设置"):
                            add Solid("#FFFFFFCC"):
                                xsize 3
                                ysize 56
                                xalign 0.0

                        text _("设置"):
                            style "game_menu_nav_button_text"
                            xalign 0.5
                            yalign 0.5

        frame:
            style "game_menu_content_frame"

            transclude


style game_menu_outer_frame:
    xfill True
    yfill True
    background "#00000080"

style game_menu_navigation_frame:
    xsize 200
    yfill True
    background "#00000040"

style game_menu_content_frame:
    xfill True
    yfill True
    background None

style game_menu_nav_button:
    xfill True
    ypadding 2
    background None
    hover_background "#FFFFFF22"
    selected_background "#FFFFFF38"
    selected_hover_background "#FFFFFF45"

style game_menu_nav_button_text:
    color "#FFFFFFB0"
    hover_color "#FFFFFF"
    selected_color "#FFFFFF"
    size 24
    xalign 0.5
    text_align 0.5


# ========================================
# 设置界面
# ========================================
screen preferences():
    tag menu

    use game_menu(_("设置")):

        vbox:
            xalign 0.5
            yalign 0.5
            spacing 40

            # 文字速度
            vbox:
                spacing 10
                text _("文字速度"):
                    style "pref_label"
                bar value Preference("text speed") style "pref_bar"

            # 音乐音量
            vbox:
                spacing 10
                text _("音乐音量"):
                    style "pref_label"
                bar value Preference("music volume") style "pref_bar"

            # 音效音量
            vbox:
                spacing 10
                text _("音效音量"):
                    style "pref_label"
                bar value Preference("sound volume") style "pref_bar"

            # 语言选择
            vbox:
                spacing 10
                text _("语言"):
                    style "pref_label"
                hbox:
                    xalign 0.5
                    spacing 20
                    textbutton _("中文") action Language("schinese") style "pref_textbutton"
                    textbutton _("英文") action Language("english") style "pref_textbutton"


style pref_label:
    color "#FFFFFF"
    size 22
    min_width 200
    xalign 0.5

style pref_bar:
    xsize 400
    ysize 30
    left_bar "#FFFFFF40"
    right_bar "#00000080"
    hover_left_bar "#FFFFFF80"
    hover_right_bar "#00000040"
    thumb "#FFFFFF"
    hover_thumb "#FFFFFF"
    thumb_offset 10

style pref_slider:
    xsize 400
    ysize 30

style pref_textbutton:
    xminimum 190
    xpadding 8
    ypadding 4
    hover_background "#FFFFFF40"

style pref_textbutton_text:
    color "#FFFFFF"
    size 18
    xalign 0.5

# ========================================
# 简洁书信页面
# ========================================
screen simple_letter(letter_text="", title=""):
    modal True
    
    # 点击关闭（放在最底层）
    button:
        xysize (config.screen_width, config.screen_height)
        background None
        action Return()
        keysym "dismiss"
    
    # 半透明黑色遮罩（全屏）
    add Solid("#00000080")
    
    # 文字容器（无边框）
    vbox:
        xalign 0.5
        yalign 0.5
        xsize 900
        spacing 30
        
        # 标题
        if title:
            text title:
                size 32
                color "#ffffff"
                xalign 0.0
                bold True
                # font "fonts/SourceHanSerifSC-Bold.otf"
            
            # 分隔线
            add Solid("#ffffff", xsize=700, ysize=1)
        
        # 书信正文（直接显示，不用viewport）
        text letter_text:
            size 26
            color "#ffffff"
            line_spacing 15
            justify True
            first_indent 0
            text_align 0.0
            xalign 0.0
            # font "fonts/SourceHanSerifSC-Medium.otf"
    
    # 关闭提示
    text "点击任意位置关闭":
        xalign 0.5
        yalign 0.95
        size 20
        color "#cccccc"

# ========================================
# 闪烁转场效果
# ========================================
# 普通闪烁
transform flicker:
    alpha 1.0
    pause 0.1
    alpha 0.3
    pause 0.1
    alpha 1.0
    pause 0.1
    alpha 0.5
    pause 0.1
    alpha 1.0

# 快速闪烁
transform flicker_fast:
    alpha 1.0
    pause 0.05
    alpha 0.2
    pause 0.05
    alpha 1.0
    pause 0.05
    alpha 0.4
    pause 0.05
    alpha 1.0
    pause 0.05
    alpha 0.1
    pause 0.05
    alpha 1.0

# 红色闪烁（受伤效果）
transform flicker_red:
    matrixcolor IdentityMatrix()
    pause 0.1
    matrixcolor TintMatrix("#f00")
    pause 0.1
    matrixcolor IdentityMatrix()
    pause 0.1
    matrixcolor TintMatrix("#f00")
    pause 0.1
    matrixcolor IdentityMatrix()

# 白色闪烁（闪光效果）
transform flicker_white:
    matrixcolor IdentityMatrix()
    pause 0.05
    matrixcolor TintMatrix("#fff")
    pause 0.05
    matrixcolor IdentityMatrix()
    pause 0.05
    matrixcolor TintMatrix("#fff")
    pause 0.05
    matrixcolor IdentityMatrix()

# 故障闪烁
transform glitch_flicker:
    parallel:
        alpha 1.0
        pause 0.05
        alpha 0.7
        pause 0.05
        alpha 1.0
    parallel:
        xoffset 0
        pause 0.05
        xoffset 5
        pause 0.05
        xoffset -5
        pause 0.05
        xoffset 0

# ========================================
# 滚动报幕系统
# ========================================
init python:
    # 左侧CG列表（phainon）
    LEFT_CGS = [
        "images/characters/phainon-little-normal.png",
        "images/characters/phainon-little-sadsmile.png",
        "images/characters/phainon-normal.png",
        "images/characters/phainon-firm.png",
        "images/characters/phainon-sad.png",
        "images/characters/phainon2-normal.png",
        "images/characters/phainon2-cool.png",
        "images/characters/phainon2-smile.png",
    ]
    
    # 右侧CG列表（anaxa）
    RIGHT_CGS = [
        "images/characters/anaxa-scholar-normal.png",
        "images/characters/anaxa-scholar-smile.png",
        "images/characters/anaxa-normal.png",
        "images/characters/anaxa-smile.png",
        "images/characters/anaxa-shock.png",
        "images/characters/anaxa2-normal.png",
        "images/characters/anaxa2-normal02.png",
        "images/characters/anaxa2-smile.png",
    ]

# CG淡入效果（平滑）
transform cg_fadein:
    alpha 0.0
    pause 0.2
    linear 1.5 alpha 1.0

# CG淡出再淡入（模拟dissolve）
transform cg_dissolve:
    alpha 1.0
    linear 0.8 alpha 0.0
    pause 0.1
    alpha 0.0
    linear 1.0 alpha 1.0

# CG交叉淡化（真正的dissolve效果）
transform cg_crossfade(duration=1.0):
    on show:
        alpha 0.0
        linear duration alpha 1.0
    on replace:
        alpha 0.0
        linear duration alpha 1.0

# 滚动动画
transform credits_scroll_up(duration=60.0):
    subpixel True
    yoffset 720
    linear duration yoffset -4000

# 滚动报幕界面（CG带dissolve效果）
screen credits_rolling():
    modal True
    tag menu
    
    # 黑色背景
    add Solid("#000")
    
    # 左侧CG区域（自动切换，带dissolve）
    frame:
        xpos 50
        ypos 50
        xsize 350
        ysize 620
        background None
        padding (0, 0, 0, 0)
        
        default left_idx = 0
        
        # 当前CG
        add LEFT_CGS[left_idx]:
            xsize 350
            ysize 620
            at cg_crossfade(1.0)
        
        # 每8秒切换CG
        timer 8.0 repeat True action [
            SetScreenVariable("left_idx", (left_idx + 1) % len(LEFT_CGS)),
        ]
    
    # 右侧CG区域（自动切换，带dissolve）
    frame:
        xpos 1520
        ypos 50
        xsize 350
        ysize 620
        background None
        padding (0, 0, 0, 0)
        
        default right_idx = 0
        
        # 当前CG
        add RIGHT_CGS[right_idx]:
            xsize 350
            ysize 620
            at cg_crossfade(1.0)
        
        # 每8秒切换CG（错开4秒）
        timer 8.0 repeat True action [
            SetScreenVariable("right_idx", (right_idx + 1) % len(RIGHT_CGS)),
        ]
    
    # 中间滚动文字
    frame:
        xpos 450
        ypos 0
        xsize 1020
        ysize 720
        background None
        
        viewport:
            xfill True
            yfill True
            draggable False
            mousewheel False
            
            vbox:
                xalign 0.5
                spacing 20
                at credits_scroll_up(60.0)
                
                text _(" ") size 120
                
                # 主标题
                text _("《游戏名称》") xalign 0.5 size 64 color "#ffd700"
                
                null height 80
                
                # STAFF
                text _("—— STAFF ——") xalign 0.5 size 32 color "#888"
                
                null height 40
                
                text _("策划") xalign 0.5 size 24 color "#aaa"
                text "XXX" xalign 0.5 size 32
                
                null height 30
                
                text _("剧本") xalign 0.5 size 24 color "#aaa"
                text "XXX" xalign 0.5 size 32
                
                null height 30
                
                text _("程序") xalign 0.5 size 24 color "#aaa"
                text "XXX" xalign 0.5 size 32
                
                null height 30
                
                text _("美术") xalign 0.5 size 24 color "#aaa"
                text "XXX" xalign 0.5 size 32
                
                null height 30
                
                text _("音乐") xalign 0.5 size 24 color "#aaa"
                text "XXX" xalign 0.5 size 32
                
                null height 60
                
                # CAST
                text _("—— CAST ——") xalign 0.5 size 32 color "#888"
                
                null height 40
                
                text _("主角") xalign 0.5 size 24 color "#aaa"
                text "CV: XXX" xalign 0.5 size 28
                
                null height 20
                
                text _("配角A") xalign 0.5 size 24 color "#aaa"
                text "CV: YYY" xalign 0.5 size 28
                
                null height 60
                
                # 特别感谢
                text _("—— SPECIAL THANKS ——") xalign 0.5 size 32 color "#888"
                
                null height 40
                
                text _("感谢所有支持我们的玩家") xalign 0.5 size 28
                text _("感谢测试组的辛勤付出") xalign 0.5 size 28
                
                null height 100
                
                # 结尾
                text _("感谢游玩") xalign 0.5 size 48 color "#ffd700"
                
                text _(" ") size 120
                text _(" ") size 120
                text _(" ") size 120
    
    # 跳过按钮
    button:
        background None
        xysize (1920, 720)
        action [Stop("music"), Hide("credits_rolling")]
    
    # 提示
    text _("点击任意位置结束"):
        xalign 0.5
        yalign 0.97
        size 16
        color "#444"

# 调用示例
# label show_credits:
#     play music "ending.ogg" fadein 2.0
#     call screen credits_rolling
#     stop music fadeout 2.0
#     return

# ========================================
# OP风格报幕（CG+文字交替浮现）
# ========================================
# 文字淡入
transform text_fadein:
    alpha 0.0
    linear 1.0 alpha 1.0

# CG淡入
transform cg_slide_left:
    xalign 0.0
    yalign 1.0
    alpha 0.0
    parallel:
        linear 1.0 alpha 1.0

transform cg_slide_right:
    xalign 1.0
    yalign 1.0
    alpha 0.0
    parallel:
        linear 1.0 alpha 1.0

transform right_text_fadein:
    xalign 0.75
    yalign 0.5
    alpha 0.0
    linear 1.0 alpha 1.0
