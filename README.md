# ivyStudynote

这是一个支持“网页编辑 → Markdown 文件落盘 → Git/GitHub 保存版本”的 Python 学习笔记项目。

## 工作原理

- 网页端可以像普通文档一样编辑每章七个固定模块下的内容。网页不显示 Markdown 源码。
- 点击网页的“保存到 Markdown 文件”后，内容被写入真实的 `notes/*.md` 文件。
- VS Code 会立即把这些文件标为已修改。
- Git 提交和 GitHub 推送保存的是 Markdown 文件的真实历史，而不是浏览器缓存。

## 第一次启动

1. 用 VS Code 打开整个 `D:\ivy\ivyStudynote` 文件夹。
2. 双击项目根目录的 `启动网站.bat`。
3. 出现 `Python 学习笔记已启动：http://127.0.0.1:8765/` 后，不要关闭该黑色窗口。
4. 在浏览器打开：<http://127.0.0.1:8765/>
5. 网页中点击“编辑本章”，修改内容，点击“保存到 Markdown 文件”。

> 需要电脑已安装 Python，并且终端中可以运行 `python --version`。这套可写入版本不使用 Live Server / Five Server。

## 编辑与保存

- 网页中：标题固定，直接编辑排版后的内容；工具栏支持加粗、斜体、列表、引用和代码块，保存后自动转换并写入 `notes`。
- VS Code 中：直接修改 `notes/*.md`，按 `Ctrl + S`；网页点击“重新读取文件”即可看到更新。
- 任何一边修改后，建议先保存，再在另一边重新读取，避免两个版本互相覆盖。

## Git 首次初始化与 GitHub 推送

先在 GitHub 新建一个**空仓库** `ivyStudynote`（不要初始化 README）。然后在 VS Code 终端运行：

```powershell
cd D:\ivy\ivyStudynote
git init
git add .
git commit -m "feat: 初始化 Python 学习笔记"
git branch -M main
git remote add origin https://github.com/你的用户名/ivyStudynote.git
git push -u origin main
```

## 每次学习后

```powershell
git status
git add notes/
git commit -m "notes: 更新第 10 章函数笔记"
git push
```

## 找回误删内容

每次提交后，GitHub 会保存一个版本。可在 GitHub 仓库的 **Commits** 查看历史。未提交的更改可以在 VS Code 的“源代码管理”中查看或放弃。

## 添加章节

1. 在 `notes/` 创建新的 `.md` 文件；保留七个 `##` 标题。
2. 在 `notes/index.json` 添加章节编号、标题和文件名。
3. 保存后点击网页的重新读取按钮，或刷新网页。

## 网页展示说明

网页阅读模式会将 Markdown 的加粗、斜体、列表、引用和代码块渲染为正常文档样式；你不会在阅读时看到 `**` 等 Markdown 标记。
