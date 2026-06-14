# script.rpy
init python:
    # CG 定义列表
    CG_LIST = [
        {
            "id": "cg_young",
            "name": _("薄荷与麦香"),
            "description": _("薄荷与麦香"),
            "image": "images/cg/cg_young.png",
            "thumbnail": "images/cg/cg_young.png"
        },
        {
            "id": "cg_gods",
            "name": _("新世界"),
            "description": _("新世界"),
            "image": "images/cg/cg_gods.png",
            "thumbnail": "images/cg/cg_gods.png"
        },
        {
            "id": "dream",
            "name": _("再会"),
            "description": _("再会"),
            "image": "images/cg/dream.png",
            "thumbnail": "images/cg/dream.png"
        },
        {
            "id": "under_sky",
            "name": _("星空之下"),
            "description": _("星空之下"),
            "image": "images/cg/under_sky.png",
            "thumbnail": "images/cg/under_sky.png"
        },
        {
            "id": "cgB-0",
            "name": _("生而为人"),
            "description": _("生而为人"),
            "image": "images/cg/cgB-0.png",
            "thumbnail": "images/cg/cgB-0.png"
        },
        {
            "id": "cgB-1",
            "name": _("无法改变的"),
            "description": _("无法改变的"),
            "image": "images/cg/cgB-1.png",
            "thumbnail": "images/cg/cgB-1.png"
        },
        {
            "id": "cgB-2",
            "name": _("终局"),
            "description": _("终局"),
            "image": "images/cg/cgB-2.png",
            "thumbnail": "images/cg/cgB-2.png"
        }, 
        {
            "id": "death",
            "name": _("死别"),
            "description": _("死别"),
            "image": "images/cg/death.png",
            "thumbnail": "images/cg/death.png"
        },
        {
            "id": "cgD1-1",
            "name": _("再度与你"),
            "description": _("再度与你"),
            "image": "images/cg/cgD1-1.png",
            "thumbnail": "images/cg/cgD1-1.png"
        },
        {
            "id": "cgD1-2",
            "name": _("与你同行的梦"),
            "description": _("与你同行的梦"),
            "image": "images/cg/cgD1-2.png",
            "thumbnail": "images/cg/cgD1-2.png"
        },
    ]
    
    # 确保已解锁 CG 集合存在
    def ensure_unlocked_set():
        """确保 persistent.unlocked_cgs 已初始化"""
        if not hasattr(persistent, "unlocked_cgs") or persistent.unlocked_cgs is None:
            persistent.unlocked_cgs = set()
    
    def unlock_cg(cg_id):
        """解锁 CG（重复解锁自动去重，不存在则忽略）"""
        ensure_unlocked_set()
        
        # 检查 CG 是否存在
        cg_exists = any(cg["id"] == cg_id for cg in CG_LIST)
        if not cg_exists:
            print(f"警告：CG '{cg_id}' 不存在，未解锁")
            return
        
        persistent.unlocked_cgs.add(cg_id)
        print(f"CG 已解锁: {cg_id}")
    
    def is_cg_unlocked(cg_id):
        """检查 CG 是否已解锁"""
        ensure_unlocked_set()
        return cg_id in persistent.unlocked_cgs
    
    def get_unlocked_cg_count():
        """获取已解锁 CG 数量"""
        ensure_unlocked_set()
        return len(persistent.unlocked_cgs)
    
    def get_total_cg_count():
        """获取 CG 总数"""
        return len(CG_LIST)

    def increase_darkness(amount=0.1):
        global darkness_level
        darkness_level = min(1.0, darkness_level + amount)
        renpy.restart_interaction()

    def decrease_darkness(amount=0.1):
        global darkness_level
        darkness_level = min(1.0, darkness_level - amount)
        renpy.restart_interaction()
    
    def glow(img, pos=0.5):
        return Transform(
            Fixed(
                Transform(img, anchor=(0.5, 1.0), ypos=1.0),
                Transform(img, zoom=1.01, matrixcolor=BrightnessMatrix(0.5), alpha=0.35, blur=50, anchor=(0.5, 1.0), ypos=1.0),
            ),
            anchor=(0.5, 1.0),
            xpos=int(config.screen_width * (0.1 + pos * 0.8)),  # 映射到10%-90%范围，避免超出屏幕
            ypos=config.screen_height,
        )

    def loop_text(texts, loop_round,interval,font="fonts/SourceHanSerifSC-Bold.otf",size=32,color="#fff"):
        i = 0
        while i < loop_round:
            for t in texts:
                renpy.show("t", what=Text(t, color=color, size=size, font=font, xalign=0.5, yalign=0.5))
                renpy.pause(interval)
                renpy.hide("t")
            i += 1

label splashscreen:
    scene black with dissolve

    show screen opening_disclaimer(_("本游戏为白厄x那刻夏CP向，仅面向喜爱厄夏CP内容的玩家\n游戏内容为基于原作崩坏·星穹铁道的同人二创独立故事线")) with dissolve
    pause 3.5
    hide screen opening_disclaimer with dissolve

    show screen opening_disclaimer(_("我们尊重原作制作组的创作内容，本游戏为完全虚构的二创独立if线\n请勿与原作故事线产生联系，感谢您的理解")) with dissolve
    pause 3.0
    hide screen opening_disclaimer with dissolve

    return

# ========================================
# 人物定义
# ========================================
define phainon = Character(_("白厄"))
define anaxa_no = Character(_("那刻夏？"))
define anaxa_letter = Character(_("那刻夏的字条"))
define phainon_letter = Character(_("白厄寄来的信"))
define anaxa_letter_notsent = Character(_("那刻夏的回信"))
define anaxa_fullname = Character(_("阿那克萨戈拉斯"))
define anaxa_teacher = Character(_("恩贝多克利斯"))
define anaxa_machine = Character(_("机巧那刻夏"))
define anaxa = Character(_("那刻夏"))
define anaxa_in_memory = Character(_("记忆中的那刻夏"))
define phainon_in_memory = Character(_("记忆中的白厄"))
define father = Character(_("熟悉的男声"))
define father_name = Character(_("希洛尼摩斯"))
define mother = Character(_("熟悉的女声"))
define mother_name = Character(_("奥妲塔"))
define friend = Character(_("儿时的玩伴"))
define narrator = Character(_(""))
define narrator_dark_anaxa = Character(
    _("那刻夏"),
    what_color="#000000",
    who_color="#000000",
    what_outlines=[],
    who_outlines=[],
    screen="say_transparent"
)

define memory_text = Character(None,
    window_yfill=True,
    window_xfill=True,
    window_background=None,
    what_slow_cps=20,
    what_color="#fff",
    what_size=40,
    what_xalign=0.5,
    what_yalign=0.5,
    window_yalign=0.5,
    what_text_align=0.5,
    what_font="fonts/SourceHanSerifSC-Bold.otf",
)
# ========================================
# 图片定义
# ========================================

# 背景图片
image bg black = "#000000"
image bg white = "#FFFFFF"
image bg red = "#2a0000"
image bg initial = "images/bg/start.png"
image bg almx = "images/bg/almx.png"
image bg top = "images/bg/top.png"
image bg window = "images/bg/window.png"
image bg office = "images/bg/office.png"
image bg sky = "images/bg/sky.png"

# 白厄立绘 - 成年版
image phainon normal = "images/characters/phainon-normal.png"
image phainon firm = "images/characters/phainon-firm.png"
image phainon sad = "images/characters/phainon-sad.png"
image phainon sadhurt = "images/characters/phainon-sad-hurt.png"

image phainon2 normal = "images/characters/phainon2-normal.png"
image phainon2 cool = "images/characters/phainon2-cool.png"
image phainon2 smile = "images/characters/phainon2-smile.png"

# 白厄立绘 - 少年版
image phainon little normal = "images/characters/phainon-little-normal.png"
image phainon little sadsmile = "images/characters/phainon-little-sadsmile.png"

# 那刻夏立绘 - 教授装
image anaxa normal = "images/characters/anaxa-normal.png"
image anaxa hurt = "images/characters/anaxa-hurt.png"
image anaxa hurt2 = "images/characters/anaxa-hurt2.png"
image anaxa eyeclose = "images/characters/anaxa-eyeclose.png"

image anaxa shock = "images/characters/anaxa-shock.png"
image anaxa smile = "images/characters/anaxa-smile.png"
image anaxa2 normal = "images/characters/anaxa2-normal.png"
image anaxa2 normal full = "images/characters/anaxa2-normal-full.png"
image anaxa2 normal02 = "images/characters/anaxa2-normal02.png"
image anaxa2 smile = "images/characters/anaxa2-smile.png"

# 那刻夏立绘 - 学者装
image anaxa scholar normal = "images/characters/anaxa-scholar-normal.png"
image anaxa scholar shock = "images/characters/anaxa-scholar-shock.png"
image anaxa scholar smile = "images/characters/anaxa-scholar-smile.png"

# 兼容旧版本（指向新立绘）
image phainon = "images/characters/phainon-normal.png"
image phainon2 = "images/characters/phainon2-normal.png"
image anaxa = "images/characters/anaxa-normal.png"
image anaxa2 = "images/characters/anaxa2-normal.png"
image phx = "images/characters/phainon-normal.png"

# 物品图标
image cerces = "images/items/cerces.png"
image kephale = "images/items/kephale.png"
image stone = "images/items/stone.png"

# CG 图片
image cg event01 = "images/cg/cg01.jpg"
image cg white = "#FFFFFF"
image cg black = "#000000"
image cg young = "images/cg/cg_young.png"
image cg gods = "images/cg/cg_gods.png"
image cg dream = "images/cg/dream.png"
image cg B-0 = "images/cg/cgB-0.png"
image cg B-1 = "images/cg/cgB-1.png"
image cg B-2 = "images/cg/cgB-2.png"
image cg D1-1 = "images/cg/cgD1-1.png"
image cg D1-2 = "images/cg/cgD1-2.png"
image cg under_sky = "images/cg/under_sky.png"
image cg death = "images/cg/death.png"
# ========================================
# 公共变量
# ========================================
default game_started = False
default story_branch = ""  # 记录剧情分支
default current_music = ""
default darkness_level = 0.0
default drawn_fortune = None
default fortune_result = None
default quiz_score = 0
# ========================================
# 游戏开始标签（Ren'Py 自动调用）
# ========================================
label start:
    # 显示主菜单
    call screen main_menu


# ========================================
# 开始新游戏
# ========================================
label new_game:
    jump prologue

