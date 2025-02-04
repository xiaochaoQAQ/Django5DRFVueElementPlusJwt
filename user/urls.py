from django.urls import path
from user.views import TestView, JwtTestView, LoginView, SaveView, PwdView, AvatarView, ImageView, SearchView, \
    ActionView, CheckView, PasswordView, StatusView, GrantRole

urlpatterns = [
    path('test', TestView.as_view(), name='test'),  # 测试
    path('jwt_test', JwtTestView.as_view(), name='jwt_test'),  # jwt测试
    path('login', LoginView.as_view(), name='login'),  # 登录
    path('save', SaveView.as_view(), name='save'),  # 用户添加或者修改
    path('updateUserPwd', PwdView.as_view(), name='updateUserPwd'),  # 修改密码
    path('updateAvatar',AvatarView.as_view(), name='updateAvatar'), # 更新头像
    path('uploadImage', ImageView.as_view(), name='uploadImage'), # 头像上传
    path('search', SearchView.as_view(), name='search'),  # 用户信息分页查询
    path('action', ActionView.as_view(), name='action'), # 用户信息操作
    path('check', CheckView.as_view(), name='check'), # 用户名查重
    path('resetPassword', PasswordView.as_view(), name='resetPassword'),  # 密码重置
    path('status', StatusView.as_view(), name='status'), # 状态修改
    path('grantRole',GrantRole.as_view(), name='grant'), # 角色授权
]
