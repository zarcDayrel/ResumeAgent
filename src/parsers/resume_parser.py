import re
from typing import Dict, List, Union

def extract_candidate_info(resume_text: str) -> Dict[str, Union[str, List[str]]]:
    """
    从简历文本中提取关键信息
    
    Args:
        resume_text (str): 简历文本内容
        
    Returns:
        Dict[str, Union[str, List[str]]]: 包含提取信息的字典
    """
    # 初始化结果字典
    result = {
        "name": "",
        "phone": "",
        "email": "",
        "education": "",
        "experience": "",
        "skills": []
    }
    
    # 提取姓名（假设姓名在文本开头，2-4个中文字符）
    name_pattern = r'^[\u4e00-\u9fa5]{2,4}'
    name_match = re.search(name_pattern, resume_text.strip())
    if name_match:
        result["name"] = name_match.group()
    
    # 提取电话号码（支持多种格式：手机号、座机号）
    phone_pattern = r'(?:1[3-9]\d{9}|0\d{2,3}-\d{7,8})'
    phone_match = re.search(phone_pattern, resume_text)
    if phone_match:
        result["phone"] = phone_match.group()
    
    # 提取邮箱
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    email_match = re.search(email_pattern, resume_text)
    if email_match:
        result["email"] = email_match.group()
    
    # 提取教育背景（假设在"教育背景"或"教育经历"等关键词之后）
    education_pattern = r'(?:教育背景|教育经历|学历)[：:]\s*(.*?)(?=\n\n|\Z)'
    education_match = re.search(education_pattern, resume_text, re.DOTALL)
    if education_match:
        result["education"] = education_match.group(1).strip()
    
    # 提取工作经历（假设在"工作经历"或"工作经验"等关键词之后）
    experience_pattern = r'(?:工作经历|工作经验)[：:]\s*(.*?)(?=\n\n|\Z)'
    experience_match = re.search(experience_pattern, resume_text, re.DOTALL)
    if experience_match:
        result["experience"] = experience_match.group(1).strip()
    
    # 提取技能列表（假设在"技能"或"专业技能"等关键词之后）
    skills_pattern = r'(?:技能|专业技能)[：:]\s*(.*?)(?=\n\n|\Z)'
    skills_match = re.search(skills_pattern, resume_text, re.DOTALL)
    if skills_match:
        # 将技能文本分割成列表（按逗号、分号或换行符分割）
        skills_text = skills_match.group(1).strip()
        skills_list = re.split(r'[,，;；\n]', skills_text)
        # 清理每个技能项（去除空白字符）
        result["skills"] = [skill.strip() for skill in skills_list if skill.strip()]
    
    return result

# 测试代码
if __name__ == "__main__":
    # 测试示例
    test_resume = """
    张三
    电话：13812345678
    邮箱：zhangsan@example.com
    
    教育背景：
    2018-2022 北京大学 计算机科学与技术 本科
    
    工作经历：
    2022-至今 ABC科技有限公司 软件工程师
    负责公司核心系统的开发和维护
    
    技能：
    Python, Java, SQL, Linux, Git
    """
    
    result = extract_candidate_info(test_resume)
    print("提取的简历信息：")
    for key, value in result.items():
        print(f"{key}: {value}") 