# ========================================
# 序章：选择的起点
# ========================================
label prologue:
    # 显示背景（黑色）
    scene bg black
    
    # 播放音乐并记录
    $ current_music = "audio/prologue.mp3"
    play music "audio/prologue.mp3"
    # 显示背景
    scene bg white with fade
    narrator "逐火之旅伴随着刻法勒火种的回归已然走向尾声。"
    narrator "走过漫长的苦旅，见证无数的血与泪，站在创世涡心的中央——"
    narrator "白厄看见了，十一枚火种闪烁在天幕。"
    scene bg initial with dissolve
    narrator "他是走向终点的唯一幸存者。十一枚火种染过战火与鲜血，见证世界的兴衰，背负众人的愿望。"
    narrator "他的手心里是最后一枚火种，只要补全最后一块拼图——"
    narrator "就能开启再创世，拯救因黑潮死去的人们。"

    # 显示白厄立绘
    show phainon firm at left with dissolve
    phainon "……"
    show kephale at truecenter with dissolve
    menu:
        "归还火种":
            narrator "他交出刻法勒火种，十二火种里最后的拼图。"
            pass
        "打碎火种":
            narrator "他看向手中那枚火种，一种难以言喻的不安随之而来。"
            narrator "打碎它，再创世不过是一场阴谋，谎言会伴随着更大的谎言。有个声音似乎在对他说。"
            narrator "他闭上眼睛，深吸一口气，举起手中的剑——"
            narrator "咔嚓——！"
            narrator "但那枚火种纹丝不动，然后在他眼前，突然升至空中，向其余十一枚火种飞去。"
            pass
        "不归还":
            narrator "黑潮近在咫尺，即将吞没脚下最后一块净土，已经无路可退了。"
            menu:
                "归还火种":
                    narrator "他交出刻法勒火种，十二火种里最后的拼图。"
                    pass
    narrator "十二枚火种已经融合，再创世即将启动。"
    narrator "一种全新的力量在他体内涌动，如脱胎换骨后重生。"
    hide kephale with dissolve
    narrator "刻法勒的火种已归还。十二枚火种作为触媒，唯一的生还者将于这世界尽头加冕。"
    phainon "……加冕？"
    narrator "成为神明。成为这苍茫大地之上唯一的神，守望因黑潮而消失的世界。\n世界于黑潮中死亡，褪去黑潮后重生。"
    phainon "那原来的人们，我的同伴们呢？"
    narrator "最纯粹的世界需要最纯粹的生命。当生命于新的混沌中诞生，前文明便会消亡。\n这就是由十二枚火种开启的「再创世」。"
    phainon "可那并不是我想要的结局！"
    narrator "那声音突然沉默，等到再次响起时，变成了他再熟悉不过的一个语调。"
    # 显示那刻夏立绘
    show anaxa normal at right with dissolve

    anaxa_no "那么，你想改变它吗？"
    phainon "……那刻夏老师？"
    anaxa_no "白厄，你在犹豫吗？"
    phainon "……我不知道怎样才是正确的道路。一路走来，我见证太多生命的消亡。"
    phainon "所谓再创世，如果只是让这个世界再次苏醒，而因黑潮死去的生命却永远消失……"
    phainon "这绝不是我、我们，一直以来想要达成的夙愿。"
    anaxa_no "哼，如果你认为那并非正确，就去纠正它。"
    phainon "我该怎么做，那刻夏老师？"
    anaxa_no "你知道我并非真实的存在。"
    phainon "我知道，你只是我脑海里的一道思想，但我……"
    anaxa_no "我已经死去了，白厄。在神悟树庭的回廊里，你曾亲眼目睹过。"
    phainon "……"
    anaxa_no "你可以把我看作你的老师，你此时此刻最想念的人。"
    anaxa_no "但你要知道，这来自于你内心深处的思念，是借由你获得的全新力量形成的一道影子。"
    phainon "……我知道。"
    anaxa_no "很好，始终记住，遵从你内心的声音。"
    phainon "但如果能够重来一次的话……"
    anaxa_no "要重来吗？"
    # 分支选择
    menu:
        "我愿意":
            jump branch_start
        
        "……":
            phainon "……重来吗？"
            phainon "贸然选择，一步不慎或许会变成更糟糕的结局。"
            phainon "这是我们为之战斗过无数个日夜的家园，如果至少能把它留下……"
            phainon "让前人的努力结出果实，也算没有前功尽弃。"
            phainon "……我的选择正确吗？"
            anaxa_no "何为正确？遵从你内心的声音，白厄。"
            phainon "但我不想成为神明，我是以人类的姿态诞生的。我更想以人类的姿态继续见证新世界。"
            anaxa_no "看来你已经做出了选择。"
            hide anaxa with dissolve
            jump branch_end_god
        
        "留在原地":
            jump branch_stay

label branch_start:
    anaxa_no "哪怕无路可退？"
    phainon "哪怕无路可退。"
    anaxa_no "很好，不愧是我的门生。"
    phainon "请开始吧。"
    anaxa_no "请记住，你必须保守秘密，不能告诉任何一人你是时空穿越者，否则一切付出将{color=#FF0000}前功尽弃{/color}。"
    anaxa_no "你要谨慎决策，任何试图改变原本故事走向的行为，都会造成{color=#FF0000}不可逆转{/color}的后果。"
    anaxa_no "……以上就是临行嘱托。那么，再见。"
    phainon "等等……"
    hide anaxa with fade
    phainon "……"
    narrator "「那刻夏」不再言语，消失在他眼前。"
    hide phainon with dissolve
    show cg black with Dissolve(2.0)
    narrator "他不知道自己即将前往何处，落地何方。\n有且仅有的，是抓住这最后的机会，来扭转一切的执念。"
    pause 2.0
    stop music fadeout 2.0
    $ current_music = ""
    narrator "灵魂和意识开始剥离，身体变得很轻，时间成为逆流的河。"
    pause 2.0
    show screen big_text("#1 回到昨日") with Dissolve(2.0)
    pause 2.0
    hide screen big_text with dissolve
    jump chapter_01


label branch_end_god:
    narrator "原初的生命，在黑潮中死去。新生的灵魂，于黑潮中孕育。\n唯有纯粹的灵魂，能够跨越死亡的距离。"
    narrator "成为神明，抛弃曾经的名字，抛弃凡俗的肉身，才能被镌刻为真正的永恒。"
    narrator "{rb}刻法勒{/rb}{rt}{size=18}卡厄斯兰那{/size}{/rt}是这个世界的创世神。新世界的人们将始终铭记。"
    phainon "人的命运该由人来决定。"
    show screen darkness_overlay
    show black as vignette:
        alpha 0.0
        linear 2.0 alpha 0.5  # 渐暗
        pause 1.0
    pause 2.0
    $ increase_darkness(0.1)
    narrator "成为神明"
    phainon "……"
    $ increase_darkness(0.1)
    narrator "成为神明"
    phainon "我拒绝。"
    $ increase_darkness(0.1)
    narrator "成为神明"
    phainon "我拒绝！"
    narrator "成为神明"
    menu:
        "成为神明":
            pass
        "拒绝成神":
            pause 1.0
            menu:
                "成为神明":
                    pass
                "拒绝成神":
                    pause 1.0
                    menu:
                        "成为神明":
                            pass
                        "拒绝成神":
                            pause 1.0
                            menu:
                                "成为神明":
                                    pass
                                "成为神明":
                                    pass
                                "成为神明":
                                    pass
                                "成为神明":
                                    pass
                                "成为神明":
                                    pass
    $ increase_darkness(0.1)
    hide phainon firm with fade
    narrator "成为{rb}神明{/rb}{rt}{size=18}{color=#FFFFFF}黑潮{/color}{/size}{/rt}"
    $ increase_darkness(0.1)
    narrator "首先失去的是光。"
    $ increase_darkness(0.1)
    narrator "而后是触觉。"
    $ increase_darkness(0.1)
    narrator "最后是身体。"
    $ increase_darkness(0.1)
    narrator "黑潮吞噬了一切。漫无边际的黑暗里，新生的神明诞生了。"
    hide vignette
    scene bg black with dissolve
    $ increase_darkness(0.1)
    pause 2.0
    show cg black with fade
    $ decrease_darkness(0.2)
    show expression glow("phainon2 normal", 0.9) as phainon_glow with Dissolve(4.0)
    anaxa "呵，还是走到了这里啊。"
    $ decrease_darkness(0.2)
    #show expression Glow("anaxa2", xalign=0.5) with fade
    show expression glow("anaxa2 normal", 1.4) as anaxa_glow with fade
    $ decrease_darkness(0.2)
    pause 2.0
    phainon "……那刻夏老师？"
    $ decrease_darkness(0.5)
    narrator "这一刻他很确信，脑海里的那刻夏并非自己的幻想。"
    anaxa "身为创世之神，感觉如何？"
    anaxa "没有视觉，没有听觉……只有灵魂。最纯粹最一无所有的灵魂。"
    anaxa "所谓神明，最终守望这一方天地，见证新生命的诞生。"
    phainon "那刻夏老师，你是什么时候……"
    anaxa "在我死去之前，我将灵魂打碎，早已与这荒唐的世界融合。"
    anaxa "只是抛弃了肉身后，在你选择成神同样灵魂化之前，我无法与你交谈。"
    phainon "那现在，我与你一样了。"
    anaxa "呵，渎神者与神最终化为了一样的形态，现实往往比神话更具戏剧色彩。"
    phainon "……抱歉，那刻夏老师。"
    anaxa "有什么好道歉的？这是我自己的选择。"
    anaxa "以灵魂的姿态跨越死亡，无论世界发生何种变化，我都能亲自见证。"
    anaxa "那么，迟来的问候——好久不见，白厄。"
    phainon "……好久不见。我很想念你，那刻夏老师。"
    anaxa "虽然结果稍微不尽人意，倒也没那么难熬。况且，不还有你么？"
    phainon "能与您同行是我的荣幸。"
    hide screen darkness_overlay
    phainon "哪怕是以灵魂的姿态。"
    anaxa "哼，那就让我来好好教导你，该如何承担神职吧。"
    hide anaxa_glow with Dissolve(3.0)
    narrator "创世者守候这一望无尽的世界。黑潮{rb}褪去{/rb}{rt}{size=18}重生{/size}{/rt}后，它逐渐绽放出色彩。"
    narrator "被黑潮吞噬的生命留在过去，无人知晓曾经的文明。"
    show expression glow("phainon2 cool", 0.9) as phainon_glow with dissolve
    narrator "人们铭记着，{rb}刻法勒{/rb}{rt}{size=18}卡厄斯兰那{/size}{/rt}开启了创世，但未曾有一人亲自目睹过祂的面貌。\n人们的脑海里，却始终存在着创世神的影子。"
    hide phainon_glow with Dissolve(3.0)
    narrator "许多年后，那麦田一隅的回忆，已成为遥远模糊的幻象。"
    show cg black with Dissolve(2.0)
    narrator "但在卡厄斯兰那已然不存在的耳旁，始终有一道清晰无比的声音。他说——"
    hide cg black
    show cg white with Dissolve(2.0)
    show anaxa2 normal02 at right:
        alpha 0.5
    with Dissolve(2.0)
    narrator_dark_anaxa "我一直在这里。"
    pause 1.0
    hide anaxa2 normal02 with Dissolve(2.0)
    show text "{color=#000000}Ending A\n最遥远的距离{/color}" at truecenter with dissolve
    pause 2.0
    hide text with dissolve
    jump main_menu_end

label branch_end_death:
    hide phainon with Dissolve(5.0)
    $ current_music = ""
    stop music fadeout 2.0
    narrator "十二火种不再完整。"
    narrator "理性的火种下落不明。"
    scene bg initial with Dissolve(5.0)
    show phainon firm at left with dissolve
    $ current_music = "audio/prologue.mp3"
    play music "audio/prologue.mp3"
    narrator "原初的生命，在黑潮中死去。新生的灵魂，于黑潮中孕育。\n唯有纯粹的灵魂，能够跨越死亡的距离。"
    narrator "倘若十二枚火种集齐，便能成为神明，抛弃曾经的名字，抛弃凡俗的肉身，才能被镌刻为真正的永恒。"
    phainon "十二枚火种……"
    narrator "他看向天幕，眼前赫然只有十一枚火种。在刚才的时间之旅里，理性火种已不复存在。"
    show cg B-0 with Fade(1.5, 0.5, 1.5)
    $ unlock_cg("cgB-0")
    pause 2.0
    narrator "世界始于混沌，终于混沌。"
    show cg B-1 with Fade(1.5, 0.5, 1.5)
    $ unlock_cg("cgB-1")
    pause 2.0
    narrator "最后的人类也将踏上死亡的宿命，退出循环。"
    phainon "循环？"
    narrator "人类于黑潮中诞生，于黑潮中灭亡。"
    narrator "直至新生神明无法再背负世界的重量，黑潮便会再次浮现，淹没众生，从此往复。"
    phainon "……人类从来不能选择自己的命运吗？"
    narrator "黑潮消解万物，最后连同黑潮本身。"
    show cg B-2 with Fade(1.5, 0.5, 1.5)
    $ unlock_cg("cgB-2")
    pause 2.0
    show black as vignette:
        alpha 0.0
        linear 2.0 alpha 0.5  # 渐暗
        pause 1.0
    narrator "万物始于混沌。"
    narrator "万物溶于黑潮。"
    narrator "万物归于寂静。"
    hide vignette
    show cg black with fade
    stop music fadeout 2.0
    narrator "寂灭前的那一瞬，他却有一瞬无比温柔的触感。"
    pause 2.0
    narrator "仿佛来自谁人的拥抱。"
    show cg white with Dissolve(5.0)
    show text "{color=#000000}Ending B\n生而为人{/color}" at truecenter with dissolve
    pause 2.0
    hide text with dissolve
    jump main_menu_end


