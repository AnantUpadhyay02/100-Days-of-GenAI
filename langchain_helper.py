from langchain.prompts import PromptTemplate
from langchain.llms import HuggingFaceHub
from langchain.chains import LLMChain
import os
import sys
sys.path.append("/Users/anantupadhyay/Downloads/API")
import api_key
api_hf = api_key.hf_key
os.environ['HUGGINGFACEHUB_API_TOKEN'] = api_hf


def generate_business_name(business):
    prompt_template_name = PromptTemplate(
                                            input_variables = ['business'],
                                            template = "A {business} in france"
                                        )
    prompt_template_name.format(business=business)
    
    llm = HuggingFaceHub(
                            repo_id="gpt2",
                            model_kwargs={"temperature": 0.6},
                        )
    
    chain = LLMChain(llm=llm, prompt=prompt_template_name)
    chain.run(business)
    

    return {
        "business_name":"Henry's bakery",
        "products":{"bread","cake","cookies"}
    }