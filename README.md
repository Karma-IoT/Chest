# Chest
Each `Chest` is a separate code package


## Reference

* project.name 名
* project.family 家族名
* project.version 版本
* project.maintainer 维护者
* project.upstream 上游
* project.platform 平台
* project.arch 架构
* chest."name" 继承chest
* build."target".src 来源
* build."target".rule 规则
* rule."name".command 规则命令
* rule."name"."ninja_variable" ninja规则变量
* tool."name".upstream 上游
* tool."name"."ninja_variable" 变量
* command."name" 命令
* init.folder=[] 初始化文件夹
* init.command=[] 初始化命令
* init.file=[] 初始化文件
* export.path=name 导出文件夹
