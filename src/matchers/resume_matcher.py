from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from typing import Dict, Any

class ResumeMatcher:
    def __init__(self, model_name: str = "qwen"):
        """
        初始化简历匹配器
        
        Args:
            model_name (str): Ollama 模型名称，默认为 "qwen"
        """
        # 初始化 Ollama LLM
        self.llm = Ollama(model=model_name)
        
        # 定义提示模板
        self.prompt_template = PromptTemplate(
            input_variables=["job_description", "resume_text"],
            template="""你是专业的HR助手，请根据以下岗位要求和候选人简历内容进行匹配度评估：

【岗位JD】:
{job_description}

【候选人简历】:
{resume_text}

请输出以下内容：
1. 总体匹配度评分（满分10分）
2. 候选人的主要优势
3. 候选人的主要短板
4. 是否推荐该候选人进入下一轮面试？为什么？

回答要简洁明了，结构清晰。"""
        )
        
        # 创建 LLM Chain
        self.chain = LLMChain(
            llm=self.llm,
            prompt=self.prompt_template
        )
    
    def evaluate_match(self, job_description: str, resume_text: str) -> Dict[str, Any]:
        """
        评估简历与岗位的匹配度
        
        Args:
            job_description (str): 岗位描述文本
            resume_text (str): 候选人简历文本
            
        Returns:
            Dict[str, Any]: 评估结果
        """
        try:
            # 调用 chain 进行评估
            result = self.chain.invoke({
                "job_description": job_description,
                "resume_text": resume_text
            })
            
            return {
                "status": "success",
                "evaluation": result["text"]
            }
            
        except Exception as e:
            return {
                "status": "error",
                "message": f"评估过程中发生错误: {str(e)}"
            }

# 测试代码
if __name__ == "__main__":
    # 测试数据
    test_jd = """
    职位：Python 开发工程师
    
    岗位要求：
    1. 本科及以上学历，计算机相关专业
    2. 3年以上 Python 开发经验
    3. 熟悉 Django/Flask 等 Web 框架
    4. 熟悉 MySQL、Redis 等数据库
    5. 有良好的代码风格和文档习惯
    6. 有团队协作精神和沟通能力
    """
    
    test_resume = """
    张三
    电话：13812345678
    邮箱：zhangsan@example.com
    
    教育背景：
    2018-2022 北京大学 计算机科学与技术 本科
    
    工作经历：
    2022-至今 ABC科技有限公司 软件工程师
    负责公司核心系统的开发和维护
    使用 Python + Django 开发 Web 应用
    负责数据库设计和优化
    
    技能：
    Python, Django, MySQL, Redis, Git
    """
    
    # 创建匹配器实例
    matcher = ResumeMatcher()
    
    # 执行评估
    result = matcher.evaluate_match(test_jd, test_resume)
    
    # 打印结果
    if result["status"] == "success":
        print("评估结果：")
        print(result["evaluation"])
    else:
        print(f"错误：{result['message']}") 