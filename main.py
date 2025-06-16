import os
from pdf_parser import parse_resume
from resume_parser import extract_candidate_info
from resume_matcher import ResumeMatcher

def main():
    """
    主程序：实现简历处理的完整流程
    """
    try:
        # 1. 指定简历路径
        resume_path = "resumes/candidate1.pdf"
        
        # 检查简历文件是否存在
        if not os.path.exists(resume_path):
            raise FileNotFoundError(f"简历文件不存在: {resume_path}")
        
        # 2. 解析 PDF 文件
        print("正在解析 PDF 文件...")
        resume_text = parse_resume(resume_path)
        if not resume_text:
            raise ValueError("PDF 解析失败，未能提取到文本内容")
        
        # 3. 提取简历关键信息
        print("正在提取简历关键信息...")
        candidate_info = extract_candidate_info(resume_text)
        
        # 打印提取到的信息
        print("\n提取的简历信息：")
        for key, value in candidate_info.items():
            print(f"{key}: {value}")
        
        # 4. 示例岗位 JD
        job_description = """
        职位：Python 开发工程师
        
        岗位要求：
        1. 本科及以上学历，计算机相关专业
        2. 3年以上 Python 开发经验
        3. 熟悉 Django/Flask 等 Web 框架
        4. 熟悉 MySQL、Redis 等数据库
        5. 有良好的代码风格和文档习惯
        6. 有团队协作精神和沟通能力
        
        工作职责：
        1. 负责公司核心业务系统的设计和开发
        2. 参与系统架构设计和技术方案制定
        3. 编写技术文档和单元测试
        4. 解决系统运行中的技术问题
        """
        
        # 5. 使用 LLM Chain 进行匹配评估
        print("\n正在进行简历匹配评估...")
        matcher = ResumeMatcher()
        evaluation_result = matcher.evaluate_match(job_description, resume_text)
        
        # 6. 打印评估结果
        if evaluation_result["status"] == "success":
            print("\n评估结果：")
            print(evaluation_result["evaluation"])
        else:
            print(f"\n评估失败：{evaluation_result['message']}")
            
    except FileNotFoundError as e:
        print(f"错误：{str(e)}")
    except ValueError as e:
        print(f"错误：{str(e)}")
    except Exception as e:
        print(f"程序执行过程中发生错误：{str(e)}")

if __name__ == "__main__":
    main() 