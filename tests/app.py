from flask import Flask, render_template, jsonify, request
import time
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run_task', methods=['POST'])
def run_task():
    task_duration = random.randint(1, 5)  # 1에서 5초 사이의 랜덤한 시간 동안 작업을 시뮬레이션
    for i in range(task_duration):
        time.sleep(1)
        remaining_time = task_duration - i
        # 진행 상황을 클라이언트로 전송
        yield jsonify({'remaining_time': remaining_time})
    yield jsonify({'status': 'Task completed'})

if __name__ == '__main__':
    app.run(debug=True)
