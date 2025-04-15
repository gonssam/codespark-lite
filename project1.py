import streamlit as st
import re
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family'] = 'Malgun Gothic'

# ---------------------- 문제 데이터 ----------------------
problems = {
    "최댓값 찾기": "리스트 [1, 10, 25, 33, 7] 안에서 가장 큰 값을 찾아 출력하세요.",
    "최솟값 찾기": "리스트 [1, 10, 25, 33, 7] 안에서 가장 작은 값을 찾아 출력하세요.",
    "평균값 구하기": "리스트 [4, 8, 15, 16, 23, 42]의 평균을 계산하여 출력하세요.",
    "리스트 정렬": "리스트 [5, 1, 4, 2, 8]를 오름차순으로 정렬하여 출력하세요.",
    "중복 제거": "리스트 [1, 2, 2, 3, 4, 4, 5]에서 중복된 값을 제거한 리스트를 출력하세요.",
    "소수 판별": "사용자가 입력한 숫자가 소수인지 판별하여 출력하세요.",
    "팩토리얼 계산": "사용자가 입력한 숫자의 팩토리얼 값을 계산하여 출력하세요.",
    "피보나치 수열": "사용자가 입력한 수까지의 피보나치 수열을 출력하세요.",
    "문자열 뒤집기": "사용자가 입력한 문자열을 거꾸로 뒤집어 출력하세요.",
    "모음 개수 세기": "문자열에서 모음(a, e, i, o, u)의 개수를 세어 출력하세요."
}

# ---------------------- 피드백 및 점수 평가 ----------------------
def rule_based_feedback(code_text):
    feedback = []
    score = 0
    no_space_code = code_text.replace(" ", "").lower()
    lines = code_text.lower().split("\n")

    if "max(" in no_space_code:
        feedback.append("✅ `max()` 내장 함수를 활용한 효율적인 풀이입니다!")
        score += 20
    if "min(" in no_space_code:
        feedback.append("✅ `min()` 내장 함수를 활용해 최솟값을 잘 찾았어요.")
        score += 20
    if "sum(" in no_space_code and "/" in no_space_code:
        feedback.append("📊 `sum()`과 나눗셈을 이용한 평균 계산이 잘 되었어요!")
        score += 20
    if "sorted(" in no_space_code or ".sort(" in no_space_code:
        feedback.append("📚 리스트를 정렬한 후 값을 찾는 전형적인 정렬 방식입니다.")
        score += 15
    if "set(" in no_space_code:
        feedback.append("🔁 `set()`을 활용해 중복 제거를 잘 했어요.")
        score += 20
    if "input(" in no_space_code:
        feedback.append("💡 사용자 입력을 처리하는 인터랙티브한 코드입니다.")
        score += 10
    if "[" in code_text and "for" in code_text and "in" in code_text and "]" in code_text:
        if re.search(r"\[.*for.*in.*\]", code_text):
            feedback.append("🧠 리스트 컴프리헨션을 사용하여 간결하게 해결했어요!")
            score += 20
    if ("for" in code_text or "while" in code_text) and ("if" in code_text or "elif" in code_text):
        if ">" in code_text or "<" in code_text:
            feedback.append("🔍 반복문과 조건문을 활용해 값을 직접 비교한 점이 좋습니다.")
            score += 15
    if ":" in code_text and "[" in code_text and "]" in code_text:
        if "-1" in code_text or "::-1" in code_text:
            feedback.append("🪞 슬라이싱을 이용한 문자열/리스트 뒤집기가 인상적입니다!")
            score += 10
    function_names = re.findall(r"def\s+([a-zA-Z_]\w*)\s*\(", code_text)
    for fname in function_names:
        if f"{fname}(" in code_text.replace(" ", "")[code_text.find(f"def {fname}") + 1:]:
            feedback.append("🔄 재귀 함수를 사용한 독창적인 접근이에요!")
            score += 25
    if "def" in code_text and "return" in code_text:
        feedback.append("📦 함수 구조를 통해 문제를 모듈화한 점이 좋습니다!")
        score += 10
    if len(code_text.strip()) < 10:
        feedback.append("⚠️ 코드가 너무 짧습니다. 작동 가능한 코드인지 확인해보세요.")
        score = 0
    if not feedback:
        feedback.append("🤔 풀이 방식이 감지되지 않아요. 다른 접근도 시도해보세요!")
        score = 0

    return "\n".join(set(feedback)), min(score, 100)

# ---------------------- 세션 초기화 ----------------------
if "page" not in st.session_state:
    st.session_state.page = "info"
