1. Setup 和模型初始化（先跑通）
2. 消息类型 + Prompt + Output Parser（控制输入输出）
3. Documents/Embeddings/Vector Store/Retriever（RAG 基础）
4. Memory（多轮对话）
5. Chains（多步骤编排）
6. Agents（工具调用）

这个 notebook 本质上是一个“从 0 到 1 搭建 LangChain 应用”的实战课，主线非常清晰：

先把 LLM 跑起来
再学怎么“更好地问”（Prompt / Output Parser / Chains）
再学怎么“让模型看外部资料”（RAG）
最后学“让模型会行动”（Tools / Agents）

你做这本 lab 时最该关注的 3 个能力

能不能把“开放问题”改写成“结构化输入 + 结构化输出”
能不能把“复杂任务”拆成多个链式步骤
能不能用检索结果约束模型，减少幻觉


对于 template/index.html 来说，就是需要:

这个 template（templates/index.html）通常是被 Flask 的 render_template() 用的。
用户访问 /
app.py 里的路由函数执行
Flask 调 render_template("index.html")
返回渲染后的 HTML 给浏览器
浏览器再加载 /static/script.js 和 /static/styles.css



This is some simple HTML that will give us a form allowing us to call the /generate endpoint, passing a message and model selection.

