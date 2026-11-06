# 06. 使用 list 和 tuple

## 一、知识点

有序集合、可变与不可变、索引。

## 二、专业术语

- List —— 列表
- Tuple —— 元组
- Index —— 索引
- Mutable —— 可变

## 三、语法

```python
names = ["Michael", "Bob"]
names.append("Tracy")
point = (10, 20)
```

## 四、示例代码

```python
names = ["Michael", "Bob"]
names.append("Tracy")
point = (10, 20)
```

## 五、注意事项

- 索引从 0 开始，最后一个元素可用 `-1`。
- list 可以修改，tuple 创建后通常不能修改。
- 单元素 tuple 要写成 `(1,)`。

## 六、常用函数/方法

### `append()`

作用：在 list 末尾添加元素

```python
names.append("Adam")
```
### `pop()`

作用：删除并返回元素

```python
names.pop()
```

## 七、我的理解

> list 适合会变化的数据，tuple 适合固定的数据。

<!-- 在这里写下你自己的理解。修改后按 Ctrl + S 保存，再执行 Git 提交。 -->
