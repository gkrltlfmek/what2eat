<h3><a href="https://chatbot.kakao.com/docs/key-concepts-entity#%EC%8B%9C%EC%8A%A4%ED%85%9C-%EC%97%94%ED%8B%B0%ED%8B%B0"> 카카오톡 챗봇 가이드 요약</h3></a>

<b><h4> 엔티티(Entity) </h4></b>
엔티티는 한 마디로 말하면 <b>키워드 사전</b>이다. 
사용자에게 입력받은 발화를 봇이 대응하기 위해서 먼저 입력해야할 일종의 단어(데이터) 사전이라 생각하면 편할 것 같다.
엔티티의 구조는 커다란 </b>하나의 엔트리</b>에서 <b>대표엔트리</b>로 나뉘고 그 대표엔트리엔 파생되는 <b>동의어</b>들이 저장된다. 
엔티티 설정메뉴에서 작업할 수 있다.

<b><h4> 엔티티의 구조 </h4></b>
<a href="https://chatbot.kakao.com/docs/key-concepts-entity#%EC%97%94%ED%8B%B0%ED%8B%B0%EC%9D%98-%EC%A2%85%EB%A5%98"><img src="https://chatbot.kakao.com/docs/assets/key-concepts/entity-structure.png" border="0"></a>

<a href="https://chatbot.kakao.com/docs/key-concepts-entity#%EC%97%94%ED%8B%B0%ED%8B%B0%EC%9D%98-%EC%A2%85%EB%A5%98"><img src="https://chatbot.kakao.com/docs/assets/key-concepts/entity-mine2.png" border="0"></a>

위 화면에 보이는 나의 엔티티 화면을 통해 제일 상위에 엔티티 명 cafe_name, 
대표엔티티인 엥헬리너스 삼디야 등, 그 옆에는 동의어인 바셋, 알레이리야 등을 확인할 수 있었다.
같은 방식으로 필요한 엔티티를 추가하면 될 것 같다.
추가로 csv파일로 대량의 엔트리를 한번에 등록할 수 있다고 한다. (구성에 변경이 없을 시, 재업로드로 반복적인 덮어쓰기 가능)
- 이때 csv파일은 utf-8 인코딩 모드로 맞춰줘야함 (한글 인코딩 문제로 추측한다.)


<b><h4> 시스템 엔티티 </b></h4>
<a href="https://chatbot.kakao.com/docs/key-concepts-entity#%EC%97%94%ED%8B%B0%ED%8B%B0%EC%9D%98-%EC%A2%85%EB%A5%98"><img src="https://chatbot.kakao.com/docs/assets/key-concepts/05@2x.png" border="0"></a>

시스템 엔티티는 관리자센터에서 <b>미리 정의해둔 엔티티</b>이다. 
주로 엔티티명이 @sys.라는 단어로 시작하고, 일반적으로 통용되는 날짜나 시간 지명 같은 개념에 대해 제공한다. 
미리 정의해둔 내용을 사이트에 정리해 놓았기에 사진을 눌러 직접 확인해보는 것이 좋다.
