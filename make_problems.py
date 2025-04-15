import json

original_problems = {
    "최댓값 찾기": {
        "description": "리스트 [1, 10, 25, 33, 7] 안에서 가장 큰 값을 찾아 출력하세요.",
        "input_example": "[1, 10, 25, 33, 7]",
        "expected_output": "33"
    },
    "최솟값 찾기": {
        "description": "리스트 [1, 10, 25, 33, 7] 안에서 가장 작은 값을 찾아 출력하세요.",
        "input_example": "[1, 10, 25, 33, 7]",
        "expected_output": "1"
    },
    "평균값 구하기": {
        "description": "리스트 [4, 8, 15, 16, 23, 42]의 평균을 계산하여 출력하세요.",
        "input_example": "[4, 8, 15, 16, 23, 42]",
        "expected_output": "18.0"
    },
    "리스트 정렬": {
        "description": "리스트 [5, 1, 4, 2, 8]를 오름차순으로 정렬하여 출력하세요.",
        "input_example": "[5, 1, 4, 2, 8]",
        "expected_output": "[1, 2, 4, 5, 8]"
    },
    "중복 제거": {
        "description": "리스트 [1, 2, 2, 3, 4, 4, 5]에서 중복을 제거하여 출력하세요.",
        "input_example": "[1, 2, 2, 3, 4, 4, 5]",
        "expected_output": "[1, 2, 3, 4, 5]"
    },
    "소수 판별": {
        "description": "숫자를 입력받아 소수인지 판별하여 출력하세요.",
        "input_example": "7",
        "expected_output": "True"
    },
    "팩토리얼 계산": {
        "description": "숫자를 입력받아 팩토리얼을 계산하여 출력하세요.",
        "input_example": "5",
        "expected_output": "120"
    },
    "피보나치 수열": {
        "description": "숫자를 입력받아 그 수까지의 피보나치 수열을 출력하세요.",
        "input_example": "5",
        "expected_output": "[0, 1, 1, 2, 3]"
    },
    "문자열 뒤집기": {
        "description": "문자열을 입력받아 거꾸로 뒤집어 출력하세요.",
        "input_example": "hello",
        "expected_output": "olleh"
    },
    "모음 개수 세기": {
        "description": "문자열에서 모음(a, e, i, o, u)의 개수를 세어 출력하세요.",
        "input_example": "education",
        "expected_output": "5"
    }
}

converted = []

for i, (title, data) in enumerate(original_problems.items(), start=1):
    converted.append({
        "id": i,
        "title": title,
        "description": data["description"],
        "input_example": data["input_example"],
        "output_example": data["expected_output"],
        "expected_output": data["expected_output"]
    })

# JSON 파일로 저장
with open("problems.json", "w", encoding="utf-8") as f:
    json.dump(converted, f, indent=2, ensure_ascii=False)

print("✅ problems.json 파일 생성 완료!")
