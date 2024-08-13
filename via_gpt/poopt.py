from Input_text_generator import json_to_query

def query_to_gpt():
    query = json_to_query('/mnt/sdb/tmp/poopsee/langchain/via_gpt/dummy.json')
    print(query)

if __name__ == "__main__":
    query_to_gpt()