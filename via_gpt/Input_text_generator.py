import json

def json_to_query(file):
    with open(file) as json_file:
        data = json.load(json_file)
        print(data)
        ID = data['IMG-id']
        color_code = data['color-code']
        bristol = data['bristol']
        blood = data['blood']

        query = f"사용자의 대변 색상 코드: {color_code}, 브리스톨 지수: {bristol}, 혈액 존재: {'있음' if blood else '없음'}이야, 이에 대한 건강 상태와 관련된 의심되는 상황을 해결하기 위해, 나에게 추가적인 질문을 한가지만 해줘"
        
        response = """model="gpt-4o"
            response_format={"type": "json_object"},
            messages=[
                {"role":"system",
                "content": "You are a helpful assistant designed to ouput JSON."},
                {"role": "user", "content": """f"{query}""""},
            ]"""

        return query, response




        