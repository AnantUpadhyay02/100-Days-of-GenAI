from langchain.llms import HuggingFaceHub
import os
import sys
sys.path.append("/Users/anantupadhyay/Downloads/API")
import api_key
api_hf = api_key.hf_key


os.environ['HUGGINGFACEHUB_API_TOKEN'] = api_hf
llm = HuggingFaceHub(
    repo_id="distilgpt2",
    model_kwargs={"temperature": 0.6},
)
print("llm set")
name = llm("Suggest a name for a tech startup")
print(name)
