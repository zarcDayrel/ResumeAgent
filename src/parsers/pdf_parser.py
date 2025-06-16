import PyPDF2
import os

def parse_resume(pdf_path):
    """
    从 PDF 文件中提取文本内容
    
    Args:
        pdf_path (str): PDF 文件的路径
        
    Returns:
        str: 提取的文本内容，如果发生错误则返回空字符串
    """
    try:
        # 检查文件是否存在
        if not os.path.exists(pdf_path):
            raise FileNotFoundError(f"文件不存在: {pdf_path}")
            
        # 检查文件扩展名
        if not pdf_path.lower().endswith('.pdf'):
            raise ValueError(f"不是 PDF 文件: {pdf_path}")
        
        # 打开 PDF 文件
        with open(pdf_path, 'rb') as file:
            # 创建 PDF 读取器对象
            pdf_reader = PyPDF2.PdfReader(file)
            
            # 获取页数
            num_pages = len(pdf_reader.pages)
            
            # 存储所有页面的文本
            text_content = []
            
            # 遍历每一页并提取文本
            for page_num in range(num_pages):
                page = pdf_reader.pages[page_num]
                text_content.append(page.extract_text())
            
            # 将所有页面的文本合并
            return '\n'.join(text_content)
            
    except FileNotFoundError as e:
        print(f"错误: {str(e)}")
        return ""
    except ValueError as e:
        print(f"错误: {str(e)}")
        return ""
    except Exception as e:
        print(f"处理 PDF 时发生错误: {str(e)}")
        return ""

# 测试代码
if __name__ == "__main__":
    # 测试示例
    test_path = "resumes/candidate1.pdf"
    result = parse_resume(test_path)
    print("提取的文本内容:")
    print(result) 