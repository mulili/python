class Settings:
    """集中存储游戏《外星人入侵》中所有设置的类"""

    def __init__(self):
        """初始化游戏的设置"""
        self.frame_rate = 60  # Pygame 尽可能的确保这个循环每秒恰好运行60秒
        self.display_caption = "👾 Alien Invasion 👾"  # 设置游戏标题
        # 指定游戏窗口的尺寸(宽、高)
        self.default_screen_width = 600
        self.default_screen_height = 900
        self.screen_width = 600
        self.screen_height = 900
        # 设置游戏屏幕背景色，RGB，red, green, blue, 0~255
        self.bg_color = (230, 230, 230)  # 浅灰色
        self.ship_speed = 1.5 # 控制飞船移动速度
        