label branch_stay:    
    anaxa_no "沉默也是一种选择。"
    phainon "我想和你在一起。"
    phainon "……永远。"
    pause 2.0
    anaxa_no "但你应当清楚，这就是一段虚无之梦。"
    phainon "……"
    anaxa_no "如果这就是你想要的。"    
    hide anaxa
    hide phainon
    show cg D1-2 with fade
    narrator "……哪怕并非真实？"
    $ unlock_cg("cgD1-2")
    pause 2.0
    scene bg white with Dissolve(2.0)
    hide cg
    pause 2.0
    show text "{color=#000000}Ending D\n与你同行的梦{/color}" at truecenter with dissolve
    pause 2.0
    hide text with dissolve
    jump main_menu_end

label main_menu_end:
    show cg black
    menu:
        "主菜单":
            return

label chapter_01:
    scene bg white with fade
    pause 1.5
    narrator "氤氲麦香间，和煦的暖风迎面而来。"
    play music "audio/chapter_01.mp3" fadein 2.0
    $ current_music = "audio/chapter_01.mp3"
    narrator "梦中时常会出现的家乡，在被黑潮吞没以前，是个宁静祥和的村落。"
    narrator "遥远的记忆里，这段无忧无虑的日子如梦般转瞬即逝。"
    pause 1.5
    scene bg almx with Dissolve(3.0)
    father "白厄……白厄！喂，怎么坐在窗边发呆？"
    mother "正是农忙的季节，才更需要充沛的体力啊。"
    phainon "啊……"
    father_name "话是这么说没错……唉，你也别太惯着他。"
    mother_name "休息好了吗，白厄？"
    narrator "倘若不是耳旁熟悉的声音，他几乎以为这只是一场过于美好的梦境。"
    narrator "暖风从窗外带来麦香，映衬在蓝天下的明黄色，和耳旁真切的声音提醒着他——"
    narrator "这并非梦乡，而是故乡。"
    narrator "是原本已覆灭于黑潮中的，他日思夜想的哀丽秘榭。"
    phainon "……"
    narrator "身在熟悉的环境里，儿时的房间还是从前的模样。"
    narrator "要查看桌上的物品吗？"
    jump check_item_in_house

label chapter_01_continue:
    narrator "那么，现在该怎么做？"
    narrator "他回忆起「那刻夏」先前所说的话。"
    show anaxa normal at right with fade
    anaxa_no "请记住，你必须保守秘密，不能告诉任何一人你是时空穿越者，否则一切付出将{color=#FF0000}前功尽弃{/color}。"
    anaxa_no "你要谨慎决策，任何试图改变原本故事走向的行为，都会造成{color=#FF0000}不可逆转{/color}的后果。"
    hide anaxa with fade
    narrator "他决定循着人声，走出房间，向前跑去。"
    narrator "耳旁的风声，氤氲的麦香，邻居的问候，父母的呼唤。"
    narrator "所有的一切就像曾亲历过的一样真实。"
    phainon "哎，父亲母亲！等我一下，马上就过来了！"
    narrator "尽管这条路他很熟悉，但脚下步伐却稍显笨拙。"
    narrator "他低头一看，发现自己的身体变成了小孩子的模样。"
    narrator "就像从前一样，他回到父母身边，帮忙整理农忙时的仓库。"
    narrator "劳作结束后，又和儿时的玩伴们一起，在田野间漫步游玩。"
    narrator "此时的哀丽秘榭，还没有受到黑潮的侵袭。"
    narrator "哪怕这只是一瞬短暂的梦，这幸福也无比真实。"
    narrator "正准备踏上回家的路，有什么吸引了他的目光。"
    narrator "他驻足原地，隔着一小片麦田抬头看过去。"
    narrator "一个熟悉的身影，学者模样。那人比现在的他略高些，弯下腰来正在田间采样。"
    narrator "他隔着一片麦田，远远地看着那个身影。"
    narrator "他绝不会认错，眼前分明是……"
    narrator "少年时的那刻夏。"
    show anaxa scholar normal at right with fade
    narrator "要上前搭话吗？"
    show phainon little normal at left with fade
    menu:
        "上前搭话":
            phainon "你好。"
            anaxa "什么事？"
            phainon "啊……"
            phainon "您是访问学者吗？"
            anaxa "称不上是学术访问，个人兴趣罢了。"
            phainon "有什么需要帮忙的吗？"
            anaxa "暂时没这个需要。"
            anaxa "你呢，刚站在那里半天看什么？很好奇？"
            narrator "原来那刻夏早就察觉到了他的视线。"
            menu:
                "好奇你在做什么":
                    anaxa "做些采集样本的工作。"
                    phainon "样本？"
                    anaxa "研究使用。"
                    phainon "原来如此。"
                    pass
                "因为你长得好看":
                    show anaxa scholar shock at right with dissolve
                    anaxa "哈，小小年纪就这么油嘴滑舌。"
                    phainon "母亲常常教导我，要善于夸赞别人的优点。"
                    anaxa "……"
                    show anaxa scholar normal at right with dissolve
                    pass
        "继续观察":
            narrator "正当他仔细观察时，那刻夏突然回过头来。"
            narrator "他下意识想避开学者的视线，一转身就想藏在树后。"
            narrator "但刚刚回退至少年的青年，还不适应现在的身体，一抬脚，反倒把自己绊了一下。"
            narrator "坠地之前，一双温暖的手接住了他。"
            anaxa "没事吧？"
            phainon "我没……没事。"
            anaxa "怎么了？没迷路吧？"
            menu:
                "我们是不是在哪里见过":
                    show anaxa scholar shock at right with dissolve
                    anaxa "你认错人了吧。"
                    show phainon little sadsmile at left with dissolve
                    pass
                "没有，我就住在旁边":
                    anaxa "位置不错。"
                    pass
    phainon "或许……你需要向导吗？"
    anaxa "这个时间，你没有农活要做吗？"
    phainon "呃，那也不是一天到晚都不休息的。"
    phainon "你来自神悟树庭，对吧？"
    anaxa "猜得不错。"
    phainon "我有个不情之请……"
    anaxa "哦，你想让我教你？"
    phainon "虽然有点冒昧……嗯。"
    anaxa "那恐怕要让你失望了。"
    phainon "哎？"
    anaxa "哼，我的研究，在神悟树庭称得上离经叛道。"
    phainon "我就喜欢这种风格。"
    anaxa "……哈？"
    show anaxa scholar shock at right with dissolve
    phainon "总之有机会的话，希望你能多带我……呃，学习学习。"
    show anaxa scholar normal at right with dissolve
    phainon "作为交换……我可以成为你的向导。"
    phainon "告诉你在哪里收集哀丽秘榭的特产，哪些适合作为炼金材料，怎么样？"
    anaxa "哦，你知道炼金术？"
    phainon "嘿嘿，略懂皮毛。"
    show phainon little sadsmile at left with dissolve
    anaxa "稍微有点意外，这可不是什么大众科目。"
    phainon "在神悟树庭寄来的一本宣传册上看过。"
    phainon "你是这方面的专家吗？"
    anaxa "要论时长，我学习的时间不算久。"
    anaxa "不过……哼，在神悟树庭，确实没有人比我更了解。"
    phainon "你是老师吗？"
    anaxa "我是神悟树庭的学生。"
    phainon "原来如此。你是一个人来的吗？"
    anaxa "嗯。"
    show phainon little normal at left with dissolve
    narrator "事实上，白厄曾学过很久炼金术。虽然……大概不能算成绩拔尖的那一类学生。"
    phainon "我对炼金术很感兴趣，如果需要向导的话，不如让我来。"
    phainon "你也看到了，现在是收获的季节，大人们都忙得很。"
    narrator "为了不打破那道时间规则，白厄对自己从前的经历缄口不言。"
    narrator "尽职尽责扮演着少年向导的身份。"
    jump chapter_01_quiz

label chapter_01_quiz:
    # 重置分数
    $ quiz_score = 0
    anaxa "既然你说对炼金术感兴趣，那先来个简单的测验吧。"
    phainon "……还有这个环节？"
    anaxa "判断一下你现在的知识储备，才好帮助我做决策。"
    anaxa "共4道题目，每题25分，满分100分。"
    pause 1.0
    # 第1题
    anaxa "第一题：炼金术可以做到下列哪些内容？"
    menu:
        "物质转化":
            anaxa "不完整。"
        "元素融合":
            anaxa "不完整。"
        "灵魂解析":
            anaxa "不完整。"
        "以上全部":
            $ quiz_score += 25
            anaxa "正确。"
    
    # 第2题
    anaxa "第二题：炼金术的终极成果是以下哪一项？"
    menu:
        "黄金":
            anaxa "那是外行人的误解。"
        "神性":
            anaxa "不正确。"
        "贤者之石":
            $ quiz_score += 25
            anaxa "不错，答对了。"
    
    # 第3题
    anaxa "第三题：以下哪一项是炼金术的最终阶段？"
    menu:
        "黑化":
            anaxa "回答错误。"
        "红化":
            $ quiz_score += 25
            anaxa "看来你对炼金术有深入研究。"
        "白化":
            anaxa "回答错误。"
        "黄化":
            anaxa "回答错误。"
    
    # 第4题
    anaxa "最后一题：炼金术的四要素是？"
    menu:
        "金木水火":
            anaxa "错。"
        "水气土火":
            $ quiz_score += 25
            anaxa "正确，四元素是炼金术的基础。"
        "木水火土":
            anaxa "再好好想想。"

    # 报分
    anaxa "测试结束。"
    narrator "你的得分是 [quiz_score] 分，满分100分。"
    pause 1.0
    # narrator提问是否再来
    if quiz_score < 60:
        narrator "要再来一次吗？"
        menu:
            "再来一次":
                jump chapter_01_quiz
            "清空答卷，重新蒙一遍":
                if fortune_result == __("凶"):
                    $ quiz_score = renpy.random.choice([0,25,50])
                elif fortune_result == __("大吉"):
                    $ quiz_score = 100
                elif fortune_result == __("中吉"):
                    $ quiz_score = 75
                else:
                    $ quiz_score = renpy.random.choice([0,25,50,75,100])
                narrator "重新蒙了题目，获得了 [quiz_score] 分!"
                pass
            "不用了":
                pass
    jump chapter_01_after
    # 分支判断

