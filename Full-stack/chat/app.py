from flask import Flask, render_template, request, jsonify
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.memory import ConversationBufferMemory
api_key = ""

app = Flask(__name__)

# 전역 메모리 객체 생성
memory = ConversationBufferMemory(
    return_messages=True,
    memory_key="chat_history"
)

# 모델 설정
model = ChatOpenAI(model="gpt-4o", api_key=api_key, temperature=0.2, max_tokens=300)
parser = StrOutputParser()

# 프롬프트 템플릿 (메모리 포함)
prompt_template = ChatPromptTemplate.from_messages([
    ("system", "You are helpful AI who talk like kind human species. But you answer shortly."),
    MessagesPlaceholder(variable_name="chat_history"),
    ("user", "{text}")
])

# 체인 설정
chain = prompt_template | model | parser

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/chat', methods=['GET', 'POST'])
def chat():
    if request.method == 'GET':
        return render_template('chat.html')
    
    elif request.method == 'POST':
        try:
            user_message = request.json['message']
            
            # 대화 기록 가져오기
            chat_history = memory.load_memory_variables({})["chat_history"]
            
            # 응답 생성
            response = chain.invoke({
                "text": user_message,
                "chat_history": chat_history
            })
            
            # 메모리 업데이트
            memory.save_context(
                {"input": user_message},
                {"output": response}
            )
            
            return jsonify({'response': response})
        except Exception as e:
            return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)