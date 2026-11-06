# 10. 函数

## 一、知识点

定义、参数、返回值、调用。

## 二、专业术语

- Function —— 函数
- Parameter —— 参数
- Return Value —— 返回值

## 三、语法

```python
def absolute_value(x):
    if x >= 0:
        return x
    return -x
```

## 四、示例代码

```python
def absolute_value(x):
    if x >= 0:
        return x
    return -x
```

## 五、注意事项

- 函数定义使用 def，末尾有括号和冒号。
- 没有 return 时，函数默认返回 `None`。

## 六、常用函数/方法

### `abs()`

作用：返回绝对值

```python
abs(-10)
```
### `max()`

作用：返回最大值

```python
max(2, 8, 3)
```

## 七、我的理解

> 函数把可重复的逻辑封装起来，调用时关注输入和输出。

<!-- 在这里写下你自己的理解。修改后按 Ctrl + S 保存，再执行 Git 提交。 -->
