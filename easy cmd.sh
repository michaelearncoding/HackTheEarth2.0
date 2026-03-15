
conda activate llm
jupyer notebook

conda create -n llm python=3.11
conda activate llm                 

pip install ipykernel
python -m ipykernel install --user --name llm --display-name "Python (llm)"

python -m pip install --upgrade pip
pip install \
  tenacity==8.2.3 \
  ibm-watsonx-ai==1.0.8 \
  ibm-watson-machine-learning==1.0.367 \
  langchain-ibm==0.1.7 \
  langchain-community==0.2.10 \
  langchain-experimental==0.0.62 \
  langchainhub==0.1.18 \
  langchain==0.2.11 \
  pypdf==4.2.0 \
  chromadb==0.4.24 \
  ipykernel

git push --set-upstream origin feature/MM_Setup_Initial

git rm -r --cached IBM
git commit -m "stop tracking IBM folder"

pip install flask

pip install Flask langchain-ibm langchain

wget -O static/script.js "https://gist.githubusercontent.com/tenzinmigmar/0168709391266a8d8da7936f1a866c71/raw/95f4f4e1a1966b3f5183dd2f822cfcfd08d2238a/script.js"

一个命令行下载工具，用来从 URL 拉文件。

-- -O 表示“输出到这个文件名”。
意思是把下载内容保存成你项目里的 static/script.js。

wget -O static/styles.css "https://gist.githubusercontent.com/tenzinmigmar/278575598f79a4940993a1fc8640a60a/raw/24eda98885e854b01b4a46d1756112e91d3acc10/styles.css"


conda create -n chroma-lab python=3.11 -y
conda activate chroma-lab
pip install -r requirements.txt

git rm --cached Sandbox/gitnexus
