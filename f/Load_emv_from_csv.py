
import openai
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.llms import OpenAI
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chains.question_answering import load_qa_chain
from langchain import PromptTemplate,LLMChain
import ast
import os
os.environ["OPENAI_API_KEY"]=""

import pandas as pd
from tabulate import tabulate

# column 1 is text chunks and 2 is emebddings
df =pd.read_csv('D:\\Learning\\openai\\thon exampls\\embeddings\\IronManSample.csv',header=None)

#print (tabulate(df,headers='keys'))
#Load into FAISS

texts =df[df.columns[0]].tolist()
embeddings =OpenAIEmbeddings()
text_embeddings = []
string_embeddings=df[df.columns[1]].tolist()

for item in string_embeddings:
    text_embeddings.append(ast.literal_eval(item))
text_embeddings_pairs = list(zip(texts,text_embeddings))

docsearch = FAISS.from_embeddings(text_embeddings_pairs,embeddings)

llm=OpenAI()

chain = load_qa_chain(llm,chain_type="stuff")

query = "What was Tony Stark famous for?"
docs = docsearch.similarity_search(query)


res = chain.run(input_documents=docs,question =query)
print (res)











