from setuptools import setup, find_packages

setup(
    name="ResumeAgent",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "PyPDF2==3.0.1",
        "numpy>=2.1.0",
        "langchain>=0.1.0",
        "langchain-community>=0.0.28",
        "langchain-core>=0.1.27",
    ],
    author="Your Name",
    author_email="your.email@example.com",
    description="智能简历分析系统",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/ResumeAgent",
    classifiers=[
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.12",
) 