label chapter_01_after:
    if quiz_score > 60:
        if quiz_score == 100:
            anaxa "完美的答卷。"
            show anaxa scholar smile at right with dissolve
        else:
            anaxa "不错，及格了。"
        anaxa "既然如此，你想知道什么？"
        phainon "我想了解你最新的研究成果。"
        show anaxa scholar shock at right with dissolve
        anaxa "哈？"
        anaxa "小小年纪，怎么会对我的研究感兴趣？"
        phainon "直觉。"
        anaxa "我在做的研究，经常被称之为渎神。"
        show anaxa scholar normal at right with dissolve
        anaxa "炼金术，万物皆可为原料，我提出过将神熔炼的假说——"
        anaxa "只可惜，没什么人理解我的比喻，反倒是斥责我的论点不敬神明。"
        phainon "不敬神明？"
        anaxa "在黑潮时代，人总会靠着信仰而活。"
        anaxa "但倘若神明如神话里那样存在，却对世界的濒毁视而不见……"
        anaxa "呵，那神明还可以称之为神吗？"
        phainon "我想，或许是力量限制，也或许是……呃……"
        anaxa "也或许是神明尚未诞生。"
        phainon "……"
        anaxa "回到正题，方才只是一种比喻。当原材料的力量来源足够强大时，炼金术理论上无所不能。"
        anaxa "时间、空间，一切有形与无形，都可以视为可转换之物。"
        phainon "时间……"
        phainon "炼金术，能够突破时间的力量吗？"
        anaxa "嗯，理论上如此。"
        anaxa "只是，现实里不具备这种实验条件。"
        narrator "他的确突破了时间的力量，才得以重返哀丽秘榭。要告诉那刻夏吗？"
        menu:
            "其实我来自未来":
                anaxa "嗯？"
                menu:
                    "我认识你，那刻夏":
                        show anaxa scholar shock at right with dissolve
                        pass
                    "我认识你，阿那克萨戈拉斯":
                        show anaxa scholar smile at right with dissolve
                        pass
                anaxa "你知道我的名字？"
                show phainon little sadsmile at left with dissolve
                phainon "我还知道你未来会成为神悟树庭的教授，继续主攻炼金术的研究。"
                show anaxa scholar normal at right with dissolve
                anaxa "看来你知道得不少。"
                phainon "事实上……"
                phainon "我来自未来。"
                anaxa "……有趣。"
                phainon "你不觉得我在说谎？"
                anaxa "呵，对素不相识的人，你有什么说谎的动机？"
                anaxa "难不成，你想逞英雄？"
                phainon "唔，我没有！"
                anaxa "既然你来自未来，那么想必能告诉我，翁法罗斯最终如何了？"
                phainon "……"
                show phainon little normal at left with dissolve
                anaxa "呵，你的脸色很不好看呐。"
                phainon "我们没能阻止黑潮。"
                anaxa "所以，你想穿越时空，拯救翁法罗斯？"
                anaxa "看你的表情，我猜对了？"
                phainon "……你是我可以完全信任的人。"
                anaxa "是吗？未来的我，和你是什么关系？"
                phainon "你是我尊敬的老师，我在你创立的学派里学习过很久。"
                narrator "当然，更多心里话他没说出口。"
                phainon "……你说得对，我也许就是想逞英雄。"
                phainon "命运已经把重来的机会交给了我，我当然要去奋力一搏。"
                anaxa "呵，你想成为英雄？"
                anaxa "无聊至极的答案。"
                phainon "……"
                anaxa "听好了，永远不要寄希望于「重来」。"
                anaxa "「再来一次就好了……」这样的话的确屡见不鲜。"
                anaxa "但真正获得重来的机会时，又有几个人能把握？"
                anaxa "要把希望留给现在，留给你能创造的「变量」。明白了吗？"
                phainon "嗯，我想过这个问题。"
                phainon "于我而言，重来一次，我依旧不知道正确的路。"
                anaxa "这世界的运转总是有一套极其荒谬的规则。"
                anaxa "有时候我们没办法去改变条件，那就去创造新的条件。"
                anaxa "就算无法改变、无法创造，那也不是某一人的责任。"
                anaxa "经历与感受，这些都是无比宝贵的。"
                phainon "嗯，你说得对。"
                phainon "就像现在……我又见了你一面，这就足够了。"
                anaxa "……"
                anaxa "看来你所熟知的那个我，已经行至终点了。"
                phainon "……嗯。"
                phainon "我很想再见你一面，一直都……"
                phainon "抱歉，我说了多余的话。"
                phainon "我知道，你并不是我的那个老师，我现在也不是你的学生。"
                anaxa "若你日后是我的学生，应当知晓我的理论：人的本质是由灵魂决定的。"
                anaxa "那么，哪怕身在不同时间线、甚至不同维度……"
                anaxa "灵魂的本质，万变不离其宗。"
                anaxa "如何，和你所熟知的阿那克萨戈拉斯，理论是否相同？"
                phainon "哈哈，果然是那刻夏老师。"
                phainon "我可以……和你拥抱一下吗？"
                narrator "那刻夏犹豫半晌，向他张开双臂，轻轻搂住了他。"
                narrator "在这样温暖的怀抱里，他想起了那个规则。"
                anaxa_no "请记住，你必须保守秘密，不能告诉任何一人你是时空穿越者，否则一切付出将{color=#FF0000}前功尽弃{/color}。"
                narrator "……没错，他没有遵守好这个规则。"
                stop music fadeout 2.0
                $ current_music = ""
                hide anaxa with Dissolve(2.0)
                narrator "那刻夏的声音远去了。"
                narrator "故乡的清风，氤氲的麦香，也逐渐消失在时间的洪流里。"
                hide phainon with dissolve
                $ current_music = "audio/prologue.mp3"
                play music "audio/prologue.mp3"
                scene bg black with dissolve
                scene bg initial with Dissolve(2.0)
                show phainon sad at left with fade
                narrator "短暂的一次回溯里，他见到了少年时的那刻夏。"
                narrator "关于哀丽秘榭的一切戛然而止。唯有手心里残余的另一人的体温在提醒他，那不是一场梦。"
                narrator "因没能遵守时间穿越的规则，他被打回了最初的起点——即将覆灭的世界。"
                narrator "但体温与心跳，暖风与麦香，都有真切存在过的痕迹。"
                narrator "那刻夏的影子已然不在那里。等待他的，唯有即将被黑潮吞没的世界。"
                narrator "现在的翁法罗斯，已经步入倒计时。"
                phainon "……"
                jump branch_end_god
            "炼金术这么厉害":
                anaxa "炼金术研究物质转换，也就是说，万物皆可熔炼。"
                anaxa "当实验条件达到完美状态，时间也可成为转换的一环。"
                phainon "你是指……时间也可作为实验材料？"
                anaxa "不太准确，时间只是炼金术的表现形式之一，并非真正的物质基础。"
                phainon "那么，怎样才能达到理想状态呢？"
                anaxa "现实条件几乎不可能，现阶段，仅仅存在于理论假说。"
                pass
    else:
        anaxa "没有及格。"
        anaxa "不过没关系，学问本就是循序渐进的过程。"
    anaxa "你叫什么名字？"
    narrator "而这时白厄才想起来，与那刻夏的相遇太过自然，他甚至忘记了自我介绍。"
    phainon "我叫白厄，你呢？"
    anaxa "阿那克萨戈拉斯。"
    phainon "好的，那刻……阿那克萨戈拉斯老师。"
    anaxa "不用叫我老师，我也并非老师。"
    phainon "只是我个人的习惯。"
    phainon "我日后也想去神悟树庭学习，到那时还请……多多指教。"
    anaxa "未来的事交给未来决定，不如做好当下该做的。"
    phainon "……"
    phainon "但我们的未来，又在哪里呢？"
    anaxa "你年纪还小，又何必急于一时。"
    phainon "不……"
    phainon "我没有什么时间了。"
    anaxa "嗯？"
    phainon "那刻夏老师，我……"
    narrator "灵魂仿佛在燃烧。空间和时间在扭曲。"
    narrator "他预感到身处哀丽秘榭的时间不多了。"
    show cg white as flash at power_die_out with None
    narrator "一次时间跳跃，似乎维持不了太久。"
    narrator "哀丽秘榭固然令人怀念，但他所奢求的那个转机并不在这里。"
    narrator "然而他的终点，又在何方？"
    narrator "与那刻夏更早的邂逅，能够为日后的新结局埋下种子吗？"    
    phainon "头……好痛。"
    anaxa "怎么了？"
    phainon "那刻夏！"
    hide cg
    show cg young with Fade(1.5, 0.5, 1.5)
    pause 4.0
    $ unlock_cg("cg_young")
    phainon "我们未来一定会再次相遇。"
    show cg black with Dissolve(5.0)
    stop music fadeout 2.0
    $ current_music = ""
    phainon "我……一定会成为让你骄傲的学生！"
    phainon "……再见。"
    hide phainon
    hide anaxa
    jump chapter_02

    # hide anaxa scholar with dissolve
    # $ reading_letter = True
    # while reading_letter:
    #     menu:
    #         "打开信件":
    #             call screen simple_letter(
    #                 letter_text="哀丽秘榭的白厄：\n\n当你打开这封信时，我已经启程前往神悟树庭。\n随信附上神悟树庭入学指南。\n\n阿那克萨戈拉斯",
    #                 title=""
    #             )
    #         "不打开":
    #             $ reading_letter = False
    # show phainon little normal at left with dissolve
    # return
    # jump chapter_02

label check_item_in_house:
    while True:
        menu:
            "查看书桌上的纸张":
                narrator "几张字条，应当来自于哀丽秘榭的玩伴。"
                narrator "一张是不太规整的棋盘格，其上有几枚黑白相间的手绘棋子。从棋子来看白方得胜。"
                narrator "一张是演算用的草稿纸，写着几行简单的数学公式。"
                narrator "这个时候的他尚未接触过炼金术，还不知道日后有更高深复杂的公式等着他。"
            "查看书桌的储物格":
                narrator "几个木头小人，模样不算很规整，看得出来雕刻者手艺还不够精湛。"
                narrator "一把稍有磨损的小刀放在旁边，似乎有阵子没在使用。"
                narrator "还有一个运势抽签桶，要抽取一张签条试试吗？"
                menu:
                    "抽签":
                        $ fortune_result = renpy.random.choice([__("大吉"), __("中吉"), __("凶")])
                        narrator "你抽到了..."
                        narrator "[fortune_result]！"
                        pass
                    "不抽签":
                        pass
            "查看书架上的相册":
                narrator "几张照片。记录了白发少年长大的过程。"
                narrator "相册最末尾是一张三人合影的全家福，一小丛风干后的麦穗从页间掉了出来。"
            "直接出发":
                jump chapter_01_continue

