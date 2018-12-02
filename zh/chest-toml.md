# Chest.toml
`chest.toml`是包的主文件，采用TOML格式定义，记录了包中的所有信息。

## Structure 
### Project section
Project定义了Chest包的主要信息。这些信息用于标识包。
#### project.name
>  类型: String

记录包名，用于标识一个包。

#### project.family
> 类型: String

家族名，一般为开发者的名字，标识包所属的域（domain）。与project.name结合共同标记一个包。

#### project.version
> 类型: String

包的当前版本，使用语义化版本号。

#### project.maintainer
> 类型: Array of string or Array of object

记录包的维护者信息。

如果array中存储的是string，则维护者信息以如下格式存储: 

```toml
maintainer = [
    "Alice <Alice@example.com>",
]
```

如果array中存储的是table，则维护者信息以如下格式存储：

```
maintainer = [
    {name = "Alice", email = "Alice@example.com"},
]
```

#### project.target

> 类型: Array of string

记录包兼容的目标设备。

可兼容的目标是一个字符串，结构按照如下方式组织:

```
arch-vendor-framework-platform-compiler
```

### Chest section
Chest部分中记录了当前包如何导入或配置其他的toml配置文件。
#### chest.import

> 类型: Table array

记录了如何导入外部toml配置文件。每一个table只存在一个key-value对，key表示外部包的索引，value表示要导入的toml文件相对外部包src目录的路径。

> 注：chest.import不能导入外部项目的chest.toml文件。

Example：

```toml
[[section.import]]
"tiannian/chest" = "build.cc"
[[section.import]]
"tiannian/chest" = "build.cc"
```

### Tool Section

Tool Section中记录了

### Rule Section

### Build Section

### Command Section

### Initial Section

### Export Section

### Dependences Section

## Reference
chest."name" 继承chest
build."target".src 来源
build."target".rule 规则
rule."name".command 规则命令
rule."name"."ninja_variable" ninja规则变量
tool."name".upstream 上游
tool."name"."ninja_variable" 变量
command."name" 命令