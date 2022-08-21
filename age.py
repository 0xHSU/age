driving = input('請問你有沒開過車?')
if driving != '有' and driving != '沒有' :
    print('只能輸入有/沒有')
    raise SystemExit
age = input('請問你的年齡?')
age = int(age)
if driving == '有' :
    if age >= 18 :
        print('你通過了')
    else  :
        print('逼逼 已違法')
elif driving == '沒有' :
    if age >= 18 :
        print('菜雞一枚')
    else :
        print ('乖狗狗')
               

    