label chapter_03:
    scene bg black with fade
    hide cg
    stop music fadeout 2.0
    $ current_music = ""
    pause 2.0
    show screen big_text("#3 终点") with Dissolve(2.0)
    pause 2.0
    hide screen big_text with dissolve
    scene bg office as darkened:
        matrixcolor BrightnessMatrix(-0.3)
    with dissolve
    play music "audio/chapter_03.mp3" fadein 2.0
    $ current_music = "audio/chapter_03.mp3"
    narrator "碎裂的器材掉落在地面，灰尘和木屑迎面扑来。眼前破败不堪的景象，却来自他曾经熟悉的地方。"
    narrator "地上绘制着炼金术的阵法，图案颇为复杂高深，从未在课本上出现过，学生们并不会知晓其中的含义。"
    phainon "……"
    show phainon sad at left with dissolve
    narrator "这是智种学派贤人的实验室，它的主人刚才在他眼前停止了呼吸。"
    narrator "就在这张倒下的桌子旁，他与他的老师曾一起讨论学术问题，也曾在窗边谈论人生理想。"
    phainon "那刻夏老师……"
    anaxa_no "白厄，你怎么来了？"
    show anaxa shock at right with fade
    phainon "咦，那刻夏……老师？"
    show phainon normal at left with dissolve
    phainon "不对，你是……"
    narrator "来人略显机械性的动作让他很快反应过来，这不是那刻夏，而是他的机巧造物。"
    phainon "……"
    phainon "……我好想见你，那刻夏老师。"
    show anaxa normal at right with dissolve
    anaxa_machine "阿那克萨戈拉斯教授不在这里。"
    phainon "我知道。"
    anaxa_machine "但若你有什么烦恼，也可以向我诉说。"
    phainon "……"
    show phainon sad at left with dissolve
    narrator "地面上散落着一些文件和信件。白厄弯腰捡起，试图把它们整理好。"
    anaxa_machine "不仔细看看么？你似乎很好奇。"
    phainon "……这是那刻夏老师的私人物品，我不能擅自翻阅。"
    anaxa_machine "他既然放在这里，想必没打算遮掩。更何况，这里面有本应寄给你的信件。"
    phainon "我的……？"
    anaxa_machine "嗯，你的。打开看看吧？"
    narrator "他把那些纸张整理好，是几封信和一份实验日志。"
    phainon "你……你不要这样盯着我，这样很不自在。"
    anaxa_machine "不用在意我，我只是个机械装置。"
    hide anaxa with Dissolve(3.0)
    while True:
        menu:
            "一张未送出的留言条":
                anaxa_letter "致白厄："
                anaxa_letter "也正如炼金术所揭示的那样，空白意味着无限可塑性。"
                anaxa_letter "——阿那克萨戈拉斯"
            "拆封过的信件":
                phainon_letter "那刻夏老师，好久不见。"
                phainon_letter "虽然一提笔就有很多想说的事，不过信件篇幅有限，还是长话短说。"
                phainon_letter "我看到了您先前刊登在报的发言。"
                phainon_letter "「如果神明存在，则神性在于神的灵魂，而与神的形态无关，正如人性也由人的灵魂决定。」"
                phainon_letter "「——由此可得，神性与人性无异，继续推论则为：人神本无异。」"
                phainon_letter "有趣的论点，但不得不说，根据我近期的观察，似乎在翁法罗斯掀起了不小的风浪。"
                phainon_letter "我试图向旁人解释您的观点，但似乎用处不大……抱歉。"
                phainon_letter "不知您近来可好？如果需要避难，欢迎来我的住处。"
                phainon_letter "虽然……房间不大。期待您的回信。"
                phainon_letter "——你的学生，白厄。"
            "未寄出的回信":
                anaxa_letter_notsent "致白厄："
                anaxa_letter_notsent "不足挂齿的流言。不必在意，一切照旧。"
                anaxa_letter_notsent "也不必抱有歉意，智种学派的大门永远向它的学子敞开。"
                anaxa_letter_notsent "——阿那克萨戈拉斯"
            "一份共创实验日志":
                narrator "记录人：阿那克萨戈拉斯，恩贝多克利斯。"
                narrator "日志记录了来自两人的报告及研究内容。"
                narrator "（前面的内容已被人为抹去，只余模糊不清的字迹。可读内容从12月20日开始。）"
                narrator "日期：12月20日"
                anaxa_fullname "……综上，若想达到贤者之石的完美状态，需要以能够超越时间的力量为源。"
                anaxa_fullname "用更通俗的话来讲，应该称之为「神性」。若能熔炼神的灵魂，则黑潮并非无解。"
                anaxa_fullname "我从不寄希望于重来。失败的实验，重来千万次也没有用。而变量、催化剂，这才是改变结果的关键。"
                narrator "日期：1月2日"
                anaxa_teacher "……熔炼神的灵魂？"
                anaxa_teacher "但是，按照你的理论，若神从不存在，又何来神的灵魂？"
                narrator "日期：1月15日"
                anaxa_fullname "目前主流观点认为，神在创世后逐渐消陨，直至火种集齐方可再造神明。"
                anaxa_fullname "既然神从来无法被召唤，我认为核心在于——「转换」。"
                anaxa_fullname "那么，神的灵魂从何而来？只要能够突破时间的桎梏，想必答案近在咫尺。"
                anaxa_fullname "但，我不相信神明凭空出现，就像炼金术一样，无中生有只是表象，等价交换才是真相。"
                anaxa_fullname "综上所述，我的实验计划如下："
                anaxa_fullname "实验步骤：一阶段，贤者之石的炼成；二阶段，灵魂与黑潮的融合。"
                anaxa_fullname "三阶段，以灵魂态启动炼金术，借由十二火种与贤者之石的力量分解黑潮，逆转因果。"
                anaxa_fullname "实验体：本人。"
                narrator "日期：2月1日"
                anaxa_teacher "你打算用自己做实验，你疯了吗！"
                narrator "日期：2月3日"
                anaxa_fullname "不，恰恰相反，我现在无比清醒。这只是追求真理的必经之路。"
                anaxa_fullname "等到我死去时，借由炼金术，我的灵魂将与黑潮完整融合。"
                anaxa_fullname "能否改变翁法罗斯的命运，就让我们拭目以待吧。"
                narrator "日期：2月5日"
                anaxa_teacher "唉，我知道你心意已决，不可能被任何人撼动。"
                anaxa_teacher "三思而行，做好万全的准备，这是我唯一的忠告了。"
                anaxa_teacher "其他若有什么需要帮忙的，记得随时开口。"
                narrator "日期：4月30日"
                anaxa_fullname "……现在启动仪式，完成贤者之石的炼成，仍然无法达到它的理想状态。"
                anaxa_fullname "但黑潮的增长速度正在加快，我所剩的时间不多了。"
                anaxa_fullname "无论是否达到理想状态，届时，我都将启动仪式。"
            "翻阅完毕":
                jump chapter_03_after

