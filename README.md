# django--
## 개발 목표
실무에서 사용할 웹 사이트를 만들며 부족한 부분을 확인하고 채우기 위해 진행한다.

## 요구 사항 
1. 개인이 오늘 할 일을 정리해서 보여준다.
2. 개인이 주간 할 일을 정리해서 보여준다.
3. 개인이 월간 할 일을 정리해서 보여준다.
4. 모든 사람은 할 일을 추가/수정/삭제할 수 있어야 한다. (관리자가 보낸 일은 수정할 수 없도록 한다.)
5. 관리자는 개인에게 할 일을 보낼 수 있어야 한다.
6. 관리자가 다수에게 일을 한 번에 보낼 수 있어야 한다.
7. 관리자는 자신이 보낸 일의 흐름을 확인할 수 있어야 한다.
8. 개인은 할 일을 마무리해서 파일 및 내용을 보낼 수 있어야 한다.

## 모델링
#### Accounts
1. 이름
2. ID
3. PW
4. Gmail 주소
5. 실제 사용 메일 주소

#### Todolist
0. 완료 여부 (체크 박스)
1. 카테고리
2. 제목
3. 내용
4. 문서첨부
5. 작성자
6. 담당자들 (미지정 시 본인)
7. 참조

##### 카테고리
1. 번역
2. 리뷰
3. PR
4. LQA
5. 기타

