# week4_api_bot.py 简易API对话机器人
import os

# 从系统环境变量读取API密钥，不要直接写密钥字符串在代码里
api_key = os.getenv("LLM_API_KEY")

def bot_reply(user_msg: str):
    """简易对话函数，模拟API调用返回回答"""
    if api_key is None:
        return "【提示】未读取到环境变量API_KEY，当前为模拟模式。\n" + simulate_answer(user_msg)
    else:
        # 真实场景：这里写request请求大模型API
        return "【真实API模式】调用大模型返回：\n" + simulate_answer(user_msg)

def simulate_answer(question):
    """模拟大模型回答，用于演示，不需要真实API也能跑通演示"""
    if "Python" in question:
        return "Python是解释型编程语言，语法简洁，适合AI、脚本开发。"
    elif "提示词" in question:
        return "提示词就是给AI的指令，清晰的约束可以提升AI输出质量。"
    elif "词汇提取" in question:
        return "词汇提取工具可以从文本中拆分词汇，过滤标点、去重，整理词表。"
    else:
        return "收到你的问题，请继续提问。"

if __name__ == "__main__":
    print("===== API对话小机器人 =====")
    print("输入问题，输入quit退出\n")
    while True:
        user_input = input("你：")
        if user_input.lower() == "quit":
            print("机器人：再见！")
            break
        answer = bot_reply(user_input)
        print(f"机器人：{answer}\n")
