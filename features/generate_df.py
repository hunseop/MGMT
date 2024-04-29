import pandas as pd
import random
import string
import time

def generate_random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

def generate_dataframe(model, ip, id, pw, command):
    # 랜덤 데이터 생성
    seq = list(range(1, 11))  # 1부터 10까지의 순차적인 값
    ids = [generate_random_string(8) for _ in range(10)]  # 8글자의 랜덤 문자열
    sources = ['.'.join(str(random.randint(0, 255)) for _ in range(4)) for _ in range(10)]  # 랜덤 IPv4 주소
    users = [generate_random_string(6) for _ in range(10)]  # 6글자의 랜덤 문자열
    destinations = ['.'.join(str(random.randint(0, 255)) for _ in range(4)) for _ in range(10)]  # 랜덤 IPv4 주소
    services = [random.choice(['HTTP', 'FTP', 'SSH', 'SMTP']) for _ in range(10)]  # 랜덤 서비스
    applications = [generate_random_string(10) for _ in range(10)]  # 10글자의 랜덤 문자열
    descriptions = [generate_random_string(20) for _ in range(10)]  # 20글자의 랜덤 문자열
    
    sleep_time = random.randint(1, 3)  # 10에서 60초 사이의 랜덤한 시간
    
    print(f"함수 실행 대기 시간: {sleep_time} 초")
    time.sleep(sleep_time)  # 랜덤한 시간 동안 sleep
    
    # DataFrame 생성
    df = pd.DataFrame({
        'model': model,
        'command': command,
        'seq': seq,
        'id': ids,
        'source': sources,
        'user': users,
        'destination': destinations,
        'service': services,
        'application': applications,
        'description': descriptions
    })
    
    return df

if __name__ == '__main__':
    # 테스트
    model = "ModelX"
    ip = "192.168.1.100"
    id = "admin"
    pw = "password123"
    command = "analyze_traffic"
