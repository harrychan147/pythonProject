import openai
import tiktoken

# encoding = tiktoken.encoding_for_model("text-embedding-ada-002")
# encoding.encode("My Name is IronMan")
encoding_name = "text-embedding-ada-002"
text="My Name is IronMan"

def num_tokens_from_strings(text: str, encoding_name: str) -> Int:
    encoding = tiktoken.encoding_for_model(encoding_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens

