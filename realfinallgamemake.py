import tkinter as tk
import winsound

class TitleScreen:
    def __init__(self, master):
        self.master = master
        self.master.title("퀴즈 타이틀 화면")
        self.master.geometry("400x400")

        self.title_label = tk.Label(self.master, text="퀴즈 풀기!", font=("Helvetica", 16))
        self.title_label.pack(pady=50)

        self.start_button = tk.Button(self.master, text="게임 시작", command=self.start_game)
        self.start_button.pack()

    def start_game(self):
        self.master.destroy()  # 타이틀 화면을 닫고
        root = tk.Tk()  # 새로운 윈도우를 열어서 게임을 시작
        quiz_app = QuizGame(root)
        root.mainloop()

class QuizGame:
    def __init__(e, pl):
        e.pl = pl
        e.pl.title("퀴즈")
        e.pl.geometry("400x400")

        e.Q = [
            {"Q": "1. 늑대는 영어로?", 
             "ans": "wolf"},
            {"Q": "2. 8+4*2=?", 
             "ans": "16"},
            {"Q": "3. 오늘의 날짜는?", 
             "ans": "12월11일"},
            {"Q": "4. 왕이 넘어지면?", 
             "ans": "킹콩"},
            {"Q": "5. 아몬드가 죽으면?", 
             "ans": "다이아몬드"},
            {"Q": "6. 204+582=?", 
             "ans": "786"},
            {"Q": "7. 653-340?", 
             "ans": "313"},
            {"Q": "8. 미국의 수도는 뉴욕이다(o,x)?", 
             "ans": "x"},
            {"Q": "9. 세상에서 가장 높은 산은?", 
             "ans": "에베레스트"},
            {"Q": "10. 7*(8-5)=?", 
             "ans": "21"},
            {"Q": "11. 1부터 10까지 모든 수를 더하면?", 
             "ans": "55"},
            {"Q": "12. 일부러 vs 일부로?", 
             "ans": "일부러"},
            {"Q": "13. 금새 vs 금세", 
             "ans": "금세"},
            {"Q": "14. 며칠 vs 몇일", 
             "ans": "며칠"},
            {"Q": "15. 1945년 우리나라가 일본으로부터 해방되었다(o,x)?", 
             "ans": "o"},
            {"Q": "16. 일본의 수도는?", 
             "ans": "도쿄"},
            {"Q": "17. 고양이는 영어로?", 
             "ans": "cat"},
            {"Q": "18. 영국은 섬나라다(o,x)?", 
             "ans": "o"},
            {"Q": "19. 사흘은 4일을 뜻한다(o,x)?", 
             "ans": "x"},
            {"Q": "20. 11*11?", 
             "ans": "121"},
            {"Q": "21. apple의 뜻은?", 
             "ans": "사과"},
            {"Q": "22. 중국의 수도는?", 
             "ans": "베이징"},
            {"Q": "23. 반성문을 영어로 하면?", 
             "ans": "글로벌"},
            {"Q": "24. 이탈리아 수도는?", 
             "ans": "로마"},
            {"Q": "25. 훈민정음을 창제한 사람은?", 
             "ans": "세종대왕"},
            {"Q": "26. 왠지 vs 웬지?", 
             "ans": "왠지"},
            {"Q": "27. 웬일이야 vs 왠일이야?", 
             "ans": "웬일이야"},
            {"Q": "28. 프랑스의 수도는 파리이다(o,x)?", 
             "ans": "o"},
            {"Q": "29. 오랜만 vs 오랫만?", 
             "ans": "오랜만"},
            {"Q": "30. 동의보감을 편찬한 사람은?", 
             "ans": "허준"},
            {"Q": "31. 820/5?", 
             "ans": "164"},
            {"Q": "32. 6*2/3?", 
             "ans": "4"},
            {"Q": "33. 쥐가 네 마리 모이면?", 
             "ans": "쥐포"},
            {"Q": "34. 역할 vs 역활?", 
             "ans": "역할"},
            {"Q": "35. Tuesday는 목요일이다(o,x)?", 
             "ans": "x"},
            {"Q": "36. tkinter는 CUI에서 사용이 가능하다(o,x)?", 
             "ans": "x"},
            {"Q": "37. 난수는 영어로?", 
             "ans": "random"},
            {"Q": "38. 제목은 영어로?", 
             "ans": "title"},
            {"Q": "39. break는 루프 하나만 빠져나올 수 있다(o,x)?", 
             "ans": "o"},
            {"Q": "40. winsound는 맥에서도 사용이 가능하다(o,x)?", 
             "ans": "x"},
            {"Q": "41. 우겨널다 vs 욱여넣다", 
             "ans": "욱여넣다"},
            {"Q": "42. 78+91=?", 
             "ans": "169"},
            {"Q": "43. 153-12>64*2(o,x)?", 
             "ans": "o"},
            {"Q": "44. 크리스마스는 영어로?", 
             "ans": "christmas"},
            {"Q": "45. 세상에서 가장 쉬운 숫자는(한글로 작성)?", 
             "ans": "십구만"},
            {"Q": "46. 신이 화가나면?", 
             "ans": "신발끈"},
            {"Q": "47. 달은 영어로?", 
             "ans": "moon"},
            {"Q": "48. 해는 영어로?", 
             "ans": "sun"},
            {"Q": "49. 겨울은 영어로?", 
             "ans": "winter"},
            {"Q": "50. 자라보고 놀란 가슴 ㅇㅇㅇ 보고 놀란다", 
             "ans": "솥뚜껑"},
            {"Q": "51. ㅇㅇㅇ도 밟으면 꿈틀한다", 
             "ans": "지렁이"},
            {"Q": "52. ㅇㅇㅇ 날자 배 떨어진다", 
             "ans": "까마귀"},
            {"Q": "53. 제자가 스승보다 나은 것을 비유하는 사자성어는?", 
             "ans": "청출어람"},
            {"Q": "54. 대나무를 타고 놀던 옛 친구라는 뜻의 사장성어는?", 
             "ans": "죽마고우"},
            {"Q": "55. 원수는 ㅇㅇㅇ 다리에서 만난다", 
             "ans": "외나무"},
            {"Q": "56. 조선 초기 중립외교를 추구했던 왕은?", 
             "ans": "광해군"},
            {"Q": "57. 임진왜란 발생연도는 1592년이다(o,x)?", 
             "ans": "o"},
            {"Q": "58. 한국전쟁은 1950년에 일어났다(o,x)?", 
             "ans": "o"},
            {"Q": "59. 어이없다 vs 어의없다?", 
             "ans": "어이없다"},
            {"Q": "60. 됐다 vs 됬다", 
             "ans": "됐다"},
            {"Q": "61. 인구가 가장 많은 나라는?", 
             "ans": "중국"},
            {"Q": "62. 딸기가 회사에서 잘리면?", 
             "ans": "딸기시럽"},
            {"Q": "63. 963/9?", 
             "ans": "107"},
            {"Q": "64. 수도가 모스크바인 나라는?", 
             "ans": "러시아"},
            {"Q": "65. 인도네시아는 인도의 수도다(o,x)?", 
             "ans": "x"},
            {"Q": "66. 비슷한 부류의 인간 모임을 비유하는 사자성어는?", 
             "ans": "유유상종"},
            {"Q": "67. 정답을 맞히다 vs 맞추다?", 
             "ans": "맞히다"},
            {"Q": "68. 파이썬에서 실시간 처리는 after()이 수행한다(o,x)?", 
             "ans": "o"},
            {"Q": "69. 2의 5제곱은?", 
             "ans": "32"},
            {"Q": "70. 실패는 성공의 어머니라는 명언을 남긴 사람은(3글자)?", 
             "ans": "에디슨"},
            {"Q": "71. 사회적으로 인정받고 출세하여 이름을 세상에 알린다는 뜻의 사자성어는?", 
             "ans": "입신양명"},
            {"Q": "72. 9^3>5^4(o,x)?", 
             "ans": "o"},
            {"Q": "73. 6^3+40=2^8(o,x)?", 
             "ans": "o"},
            {"Q": "74. 잠갔다 vs 잠궜다?", 
             "ans": "잠갔다"},
            {"Q": "75. 120/2/4/3=?", 
             "ans": "5"},
            {"Q": "76. 소 잃고 ㅇㅇㅇ 고친다", 
             "ans": "외양간"},
            {"Q": "77. 미리 준비가 되어 있으면 걱정힐 일이 없다는 뜻의 사자성어는?", 
             "ans": "유비무환"}
        ]

        e.current_quiz_index = 0
        e.correct_point=0
        e.incorrect_point=0

        e.Q_label = tk.Label(e.pl, text=e.Q[e.current_quiz_index]["Q"])
        e.Q_label.pack(pady=10)

        e.ans_var = tk.StringVar()
        e.ans_entry = tk.Entry(e.pl, textvariable=e.ans_var)
        e.ans_entry.pack(pady=10)

        e.submit_btn = tk.Button(e.pl, text="제출하기", command=e.b_ans)
        e.submit_btn.pack(pady=10)

    def b_ans(e):
        pl_ans = e.ans_var.get().strip().lower()
        correct_ans = e.Q[e.current_quiz_index]["ans"]

        if pl_ans == correct_ans:
            result_text = "정답입니다."
            winsound.Beep(261,300)#도
            winsound.Beep(329,300)#미
            winsound.Beep(392,300)#솔
            e.correct_point+=1
        else:
            result_text = f"오답입니다. 정답은 {correct_ans}."
            winsound.Beep(493,300)#시
            e.incorrect_point+=1

        result_label = tk.Label(e.pl, text=result_text)
        result_label.pack(pady=10)

        e.current_quiz_index += 1
        if e.current_quiz_index < len(e.Q):
            e.Q_label.config(text=e.Q[e.current_quiz_index]["Q"])
            e.ans_var.set("")   
        else:
            if e.correct_point>=86:
                e.end_quiz1()
            else:
                e.end_quiz2()

    def end_quiz1(e):
        e.Q_label.config(text="정답을 모두 맞혀 문의 잠금이 해제됩니다.")
        e.ans_entry.pack_forget()
        e.submit_btn.pack_forget()
        winsound.Beep(261,350)#도
        winsound.Beep(329,350)#미
        winsound.Beep(392,350)#솔
        winsound.Beep(523,350)#도
    
    def end_quiz2(e):
        e.Q_label.config(text="정답을 모두 맞히지 못하여 들어가실 수 없습니다.")
        e.ans_entry.pack_forget()
        e.submit_btn.pack_forget()
        winsound.Beep(493,350)#시
        winsound.Beep(493,350)#시
        winsound.Beep(493,350)#시
        winsound.Beep(493,350)#시

def main():
    root = tk.Tk()
    title_screen = TitleScreen(root)
    root.mainloop()

if __name__ == "__main__":
    main()