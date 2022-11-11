<h3>시나리오(Scenario)</h3>

시나리오는 <b>사용자에게 응대하는</b> 가장 작은 단위인 블록들을 모아 만든 <b>하나의 서비스</b>로 정의할 수 있다.
what2eat에서 제공할만 한 시나리오는 크게 식당 안내 / 시설 안내로 나눌 수 있을 것 같다.

<h4>기본 시나리오</h4>

기본 시나리오는 모든 봇에 장착되어 있고, 다음 3개의 블록이 항상 포함된다.
1. 웰컴 블록 (Welcome) : 사용자를 <b>처음 만날 때 발송</b>하는 메시지
2. 폴백 블록 (Fall-back) : 사용자의 발화를 <b>이해하지 못한 경우 응대</b>하는 메시지
3. 탈출 블록 (exit) : 봇의 되묻기 상황에서 <b>사용자가 대화를 초기화 또는 탈출</b>하고 싶을 때 쓰는 명령어 집합

<h4>커스텀 시나리오</h4>

<a href="https://chatbot.kakao.com/docs/key-concepts-scenario#%EC%8B%9C%EB%82%98%EB%A6%AC%EC%98%A4-%EC%84%A4%EC%A0%95"><img src="https://chatbot.kakao.com/docs/assets/key-concepts/scenario-adding.png" border="0"></a>

검은 박스로 된 부분이 커스텀 시나리오다. 본 화면에서 시나리오 설정으로 넘어갈 수 있다.
시나리오 설정에는 되묻기 질문을 등록할 수 있다. 
되뭄기 질문이란 사용자로부터 <b><a href=https://chatbot.kakao.com/docs/key-concepts-parameters#%EA%B7%B8%EB%A3%B9-%ED%8C%8C%EB%9D%BC%EB%AF%B8%ED%84%B0>특정 발화(=파라미터)</b></a>를 얻기 위해 최대 8번까지 물어보는 질문이다.

<h4>봇 제네릭 메뉴</h4>
<a href="https://chatbot.kakao.com/docs/key-concepts-scenario#%EC%8B%9C%EB%82%98%EB%A6%AC%EC%98%A4-%EC%84%A4%EC%A0%95"><img src="https://chatbot.kakao.com/docs/key-concepts-scenario#%EB%B4%87-%EC%A0%9C%EB%84%A4%EB%A6%AD-%EB%A9%94%EB%89%B4" border="0"></a>

봇 제네릭 메뉴는 위 화면처럼 구성된 사용자 인터페이스를 의미한다.
