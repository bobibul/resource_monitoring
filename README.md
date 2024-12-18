# python 버전 : 3.8.10

## 필요한 패키지 설치 : $pip install -r requirements.txt
## 실행 파일 : client.py, server.py


## 실행 방법
1. server.py 실행 후 왼쪽 하단 IP 주소 확인
2. client.py 실행 후 오른쪽 하단 server ip 에 서버 프로그램 IP 주소 입력(한 컴퓨터일 경우 127.0.0.1)
3. connect 버튼 누를 시 서버에 연결
4. 서버에서 해당 IP 주소의 off 버튼 누를 시 컴퓨터 종료됨
5. 다음 연결 시도 시 자동으로 서버 IP 주소 설정됨

# 배포 방법
$python setup.py build 