if "records" not in st.session_state:
    st.session_state.records = {}
if "submissions" not in st.session_state:
    st.session_state.submissions = []

# ---------------------- 학생 정보 입력 ----------------------
if st.session_state.page == "info":
    st.title("📌 CodeSpark Lite - 학생 정보 입력")
    student_id = st.text_input("학번을 입력하세요:")
    student_name = st.text_input("이름을 입력하세요:")
    if st.button("입장하기") and student_id and student_name:
        st.session_state.student_id = student_id
        st.session_state.student_name = student_name
        st.session_state.page = "list"
        st.rerun()

# ---------------------- 문제 목록 선택 ----------------------
elif st.session_state.page == "list":
    st.title(f"👋 {st.session_state.student_name}님, 문제를 선택하세요")
    selected = st.selectbox("문제 선택:", list(problems.keys()))
    if st.button("문제 풀기"):
        st.session_state.selected_problem = selected
        st.session_state.page = "problem"
        st.rerun()

    # 교사용 페이지 비밀번호 확인
    teacher_pw = st.text_input("교사용 페이지 비밀번호 입력:", type="password")
    if st.button("📊 교사용 페이지 보기"):
        if teacher_pw == "0429":
            st.session_state.page = "teacher"
            st.rerun()
        else:
            st.warning("비밀번호가 틀렸습니다.")

# ---------------------- 문제 풀이 화면 ----------------------
elif st.session_state.page == "problem":
    st.title(f"🧠 문제: {st.session_state.selected_problem}")
    st.markdown(f"### {problems[st.session_state.selected_problem]}")
    code = st.text_area("💻 코드 입력:", height=300)

    if st.button("제출하기"):
        feedback, score = rule_based_feedback(code)
        record = {
            "학번": st.session_state.student_id,
            "이름": st.session_state.student_name,
            "문제": st.session_state.selected_problem,
            "점수": score,
            "코드": code
        }
        st.session_state.submissions.append(record)
        key = (st.session_state.student_id, st.session_state.selected_problem)
        st.session_state.records[key] = {"score": score, "code": code, "feedback": feedback}
        st.session_state.page = "result"
        st.rerun()

    if st.button("← 목록으로 돌아가기"):
        st.session_state.page = "list"
        st.rerun()

# ---------------------- 제출 결과 ----------------------
elif st.session_state.page == "result":
    key = (st.session_state.student_id, st.session_state.selected_problem)
    st.title("📊 제출 결과")
    st.markdown(f"**문제:** {st.session_state.selected_problem}")
    st.markdown(f"**점수:** {st.session_state.records[key]['score']}점")
    st.markdown("**피드백:**")
    st.info(st.session_state.records[key]['feedback'])
    st.markdown("---")
    st.markdown("### 📂 내가 푼 문제 기록")
    for (sid, prob), data in st.session_state.records.items():
        if sid == st.session_state.student_id:
            st.markdown(f"- `{prob}`: {data['score']}점")
    if st.button("← 목록으로 돌아가기"):
        st.session_state.page = "list"
        st.rerun()

# ---------------------- 교사용 요약 보기 ----------------------
elif st.session_state.page == "teacher":
    st.title("🧑‍🏫 교사용 제출 요약")
    df = pd.DataFrame(st.session_state.submissions)
    if not df.empty:
        summary = df.groupby(["학번", "이름"]).agg({"문제": "count", "점수": "mean"}).reset_index()
        summary.columns = ["학번", "이름", "풀이 수", "평균 점수"]
        summary = summary.sort_values("학번")
        selected_id = st.selectbox("학생 선택:", summary["학번"])
        st.dataframe(summary)

        # 점수 분포 시각화
        st.markdown("### 📈 전체 점수 분포")
        fig, ax = plt.subplots()
        ax.hist(df["점수"], bins=10, color="skyblue", edgecolor="black")
        ax.set_xlabel("점수", fontsize=12)
        ax.set_ylabel("학생 수", fontsize=12)
        ax.set_title("학생 점수 분포", fontsize=14)
        st.pyplot(fig)

        # 상세 보기
        st.markdown("---")
        st.markdown(f"### 🔍 학번 {selected_id} 제출 상세")
        detail = df[df["학번"] == selected_id][["문제", "점수", "코드"]]
        st.dataframe(detail)
    else:
        st.warning("아직 제출된 내용이 없습니다.")
    if st.button("← 학생 화면으로 돌아가기"):
        st.session_state.page = "list"
        st.rerun()
