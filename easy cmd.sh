
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
