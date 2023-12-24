import PyQt5.QtWidgets import QApplscation, QWidget, QlineEdit,\
        QHBoxLayout, QVBoxLayout, QPushButton, QLabel

menu_win= QWidget()

lb_quest = QLabel('Введіть запитання:')
lb_right_ans = QLabel('Введіть вірну відповідь:')
lb_wrong_ans1 = QLabel('Введіть першу хибну відповідь')
lb_wrong_ans2 = QLabel('Введіть другу хибну відповідь')
lb_wrong_ans3 = QLabel('Введіть третю хибну відповідь')

lb_question = QlineEdit()
lb_right_ans = QlineEdit()
lb_wrong_ans1 = QlineEdit()
lb_wrong_ans2 = QlineEdit()
lb_wrong_ans3 = QlineEdit()

lb_header_stat = QLabel("Статистика:")
lb_header_stat.setStyleSheet('font-size: 19px; font-weight; bold;')

lb_statistic = QLabel()

vl_Labels = QVBoxLayout()
vl_Labels.addWidgets(lb_quest)
vl_Labels.addWidgets(lb_right_ans)
vl_Labels.addWidgets(lb_wrong_ans1)
vl_Labels.addWidgets(lb_wrong_ans2)
vl_Labels.addWidgets(lb_wrong_ans3)

vl_LineEdits = QVBoxLayout()
vl_LineEdits.addWidgets(lb_quest)
vl_LineEdits.addWidgets(lb_right_ans)
vl_LineEdits.addWidgets(lb_wrong_ans1)
vl_LineEdits.addWidgets(lb_wrong_ans2)
vl_LineEdits.addWidgets(lb_wrong_ans3)

h1_question = QHBoxLayout()
h1_question.addLayout(vl_Labels)
h1_question.addLayout(vl_LineEdits)