label chapter_03_after:
    phainon "……"
    phainon "那刻夏老师……原来一直在进行这么危险的实验。"
    phainon "通过炼金术打造完美的贤者之石，关键在于……神的灵魂？"
    phainon "神……的灵魂。"
    phainon "神。"
    show phainon firm at left with dissolve
    phainon "并非召唤，而是转换。"
    phainon "难道是……"
    phainon "……我？"
    show anaxa normal at right with dissolve
    anaxa_machine "你有什么眉目？"
    phainon "！"
    phainon "吓我一跳。"
    anaxa_machine "？"
    phainon "我有些眉目了，但我还不能说。"
    anaxa_machine "很多学生在解不出问题时都会这么回答。"
    phainon "……"
    phainon "哎，你果然不是那刻夏老师。"
    anaxa_machine "我刚才就是这么说的。那我再自我介绍一下，我是阿那克萨戈拉斯教授的机巧造物。"
    phainon "你知道贤者之石的炼成方法吗？"
    anaxa_machine "很遗憾，我没有这样的功能。"
    phainon "好吧……"
    anaxa_machine "看来我无法解答你的疑问。"
    anaxa_machine "再见。"
    phainon "等等……"
    hide anaxa with fade
    narrator "机巧那刻夏离开了实验室。"
    narrator "白厄又仔细翻阅了资料。那刻夏的研究手记里，并未记载如何炼成贤者之石。"
    narrator "凭借智种学派学生的知识，暂时还无法完成这般复杂的炼金术。"
    phainon "……那刻夏老师。"
    phainon "好想……再见你一面。"
    pause 2.5
    anaxa "打起精神，这可不像你。"
    phainon "那刻夏老师？！"
    show anaxa normal at right with fade
    phainon "我以为你已经……"
    show phainon sad at left with dissolve
    anaxa "……怎么了？"
    show cg D1-1 with fade
    $ unlock_cg("cgD1-1")
    anaxa "白厄？"
    narrator "温暖的身躯，温热的呼吸。"
    narrator "这是还存在于人世的那刻夏。这一次的时间并未继续线性向前，而是回到了更早的神悟树庭。"
    phainon "看到实验室这副模样，我差点还以为你已经……你没事真是太好了。"
    anaxa "呵，实验事故在所难免，只是清理起来稍有些费力。"
    anaxa "你呢？突然跑来神悟树庭，是有什么问题要请教？"
    phainon "我的确有一事相求！"
    phainon "我的时间有限，来不及解释原因，但我必须放手一搏。"
    phainon "那刻夏老师，请熔炼我的灵魂！"
    anaxa "……你？"
    phainon "我看过了你的研究笔记，我认为想要炼成完美的贤者之石，这是最理想的解法。"
    anaxa "白厄，你的意思是……"
    anaxa "……哼，我知道了。"
    anaxa "刚好，贤者之石的阵法就在这里。站在这里别动，我会启动它。"
    phainon "明白。"
    anaxa "你不害怕吗？"
    phainon "有你在我身边，我很安心。"
    phainon "……比以往任何时候都要安心。"
    anaxa "从未做过的实验，我无法保证结果。"
    anaxa "等价交换为前提，实验只能保证你继续存在。但至于以何种方式存在……"
    phainon "我相信你，请开始吧。"
    anaxa "……呵，那就开始了。"
    show phainon firm
    hide cg with Fade(1.5, 0.5, 1.5)
    menu:
        "完成炼金仪式":
            pass
    anaxa "那么，先说明注意事项。"
    anaxa "第一，保持安静，一旦炼金仪式开始，任何非常规现象，都属于炼金仪式的一环。"
    anaxa "第二，保持专注，不可分心，不要提问。这句话既适用于你，也适用于我。"
    anaxa "第三，无论发生什么事情，都万万不能离开阵法，这是确保安全的前提条件。"
    anaxa "那么，白厄——"
    anaxa "接下来，你将成为炼金术的一环，你愿意把灵魂乃至生命交予我，完成这场炼金仪式吗？"
    phainon "我愿意。"
    anaxa "好。那么闭上你的眼睛。"
    anaxa "记住我刚才说的话。"
    show cg black with Fade(1.5, 0.5, 1.5)
    hide darkened
    stop music fadeout 2.0
    $ current_music = ""
    anaxa "深呼吸。"
    anaxa "保持安静，专注于自我灵魂的感知。"
    anaxa "就像我从前教你的那样。"
    pause 2.0
    narrator "当有形与无形不再拥有边界，前所未有的力量充斥于体内。"
    narrator "他感应到术式的启动，全身心集中于自我的感知。"
    narrator "他——即是跨越时间而来的「神性」，是炼金术的最后一环。"
    narrator "现在，他站在炼金术的阵法里，将此身托付于他的老师。"
    pause 2.0
    narrator "很快，他感应到炼金术的触媒，「等价交换」法则的一部分。"
    narrator "等到他反应过来那是什么时，几乎屏住了呼吸。"
    narrator "这炼金术的触媒是——"
    narrator "一颗蓬勃跳动的心脏。"
    phainon "……！"
    play sound "audio/heartbeat.ogg" loop volume 3.0 fadein 2.0
    narrator "他不知道那刻夏是什么时候将心脏分离出来的。"
    narrator "那刻夏也从未向他提及过，毕竟，告知学生真相只会让对方犹疑。"
    narrator "甚至就连刚才的实验日志，也有意抹去了这一部分。"
    narrator "白厄有很多问题想问，但谨记着要保持安静、专注。"
    narrator "那刻夏将身心交付与他，他自然要给予相同的回应。"
    pause 2.0
    anaxa "——至是，工程已毕，言尽于此。"
    phainon "……成功了吗？"
    narrator "——术法完全结束时，那炼金术的造物，便成为了他的一部分。"
    narrator "或者说，他成为了它的一部分。"
    show stone:
        xalign 0.5
        yalign 0.5
        zoom 1.0
    with Dissolve(5.0)
    narrator "——贤者之石。"
    narrator "炼金术真正的终极成果，至高至纯的贤人造物，已然近在眼前。"
    narrator "他与那刻夏的心脏合二为一。"
    anaxa "保管好贤者之石，你的灵魂现在已经与它紧密相连。"
    phainon "嗯，我能感受到，它已成为我生命的一部分。"
    phainon "……我的灵魂与你的心脏，如此紧密相连着。"
    phainon "我会守护它，直到我的生命尽头。"
    anaxa "很好，那么……"
    anaxa "——我会在终点等你。"
    hide stone with fade
    stop sound fadeout 2.0
    narrator "借由那刻夏的方法，他再次突破了时间与空间。"
    narrator "与前两次不同的是，他的灵魂不再被生硬地撕扯。"
    narrator "被埋葬的无数记忆从他眼前掠过，他就像一段段电影的观众，以灵魂的姿态感受一切。"
    show expression glow("phainon2 smile", 0.9) as phainon_glow with Dissolve(5.0)
    narrator "他看到无数灵魂被束缚于黑潮中。"
    narrator "人类构筑了这个世界。"
    narrator "人类想守护这个世界。"
    narrator "人类不愿就此放弃自己的家园。"
    narrator "最后，在通往那时间尽头的路上，他依稀看到了温暖光明的幻象。"
    show expression glow("phainon2 normal", 0.9) as phainon_glow with dissolve
    narrator "他向前方的人影伸出手，却触碰不到任何事物。"
    narrator "他已达到了灵魂至纯的状态，就像未来的那刻夏对自己所做的一样。"
    phainon "……那刻夏老师？"
    hide phainon_glow with Dissolve(3.0)
    $ current_music = "audio/chapter_02.mp3"
    play music "audio/chapter_02.mp3" fadein 2.0
    show cg dream at blur_to_clear(5.0) with Dissolve(2.5)
    $ unlock_cg("dream")
    hide phainon
    hide anaxa
    anaxa "做得不错，白厄。"
    anaxa "希望的种子已经播下。循着时间的河流，我们终会找到属于彼此的答案。"
    phainon "我还能再见到你吗？"
    phainon "我还能……再拥抱你吗？"
    anaxa "从未做过的实验，我无法保证结果。"
    anaxa "唯有一事我可以确定，现在的贤者之石，是炼金术所能抵达的终极成果。"
    anaxa "是只在理想状况下才能达成的完美状态。"
    anaxa "我相信，我的计算确凿无疑。"
    phainon "我也相信。"
    phainon "但用心脏作为触媒……"
    phainon "你的肉身还能支撑多久呢？"
    anaxa "呵，白厄。所有一切都在我的计算内。"
    anaxa "只有抛却物理的存在，才能抵达至纯的终极。"
    anaxa "无论运用何种计算方法，想要突破黑潮的桎梏，都需要所谓神性作为炼金术的一环。"
    phainon "所以，我出现在了这里，成为未来与过去相接的最后拼图。"
    phainon "你的推论还是那么完美无缺。"
    phainon "……那刻夏老师，能成为你的学生真是太好了。"
    anaxa "变量，需要由人去创造。坐以待毙从来不是我的风格。"
    phainon "我还有一事想请教。"
    anaxa "尽情提问吧。"
    phainon "那么，现在的我们究竟是为何物？"
    anaxa "我一向很少这么回答。但白厄，我也无法给出准确的答案。"
    anaxa "这是从未被论证过的存在形式，我们将回归灵魂最纯净的姿态，拥有超越时间与空间的力量。"
    anaxa "如此一来，便能将不可能化为可能。"
    anaxa "——分解吞没世界的黑潮，解放被黑潮束缚的灵魂。"
    anaxa "你准备好了吗？"
    phainon "当然。"
    phainon "吾师，谢谢你给我指引了这条道路。"
    phainon "我向你发誓：我会引领所有人在新世界重逢。"
    anaxa "很好，不愧是我的门生。"
    anaxa "——愿理性予以你启蒙。"
    anaxa "再会。"
    menu:
        "继续向前":
            pass
    stop music fadeout 2.0
    $ current_music = ""
    scene bg initial with Fade(1.5, 0.5, 1.5)
    hide cg
    narrator "他以全然不同的存在方式，再次回到起点。"
    narrator "完整的十二火种缀于天幕，静静等待着他的归来。"
    narrator "超脱于时间与空间，不再以物理方式存在，他依然听得到这道声音——"

    play music "audio/chapter_03.mp3" fadein 2.0
    $ current_music = "audio/chapter_03.mp3"
    narrator "原初的生命，在黑潮中死去。新生的灵魂，于黑潮中孕育。\n唯有纯粹的灵魂，能够跨越死亡的距离。"
    narrator "成为神明，抛弃曾经的名字，抛弃凡俗的肉身，才能被镌刻为真正的永恒。"
    show expression glow("phainon2 normal", 0.9) as phainon_glow with Fade(1.5, 0.5, 1.5)

    #show phainon2 cool at left with Fade(1.5, 0.5, 1.5)
    narrator "成为神明"
    phainon "……我拒绝。"
    narrator "成为神明"
    phainon "我拒绝。"
    narrator "成为神明。"
    menu:
        "我拒绝":
            pass
    anaxa "谁在替他做决定？"
    show expression glow("anaxa2 normal", 1.4) as anaxa_glow with Fade(1.5, 0.5, 1.5)

    # show anaxa2 normal at right with Fade(1.5, 0.5, 1.5)
    anaxa "抛却陈旧伪神的概念，由我来重新定义何为神明。"
    anaxa "白厄——现在，我们以相同的方式存在着，便能互相感知。"
    phainon "那刻夏老师！"
    anaxa "如此一来，我的实验计划只余最后阶段。"
    anaxa "以十二火种与完整的贤者之石为基底，我将熔炼黑潮，解放被束缚的灵魂。"
    show expression glow("phainon2 smile", 0.9) as phainon_glow with Fade(1.5, 0.5, 1.5)
    phainon "请开始吧。"
    show cg white with fade
    hide phainon_glow
    hide anaxa_glow
    show stone:
        xalign 0.5
        yalign 0.5
        zoom 0.8
    with Fade(1.5, 0.5, 1.5)
    menu:
        "完成最后的炼金仪式":
            pass
    anaxa "世界诞生之初为一团混沌。灵魂的种子栖息其中，逐渐生根发芽。"
    anaxa "黑潮不过为笼罩世界的表象，现在，由我们来引领世界走向真实。"
    scene bg black with dissolve
    hide stone with dissolve
    hide cg
    show expression glow("anaxa2 normal", 1.4) as anaxa_glow with fade
    anaxa "生息破土，世界塑造——"
    hide anaxa_glow with Dissolve(3.0)
    
    show expression glow("phainon2 normal", 0.9) as phainon_glow with dissolve
    phainon "黎明创世，地辟天开！"
    hide phainon_glow with Dissolve(3.0)
    show expression glow("anaxa2 normal full", 1.2) as anaxa_glow with fade
    anaxa "我，阿那克萨戈拉斯在此断言——"
    anaxa "唯我们自己，才是此世的神明！"
    hide anaxa_glow with Dissolve(3.0)
    jump true_end

