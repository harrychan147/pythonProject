import csv

import openai

openai.api_key = ""

input_text = "Ironman, also known as Tony Stark, is a fictional superhero in the Marvel Comics universe. Created by writer Stan Lee, he first appeared in 'Tales of Suspense' #39 in 1963. Tony Stark is a genius billionaire, inventor, and industrialist who becomes the armored superhero, Ironman, after constructing a powered exoskeleton suit. Using his intelligence and technological prowess, he fights against villains and uses his wealth to develop advanced weaponry and technology for the betterment of society. Ironman's character has become one of the most iconic and beloved figures in popular culture, featuring in numerous comic books, movies, and TV shows."

csv_path= "D:\\Learning\\openai\\thon exampls\\embeddings\\IronManSample.csv"

def create_embeddings(text: str, model="text-embedding-ada-002"):
    embeddings = []
    try:
        embedding = openai.Embedding.create(
            input=text,
            model=model
        )["data"][0]["embedding"]
        return embedding
    except:
        print(f"Error in creating Embeddings: {e}")
        return None



def write_embeddings_to_csv(embeddings,csv_path,input_text):
    with open(csv_path,"w",newline="") as csvFile:
        print(embeddings)
        embeddings = '"' + input_text + '"' + "," + '"' + str(embeddings) + '"'
        csvFile.write(embeddings)

embeddings_created = create_embeddings(input_text)

write_embeddings_to_csv(embeddings_created,csv_path,input_text)

print(len(embeddings_created))
