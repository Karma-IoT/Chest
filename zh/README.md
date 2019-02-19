# Chest

> Each `Chest` is a separate code package.

`Chest` is an universal packages manager.

---
Maintainer:
- [tiannian](https://github.com/tiannian) &lt;dtiannian@aliyun.com>,dtiannian@gmail.com&gt;

## 目标

- 管理源代码之间的依赖，并能够方便快捷的编译于构建这些代码。
- 管理不同目标平台的工具链，实现针对不同平台的交叉编译。
- 预设插件机制，便于扩展。
- 管理二进制预编译代码，针对不同平台可以进行分发。

## 规范目录

- 包
  - chest.toml
  - 项目结构
  - 模板
  - 交叉编译
  - 测试
- 全局
  - SYSROOT
  - Embedcode
  - 依赖
  - 设备
  - 源
  - 账户
  - 插件
- 扩展
  - 模板类型扩展
  - 设备扩展
    - 本地设备
    - 串口设备
    - ssh设备
    - docker设备
    - Karma OTA设备
  - 源扩展
    - Github源
    - File源
    - HTTP源
    - FTP源
    - IPFS源

## 实现项目

- [Embedcode](https://github.com/ecode) - 单头文件的Embedcode的C++实现。
- [Chepp]() - 通用包管理器 `Chest` 的C++实现。

## 参与项目

我们欢迎对Karma项目感兴趣，志同道合的朋友参与。

规范采用提交issues的方式来改进系统与设计。

