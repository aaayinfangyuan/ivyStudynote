# 09. 使用 dict 和 set

## 一、知识点

键值对、唯一元素、快速查找。

## 二、专业术语

- Dictionary —— 字典
- Key —— 键
- Value —— 值
- Set —— 集合

## 三、语法

```python
scores = {"Alice": 95}
scores["Bob"] = 88
numbers = {1, 2, 2, 3}
```

## 四、示例代码

```python
scores = {"Alice": 95}
scores["Bob"] = 88
numbers = {1, 2, 2, 3}
```

## 五、注意事项

- dict 的键必须是不可变对象。
- get() 获取不存在的键时更安全。
- set 自动去重，没有固定顺序。

## 六、常用函数/方法

### `get()`

作用：安全获取字典值

```python
scores.get("Tom", 0)
```
### `add()`

作用：向 set 添加元素

```python
numbers.add(4)
```

## 七、我的理解

> dict 用名字查数据，set 用来去重或判断成员是否存在。

<!-- 在这里写下你自己的理解。修改后按 Ctrl + S 保存，再执行 Git 提交。 -->
