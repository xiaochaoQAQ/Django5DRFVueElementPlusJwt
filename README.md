Python 3.11 + Django5 + DRF + JWT + MySQL8

创建Django项目，移除内置Admin模块，采用多模块开发（user、role、menu）。

配置数据库连接、JWT认证（djangorestframework-jwt）。

实现用户实体类SysUser、角色类SysRole、菜单类SysMenu，并通过迁移生成数据表。

使用DRF序列化器（ModelSerializer）处理数据序列化与反序列化。

自定义中间件JwtAuthenticationMiddleware实现全局Token鉴权。
