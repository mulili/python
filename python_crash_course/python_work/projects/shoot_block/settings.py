class Settings:
    """集中存储游戏《外星飞船入侵》中所有设置的类"""

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

        # 飞船设置
        self.ship_speed = 1.5  # 控制飞船移动速度
        self.ship_limit = 3  # 可用飞船数量
        self.ship_collided_num = 0  # 飞船被撞毁的次数

        # 子弹设置
        self.bullet_speed = 5  # 子弹速度比飞船稍快
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = (60, 60, 60)  # 深灰色
        # TODO: 持续开火功能
        # self.is_firing = False # 开火状态
        self.fired_bullets_num = 0  # 发射子弹数量统计

        # 外星飞船设置
        self.block_speed = 10  # 标靶上下移动速度
        self.block_direction = 1  # 1 向下，2向上
        self.block_destroyed_num = 0  # 统计被击毁的标靶的数量