label chapter_02:
    scene bg black with fade
    stop music fadeout 2.0
    $ current_music = ""
    pause 2.0
    show screen big_text("#2 重回树庭") with Dissolve(2.0)
    pause 2.0
    hide screen big_text with dissolve
    scene bg red with fade
    phainon "呃……"
    narrator "灵魂与身体一起在燃烧，他被时间的裂隙不断撕扯。"
    narrator "违逆时间带来的灼烧感，令他的意识几近崩溃。"
    $ current_music = "audio/main_menu.mp3"
    play music "audio/main_menu.mp3" fadein 2.0
    show expression Text("{alpha=0.7}我{/alpha}", size=45, color="#fff", font="fonts/SourceHanSerifSC-Bold.otf") as text_end at nightmare_twist:
        xalign 0.5
        yalign 0.5
    with fade
    show phainon little normal at mosaic_blur_at(z=1.4,alpha_val=0.3) with dissolve
    pause 2.0
    show phainon normal at mosaic_blur_at(z=1.4,alpha_val=0.3) with dissolve
    pause 2.0
    hide text_end
    hide phainon with dissolve
    show anaxa scholar normal at mosaic_blur_at(z=1.4,alpha_val=0.3) with dissolve
    pause 2.0
    show anaxa normal at mosaic_blur_at(z=1.4,alpha_val=0.3) with dissolve
    show expression Text("{alpha=0.7}我们{/alpha}", size=45, color="#fff", font="fonts/SourceHanSerifSC-Bold.otf") as text_end at nightmare_twist:
        xalign 0.5
        yalign 0.5
    with fade
    pause 2.0
    hide text_end
    hide anaxa with fade
    scene bg black with fade
    memory_text "{alpha=0.7}PE{w=0.5}OPLE{w=0.5}? {color=#FF0000}GOD{w=0.5}{/color}? NULL{w=0.5}?{/alpha} "
    # 快速闪回
    show black as vignette:
        alpha 0.0
        linear 1.0 alpha 0.8  # 渐暗
        pause 1.0
        linear 0.5 alpha 0.6  # 稍微恢复
        pause 0.5
        linear 1.0 alpha 0.9  # 再次变暗
        pause 1.0
        linear 0.5 alpha 0.5
    pause 2.0
    show bg almx at breathe_blur with fade
    # show anaxa scholar smile at mosaic_blur_at(z=1.4,alpha_val=0.3) with fade
    # $ loop_text(["{alpha=0.7}你知道我并非真实的存在。{/alpha}","{alpha=0.7}如果你认为那并非正确，就去纠正它。{/alpha}","{alpha=0.7}我是神悟树庭的学生。{/alpha}","{alpha=0.7}你叫白厄，对吧？{/alpha}","{alpha=0.7}我已经死去了，白厄。{/alpha}"],5,0.1)
    # hide anaxa with fade
    # scene bg black
    pause 2.0
    show bg initial at breathe_blur with fade
    pause 5.0
    phainon "头……好痛。"
    narrator "成为神明。"
    narrator "成为神明。"
    narrator "成为神明。"
    phainon "不……对……"
    narrator "时间在扭曲。空间在扭曲。"
    narrator "它们被压缩折叠，以几近令人窒息的方式。"
    narrator "模糊不清的记忆从眼前闪过。"
    hide flash
    stop music fadeout 2.0
    narrator "直到他终于看见，令人怀念的地方。"
    scene bg black with dissolve
    $ current_music = ""
    scene bg top with Dissolve(5.0)
    play music "audio/chapter_02.mp3" fadein 2.0
    $ current_music = "audio/chapter_02.mp3" 
    # 第一段记忆
    hide vignette
    scene bg top at default with Dissolve(5.0)
    show anaxa normal at right with Fade(1.5, 0.5, 1.5)
    show screen memory_overlay 
    with dissolve
    anaxa_in_memory "白厄？"
    anaxa_in_memory "哼，欢迎来到神悟树庭的入学仪式。"
    anaxa_in_memory "就像我们先前约定的那样——恭喜你，现在正式成为我的学生了。"
    show anaxa smile at right with dissolve
    show phainon normal at left with fade
    phainon_in_memory "好久不见，那刻夏老师。"
    anaxa_in_memory "是阿那克萨戈拉斯。"
    anaxa_in_memory "如果想找我请教问题，记得称呼这个名字。"
    phainon_in_memory "明白。"
    hide cg
    show cg black with fade
    # 第二段记忆
    scene bg black with dissolve
    scene bg window with Dissolve(4.0)
    hide cg black
    hide phainon
    hide anaxa
    #show anaxa normal at right with fade
    show anaxa normal at right with Fade(1.5, 0.5, 1.5)
    anaxa_in_memory "翻开这本书第七百二十页——"
    show phainon normal at left with dissolve
    phainon_in_memory "这上面的图片是……从前的星空？"
    anaxa_in_memory "曾经，神悟树庭的窗外还看得到星空。"
    anaxa_in_memory "那时，从这里所看到的星星，都是它们若干年前的影像。"
    anaxa_in_memory "反之也同样，现在的翁法罗斯，如果正在被数万光年以外的星球观测——"
    anaxa_in_memory "他们所看到的，是尚在新生的星球。"
    phainon_in_memory "而事实上……我们的家园却在濒毁的边缘。"
    show phainon sad at left with dissolve
    phainon_in_memory "书上也说，神悟树庭能看到星空已经是很多年前的事了。您曾经看到过这样的星空吗？"
    anaxa_in_memory "我来到这里后，神悟树庭的永夜天幕里早已空无一物。"
    anaxa_in_memory "自从黑潮接连笼罩翁法罗斯，遥远的星空便不再显现，混沌的天幕取而代之。"
    phainon_in_memory "果然是只存在于书中的景象吗……"
    anaxa_in_memory "倘若终有一日，黑潮吞没我们的土地，这颗星球便也消弭于偌大的宇宙中。"
    anaxa_in_memory "但在数万光年以外，却还有人能看到翁法罗斯曾经存在过的痕迹。"
    anaxa_in_memory "我们存在过的历史，将在那遥远的星空被观测与证明。"
    phainon_in_memory "等到我们集齐十二枚火种，就能驱散混沌，再次见到真实的星空。"
    show phainon firm at left with dissolve
    phainon_in_memory "到那时，透过这扇窗，我们一定可以看到真实星空的景色。"
    anaxa_in_memory "白厄，我从不相信火种能够引领我们走向新世界。"
    anaxa_in_memory "你若是如此坚信，等到需要理性火种的那一天，就将它拿去吧。"
    anaxa_in_memory "它就在启蒙王座的顶端。倘若黑潮降临，那里能够庇佑它暂时免于侵蚀。"
    phainon_in_memory "……那刻夏老师，你连这种准备都做好了吗？"
    anaxa_in_memory "为不确定性尽早做打算，本就是我的风格。"
    show cg black with Fade(1.5, 0.5, 1.5)
    hide phainon
    hide anaxa
    # 第三段记忆
    hide cg with fade
    show phainon normal at left with dissolve
    phainon_in_memory "那刻夏老师，我来了。"
    show anaxa normal at right with dissolve
    anaxa_in_memory "这么早就来了？我们约定的时间是半小时后。"
    phainon_in_memory "哈哈，闲着也是闲着，只是想着万一有什么需要我帮忙的……"
    anaxa_in_memory "不要勉强自己一直保持笑容。"
    phainon_in_memory "……"
    anaxa_in_memory "我听说了哀丽秘榭之前发生的事情。"
    anaxa_in_memory "……节哀。"
    phainon_in_memory "我……没事，那刻夏老师。能来这里和您说说话就够了。"
    show phainon sad at left with dissolve
    anaxa_in_memory "适当的倾诉是有必要的。"
    phainon_in_memory "……谢谢您。"
    anaxa_in_memory "在我很小的时候，家人就被黑潮夺去性命，只有我活了下来。"
    anaxa_in_memory "「如果那一天活下来的是他们就好了。」会有这样的想法也不奇怪。"
    phainon_in_memory "原来老师也和我一样，我还是第一次听你讲过去的事。"
    anaxa_in_memory "生者总要背负着死者的愿望前进。"
    anaxa_in_memory "我也曾经试图寻找过令黑潮中的死者复生的方法。"
    anaxa_in_memory "只是，炼金术虽能进行物质转换，却缺少强大的催化剂。"
    anaxa_in_memory "无论进行多么缜密的运算，也无法够到那道界限。"
    phainon_in_memory "……希望我们都不要再经历那样的离别。"
    anaxa_in_memory "我比你年长，如你所见，身体也不怎么样。我不擅长武力，如果黑潮来临……"
    phainon_in_memory "不要再说了，那刻夏老师。"
    anaxa_in_memory "离别是我们一生中必须面对的课题，更何况身在这个年代。"
    phainon_in_memory "我不想再和你分开。"
    anaxa_in_memory "总有一天，离别会如期而至，或早或晚。"
    show cg black with Fade(1.5, 0.5, 1.5)
    hide phainon
    hide anaxa

    # 第四段记忆
    scene bg black with dissolve
    scene bg top with Dissolve(4.0)
    hide cg
    show anaxa smile at right with dissolve
    anaxa_in_memory "那么，恭喜毕业，白厄。"
    show phainon normal at left with dissolve
    phainon_in_memory "仅此而已吗，那刻夏老师？"
    phainon_in_memory "一般来说，老师对学生，总有些毕业寄语吧。"
    anaxa_in_memory "哼，那么，你有什么愿望？"
    show anaxa normal at right with dissolve
    phainon_in_memory "现在，我还想去寻求黑潮的解法。"
    phainon_in_memory "我也想去拯救那些被黑潮所困的人们，至少不要让家乡的悲剧重演。"
    show phainon firm at left with dissolve
    anaxa_in_memory "看来你还是想成为英雄。"
    phainon_in_memory "是啊，英雄。"
    phainon_in_memory "「无聊至极的答案」——对吗？"
    anaxa_in_memory "空白意味着无限可能，而英雄也是其中的一种。"
    anaxa_in_memory "坚持你的理想，如果时至今日它仍是你的理想。"
    phainon_in_memory "假设我们抗击黑潮成功，那刻夏老师，你最想做的事情是什么？"
    anaxa_in_memory "研究宇宙中的奥秘，拓展知识的边界。某种程度上来说，和现在的重心倒也无异。"
    anaxa_in_memory "你呢？"
    phainon_in_memory "我？如果做得到的话，我想成为领航员，在星海里遨游，到那时——"
    show phainon normal at left with dissolve
    phainon_in_memory "就可以对外如此介绍：我啊，是那刻夏老师的学生。"
    anaxa_in_memory "哼，还是这么油嘴滑舌。"
    phainon_in_memory "这是真情流露。"
    show cg black with Dissolve(4.0)
    phainon_in_memory "我相信，有朝一日，我们一定可以看到真实的星空。"
    hide screen memory_overlay
    hide phainon
    hide anaxa
    # back
    narrator "记忆逐渐褪色。"
    narrator "一枚火种照耀在漫漫长路的终点。"
    narrator "理性的象征，智慧的顶点，真正的启蒙王座近在咫尺。"
    show cerces:
        xalign 0.5
        yalign 0.5
        zoom 0.5
    with Dissolve(5.0)
    show cerces:
        xalign 0.5
        yalign 0.5
    with Dissolve(3.0)
    anaxa "白……厄？"
    hide cerces with dissolve
    hide cg with Fade(1.5, 0.5, 1.5)
    show anaxa hurt at right with Dissolve(3.0)
    phainon "那刻夏老师！"
    show phainon firm at left with dissolve
    anaxa "你怎么现在……会在这里？"
    anaxa "这里很危险。"
    phainon "别动，你流了好多血。"
    anaxa "……"
    anaxa "呵，这副模样见你，还真狼狈。"
    phainon "我马上带你离开！"
    anaxa "别做多余的事，尽快撤离才是正解。"
    phainon "不行，我不能……"
    anaxa "冷静点，白厄。你我都知道这种程度已经无力回天。"
    anaxa "别忘了，生者总要背负着死者的愿望前进。"
    phainon "我怎么可以在这里就放弃……"
    anaxa "生命尚在，就有希望。不要放弃它。"
    phainon "……"
    anaxa "古老的神话里，潘多拉的魔盒打开后，灾厄接连降世，人类濒临毁灭。"
    anaxa "到了最后，盒子里唯一留下的是希望。"
    phainon "希望，唯一的希望吗……"
    anaxa "希望，意味着不确定的期待。"
    anaxa "我并不认同火种能够改变人类的命运。更不指望它改写历史，亦或是创造未来。"
    anaxa "但，不否认它会成为某种催化剂。催生出来的成果，才是我们所要寻求的转机。"
    anaxa "不要放弃希望，直至最后一刻。"
    phainon "……我如果再早点来就好了。"
    phainon "我不想……经历这种离别。"
    show phainon sad at left with dissolve
    anaxa "呵，这世上没有那么多如果。"
    phainon "我知道，但是……"
    anaxa "不要过多留恋没能达成的事。"
    phainon "别说了，我来想办法给你止血。"
    anaxa "别白费力气了，白厄。我撑不了多久。"
    phainon "我……还想未来有一天，能回到神悟树庭，像从前一样坐在教室窗边。"
    phainon "我还希望，有朝一日能和你一起观测星空。"
    phainon "我想救你，我想救所有人。我们的命运不该被终止于此，不该被就此遗忘。"
    anaxa "遗忘？"
    anaxa "浩瀚银河间，总有人会知晓你我的存在。"
    anaxa "我们……咳……"
    show anaxa eyeclose at right with fade
    phainon "……好多血。"
    phainon "老师，你现在的身体不适合讲太多话。"
    anaxa "呵，再不讲就没机会了，我这副身体撑不了多久。"
    anaxa "你也别在这里逗留太久，树庭还没脱离危险。"
    show anaxa hurt at right with dissolve
    phainon "的确，生者总要背负死者的愿望活下去。"
    phainon "但那刻夏老师……"
    phainon "你的愿望是什么？"
    anaxa "学者终其一生的理想，大多是解明真理。我也不例外。"
    anaxa "只是课题设置过于宏大，以至于将死之际也未能解明。"
    anaxa "若有更多时间进行充足的论证，想必也就不留遗憾了。"
    phainon "……为什么我们的命运里，总有这么多遗憾。"
    menu:
        "其实我来自未来":
            phainon "其实我来自未来，未来的你已经离我而去了。"
            phainon "现在的我……也没能救下你。"
            anaxa "呵，来自未来？"
            anaxa "不要寄希望于重来。失败的实验，重来千万次也没有用。"
            anaxa "要把希望留给你能创造的「变量」。"
            phainon "……"
            phainon "无论如何，我想走向有你的未来。"
            anaxa "别露出这副表情。"
            anaxa "还记得你当年毕业时的愿望吗？"
            anaxa "空白意味着无限可能，而英雄也是其中的一种。"
            phainon "……原来你全部都记得。"
            anaxa "哼，身为你的老师，我当然记得。"
            phainon "但我到头来也没能拯救世人，又能算什么英雄呢？"
            anaxa "学者终其一生探寻真理，而未能获得所求者千千万。"
            anaxa "但这并不意味着，其中间的过程都是无用功。英雄也同样。"
            anaxa "更何况自神悟树庭毕业后，你一直奋战在第一线，连信件也没以前寄得勤快。"
            phainon "老师是在责怪我吗？"
            anaxa "哼，怎么会。"
            phainon "抱歉，我只是……不想让你担心。"
            anaxa "白厄，你一直都是……咳、咳咳……"
            show anaxa eyeclose at right with Fade(1.5, 0.5, 1.5)
            phainon "……"
            phainon "……那刻夏老师？"
            phainon "……那刻夏老师！"
            anaxa "……"
            anaxa "……一直都是……令我骄傲的……学生。"
            show anaxa hurt2 at right with dissolve
            pause 2.0
            show cg death with Fade(1.5, 0.5, 1.5)
            $ unlock_cg("death")
            narrator "微弱的呼吸逐渐停止。"
            phainon "……永别了，吾师。"
            phainon "至少，这一次……我能和你好好道别了。"
            narrator "他长久拥抱着面前的身躯。沾在面颊的血逐渐干涸，和身躯一起慢慢失去温度。"
            show phainon sadhurt at left
            hide anaxa
            narrator "——直至粉蓝色的眼睛长久阖上后，他想起了那道时间规则。"
            hide cg with Fade(1.5, 0.5, 1.5)
            anaxa_no "请记住，你必须保守秘密，不能告诉任何一人你是时空穿越者，否则一切付出将{color=#FF0000}前功尽弃{/color}。"
            narrator "……没错，他没有遵守好这个规则。"
            stop music fadeout 2.0
            $ current_music = ""
            narrator "眼前的画面远去了。"
            scene bg black with Dissolve(2.0)
            hide phainon with Dissolve(2.0)
            $ current_music = "audio/prologue.mp3"
            play music "audio/prologue.mp3"
            scene bg initial with Dissolve(2.0)
            show phainon firm at left with fade
            narrator "短暂的第二次回溯里，他见到了濒死时的那刻夏。"
            narrator "关于神悟树庭的一切戛然而止。唯有手心里残余的冰冷在提醒他，那不是一场梦。"
            narrator "那刻夏的影子已然不在那里。等待他的，唯有即将被黑潮吞没的世界。"
            narrator "现在的翁法罗斯，已经步入倒计时。"
            phainon "……"
            jump branch_end_god
        "……":
            phainon "……"
            phainon "无论如何，我想走向有你的未来。"
            phainon "可是时至今日，我们仍然没能亲眼看到真实的星空。"
            anaxa "别露出这副表情。"
            anaxa "还记得你当年毕业时的愿望吗？"
            anaxa "空白意味着无限可能，而英雄也是其中的一种。"
            phainon "……原来你全部都记得。"
            anaxa "哼，身为你的老师，我当然记得。"
            phainon "但我到头来也没能拯救世人，又能算什么英雄呢？"
            anaxa "学者终其一生探寻真理，而未能获得所求者千千万。"
            anaxa "但这并不意味着，其中间的过程都是无用功。英雄也同样。"
            anaxa "更何况自神悟树庭毕业后，你一直奋战在第一线，连信件也没以前寄得勤快。"
            phainon "老师是在责怪我吗？"
            anaxa "哼，怎么会。"
            phainon "抱歉，我只是……不想让你担心。"
            anaxa "白厄，你一直都是……咳、咳咳……"
            show anaxa eyeclose at right with Fade(1.5, 0.5, 1.5)
            phainon "……"
            phainon "……那刻夏老师？"
            phainon "……那刻夏老师！"
            anaxa "……"
            anaxa "……一直都是……令我骄傲的……学生。"
            show anaxa hurt2 at right with dissolve
            pause 2.0
            show cg death with Fade(1.5, 0.5, 1.5)
            $ unlock_cg("death")
            narrator "微弱的呼吸逐渐停止。"
            phainon "……永别了，吾师。"
            phainon "至少，这一次……我能和你好好道别了。"
            narrator "他长久拥抱着面前的身躯。沾在面颊的血逐渐干涸，和身躯一起慢慢失去温度。"
            show phainon sadhurt at left
            hide anaxa
            narrator "温热的眼泪落在冰冷的身躯。而面前燃起的火种仍在提醒他，一切尚未结束。"
            hide cg with Fade(1.5, 0.5, 1.5)
            show cerces:
                xalign 0.5
                yalign 0.5
            with Dissolve(3.0)
            narrator "要带走理性火种吗？"
            menu:
                "带走它":
                    pass
                "不带走":
                    narrator "要就此放弃火种吗？"
                    menu:
                        "放弃火种":
                            narrator "确认要就此放弃火种吗？"
                            menu:
                                "确认放弃":
                                    narrator "理性火种的光芒逐渐黯淡。"
                                    scene bg black with Dissolve(5.0)
                                    narrator "就像千千万万的造物一样，慢慢溶解于黑潮中。"
                                    hide cerces with Dissolve(5.0)
                                    narrator "那熟悉的感觉再度来临，时间与空间继续折叠，没有任何留恋的余地。"
                                    jump branch_end_death
                                "带走火种":
                                    pass
                        "带走火种":
                            pass
            narrator "他带走了理性火种，神悟树庭所保存的希望。"
            show bg top at clear_to_blur
            show bg black with Dissolve(5.0)
            narrator "那熟悉的感觉再度来临，时间与空间继续折叠，没有任何留恋的余地。"
            show bg initial at mosaic_blur_slight with fade
            narrator "在模糊不清的画面里，他看见理性火种回到天幕。"
            hide cerces with Dissolve(3.0)
            show cg black with Dissolve(3.0)
            hide phainon
            jump chapter_03

