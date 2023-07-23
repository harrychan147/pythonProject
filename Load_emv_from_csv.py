
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chains.question_answering import load_qa_chain
from langchain import PromptTemplate,LLMChain
import ast

import pandas as pd

df =pd.read_csv("D:\\Learning\\openai\\thon exampls\\embeddings\\IronManSample.csv")
print(df.count())
df.head()

#Load into FAISS



