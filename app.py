import streamlit as st
st.set_page_config(page_title='AiconvVer1.0', layout='wide')
st.title('덧셈과 곱셈 머신러닝')
c1, c2 = st.columns((4,1))
with c1 :
    with st.expander('메인 콘텐츠 #1'):
        # st.subheader('덧셈기')
        #letax document(overleaf 사이트 참고)
        plusexp = '''
# 덧셈기는? 

> 덧셈 연산을 수행하는 논리 회로로, 디지털 회로와 조합 회로의 일종입니다. 덧셈기는 산술 논리 장치로 사용되며, 주소값이나 테이블 색인 등을 더하는 프로세서의 일부로도 사용됩니다. 
덧셈기의 종류로는 반가산기와 풀가산기가 있습니다. 
    
    * 반가산기는 한 자리의 2진수 2개를 입력하여 합과 캐리를 계산하는 덧셈 회로입니다. 
    * 풀가산기는 4자릿수의 이진수 2개를 더할 수 있는 칩으로, 74LS83이 대표적인 제품입니다. 

> 덧셈기는 이진화 십진법, 3 초과 부호 등 여러 가지 수학적 연산을 수행할 수 있습니다.         

$$
a+b=c

\sum_{x=1}^n 

$$
        '''
        st.markdown(plusexp)
        st.image('C:/aiconv_2024_winter/static/images/img1.png')
    
    with st.expander('메인 콘텐츠 #2'):
        st.subheader('덧셈에 대한 온라인 학습')
        url1 = 'https://www.youtube.com/watch?v=vmgo1eN0WEo'
        st.video(url1)

    with st.expander('메인 콘텐츠 #3'):
        st.subheader('머신러닝에 의한 덧셈과 뺄셈')
        # 머신러닝 학습모델 불러오기
        import joblib
        from sklearn.metrics import accuracy_score
        from sklearn.model_selection import train_test_split
        from sklearn.svm import SVC
        import pandas as pd

        df = pd.read_csv('C:/aiconv_2024_winter/static/dataset/mydata.csv')
        X = df.iloc[:, :3]
        y = df.iloc[:, 3]
        X_train, X_test, y_test, y_train = train_test_split(X, y, test_size=0.3, shuffle=True)

        myModel = SVC()
        myModel.fit(X_train, y_train)
        y_pred = myModel.predict(X_test)

        savedModel = joblib.load('C:/aiconv_2024_winter/mymodel/model.pkl')
        acc = round(accuracy_score(y_test, y_pred)*100, 2)

        # 3개의 숫자 입력받기
        with st.form('Input value'):
            num1 = st.number_input('First Number:', min_value=1, max_value=100, step=1, key='1stnum')
            num2 = st.number_input('Second Number:', min_value=1, max_value=100, step=1, key='2ndnum')
            num3 = st.number_input('Result Number:', min_value=1, step=1, key='rsnum')

            if st.form_submit_button('+/x 예측하기'):
                rs = savedModel.predict([[num1,num2,num3]])
                st.write(f'{num1}과 {num2}을(를) 연산한 결과 값 {num3}는 {rs}의 결과입니다. (Supported with {acc}%)')
        
        # 학습 모델에 입력해서 예측하기
        # 가상환경에 나가서 설치하려면 ctrl+c 하고 설치하고 화살표 위 2번
        # 덩어리 코드를 던지는게 아니라 스크래칭

        #시각화(혼동행렬) - 정확도 근거
        if st.checkbox('혼동행렬 확인'):
            import seaborn as sns
            import matplotlib.pyplot as plt
            from sklearn.metrics import confusion_matrix
            sns.heatmap(confusion_metrix(y_test, y_pred))
            plt.xticks([0.5,1.5],['+','x'])
            plt.yticks([0.5,1.5],['+','x'])
            st.pyplot(fig)

with c2:
    with st.expander('Tips...'):
        st.subheader('덧셈이란?')
        plusis = '''
        덧셈은 산술의 기본 연산 중의 하나로, 뺄셈과 곱셈, 나눗셈과 함께 대표되는 사칙연산이다. 두 개의 수를 받아서 두 수의 합인 하나의 수를 내는 연산이다. 옆의 그림에서
        ''' #변수에 넣기
        st.info(plusis)