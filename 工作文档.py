def check_answers():
    # 获取用户输入
    year_input = input("请输入你要核对的卷次、年份及文章号（如120103）：")

    # 将正确答案定义给correct_answers
    from 历年英一真题答案 import answers
    try:
        correct_answers = answers[int(year_input)]
    except KeyError:
            print(f"错误：没有找到{year_input}年的答案")
            return

    # 获取用户输入
    answers_input = input("请输入你的答案（如ACDBA）：").upper()

    # 将用户输入拆分成单个答案
    user_answers = list(answers_input)



    # 比较答案并统计正确数
    correct_count = 0
    wrong_questions = []

    for i in range(len(correct_answers)):
        if user_answers[i] == correct_answers[i]:
            correct_count += 1
        else:
            wrong_questions.append(i + 1)  # 题号从1开始

    # 输出结果
    print(f"正确数量：{correct_count}/{len(correct_answers)}")


# 运行函数
check_answers()