# LangChain

you will construct a QA bot that 
automates this process. By leveraging LangChain and an LLM, 
the bot will read and understand the content of loaded PDF documents, 
enabling it to provide precise answers to user queries. 
You will integrate the tools and techniques, 
from document loading, text splitting, embedding, vector storage, 
and retrieval, to create a seamless and user-friendly experience 
via a Gradio interface.



# cmd

# installing necessary packages in my_env
python3.11 -m pip install \
gradio==4.44.0 \
ibm-watsonx-ai==1.1.2  \
langchain==0.2.11 \
langchain-community==0.2.10 \
langchain-ibm==0.1.11 \
chromadb==0.4.24 \
pypdf==4.3.1 \
pydantic==2.9.1


Serve the application
To serve the application, paste the following into your Python terminal:


bash
python3.11 qabot.py
Run
If you cannot find an open Python terminal or the buttons on the above cell do not work, you can launch a terminal by going to Terminal --> New Terminal. However, if you launch a new terminal, do not forget to source the virtual environment you created at the beginning of this lab before running this line:


shell
source my_env/bin/activate # activate my_env