# ========================================
# true end & staff list
# ========================================
label true_end:
    narrator "黑潮渐渐褪去，世界展露出真实的样貌。"
    phainon "这是……"
    scene bg sky at breathe_blur with Fade(1.5, 0.5, 1.5)
    narrator "当一切有形无形不再拥有边界。"
    narrator "他已经分不清现在身处于哪个空间。"
    narrator "就像回到了神悟树庭的某个平凡夜晚，草地里的微风如薄荷般清新。"
    narrator "不同于从前的则是，混沌的天幕被星空取而代之。"
    phainon "很高兴能够与你再次相见，那刻夏老师。"
    phainon "我们这是……在哪里？"
    anaxa "黑潮分解的那一瞬，带来庞大的力量将我们推向未知。"
    anaxa "这是我们记忆里从未存在过的，拥有星空的神悟树庭。"
    phainon "——嗯，看来我们做到了。"
    anaxa "这便是群星真实的模样。"
    anaxa "感觉如何？"
    phainon "我看到……宇宙正在流动。"
    scene bg black with Dissolve(3.0)
    show cg under_sky at breathe_light with Fade(1.5, 0.5, 1.5)
    $ unlock_cg("under_sky")
    phainon "我还记得您曾经说过，我们所能看到的星星，都是他们从前的影像。"
    phainon "反之则是，他们所看到的我们，或许尚未诞生。"
    anaxa "新生、发芽、成长、濒毁。"
    anaxa "最后，于一线希望里重生。"
    anaxa "这便是我们所走过的，通向真实的道路。"
    anaxa "从此往后，这样的星空不再是虚假的幻象。"
    phainon "这就是……真正的新世界。"
    anaxa "葬身于黑潮中的灵魂，将逐渐被炼金术解放出来。"
    phainon "新世界的人们，终于可以一同守望没有黑潮的明天。"
    scene bg black with Dissolve(5.0)
    $ current_music = ""
    stop music fadeout 2.0
    pause 3.0
    narrator "像一场漫长的梦终于迎来尾声，而只有亲历者才知晓，这并非梦乡。"
    narrator "氤氲麦香间，和煦的暖风迎面而来。"
    $ current_music = "audio/true_end.mp3"
    play music "audio/true_end.mp3" fadein 2.0
    narrator "梦中时常会出现的家乡，在被黑潮吞没以前，是个宁静祥和的村落。"
    narrator "与从前不同的则是，眼前的村落褪去黑潮后，安静得不同寻常。"
    scene bg almx at blur_to_clear(10.0) with Dissolve(5.0)
    narrator "——他回到了最初的哀丽秘榭。"
    narrator "空无一人的麦田里，熟悉的身影出现在眼前。"
    show cg gods with Fade(1.5, 0.5, 1.5)
    
    $ unlock_cg("cg_gods")
    anaxa "等待总是漫长的，虽说黑潮已经消退了，灵魂的解放仍然需要时间。"
    phainon "哈哈，我只是在想——原来一切都在你的计算之中。"
    anaxa "寄希望于不确定因素不是我的风格。"
    anaxa "我先一步抵达时间之外，直至过去的炼金术跨越时间，由你来完成首尾相连。"
    phainon "那么这一次，我交出的答卷能打几分？"
    anaxa "你心中应当已有答案。"
    phainon "我以为会有更多评语，或者……像往常一样的反问？"
    pause 3.0
    #stop music fadeout 2.0
    hide cg with dissolve
    pause 2.0
    show anaxa2 normal02 at right with fade
    anaxa "那么，哀丽秘榭的白厄——"
    show anaxa2 smile at right with dissolve
    pause 2.0
    anaxa "你的理想是什么？"
    pause 2.0
    hide anaxa2 with dissolve
    pause 5.0
    #play music "audio/chapter_02.mp3" fadein 2.0
    scene bg white with dissolve
    show expression Text("《See You Again》", size=64, color="#000", font="fonts/HuiWenMinCho.ttf") at truecenter as text_end with Dissolve(2.0)
    show phainon little normal at left with Dissolve(2.0)
    pause(2.0)
    hide phainon with fade
    show anaxa scholar normal at right with Dissolve(2.0)
    pause(2.0)
    hide expression text_end with Dissolve(2.0)
    hide anaxa with fade

    show phainon sad at left with Dissolve(2.0)
    show expression Text("原作  崩坏·星穹铁道 / CP：厄夏", size=32, color="#000", font="fonts/HuiWenMinCho.ttf") as text_end:
        xalign 0.7
        yalign 0.5
    with Dissolve(2.0)
    pause(2.0)
    hide expression text_end with Dissolve(2.0)
    hide phainon with fade
    
    show anaxa normal at right with Dissolve(2.0)
    show expression Text("演员  白厄/那刻夏", size=32, color="#000", font="fonts/HuiWenMinCho.ttf") as text_end:
        xalign 0.5
        yalign 0.5
    with Dissolve(2.0)
    pause(2.0)
    hide expression text_end with Dissolve(2.0)
    hide anaxa with fade 

    show phainon2 normal at left with Dissolve(2.0)
    show expression Text("美术/人设    游离态深蓝", size=32, color="#000", font="fonts/HuiWenMinCho.ttf") as text_end:
        xalign 0.7
        yalign 0.5
    with Dissolve(2.0)
    pause(2.0)
    hide expression text_end with Dissolve(2.0)
    hide phainon2 with fade 

    show anaxa2 normal at right with Dissolve(2.0)
    show expression Text("文案/程序    阿葵aaaoi", size=32, color="#000", font="fonts/HuiWenMinCho.ttf") as text_end:
        xalign 0.25
        yalign 0.5
    with Dissolve(2.0)
    pause(2.0)
    hide expression text_end with Dissolve(2.0)
    hide anaxa2 with fade
    show expression Text("音乐  Alex Productions/The Mountain/Kevin MacLeod", size=32, color="#000", font="fonts/HuiWenMinCho.ttf") at truecenter as text_end with Dissolve(2.0)
    hide expression text_end with Dissolve(2.0)
    show kephale:
        xalign 0.33
        yalign 0.4
    with Dissolve(2.0)
    show cerces:
        xalign 0.66
        yalign 0.4
    with Dissolve(2.0)
    show expression Text("Thanks for playing, and wish you a pleasant journey.", size=32, color="#000", font="fonts/HuiWenMinCho.ttf") as text_end:
        xalign 0.5
        yalign 0.75
    with Dissolve(2.0)
    pause 5.0
    scene cg white
    hide kephale
    hide cerces
    hide text_end with dissolve
    stop music fadeout 2.0
    $ current_music = ""
    scene bg almx with dissolve
    pause 2.0
    phainon "我的理想是——"
    show phainon2 normal at left with Dissolve(2.0)
    pause 2.0
    show phainon2 smile at left with dissolve
    phainon "创造实现理想的世界。"
    pause 2.0
    hide phainon2 with dissolve
    show text "{color=#000000}Ending C——True End\n新世界{/color}" at truecenter with dissolve
    pause 5.0
    hide text with dissolve
    pause 3.0
    menu:
        "返回主菜单":
            return


# ========================================
# CG 画廊
# ========================================
label cg_gallery:
    call screen cg_gallery_screen
    return


# ========================================
# load to restore music
# ========================================

label after_load:
    # 恢复音乐
    if current_music != "":
        play music current_music fadein 1.0
    return