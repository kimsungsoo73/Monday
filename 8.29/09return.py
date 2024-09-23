# 09return.py

# 함수의 리턴값을 1개 이상 처리
# 함수의 매개인자 1개 이상 처리 (*)를 이용

score= {'kim':[100,60], 
        'lee':[90,77], 
        'goo':[82,34] }

def score_procedure(sd):
    kor_list = []
    eng_list = []
    for data in sd.values():
        kor_list.append(data[0])
        eng_list.append(data[1])
    
    kor_hap = sum(kor_list)
    eng_hap = sum(eng_list)
    kor_avg = kor_hap/len(kor_list)
    eng_avg = eng_hap/len(eng_list)
    return kor_hap, eng_hap, kor_avg, eng_avg
        
a,b,c,d = score_procedure(score)
print(a,b,c,d)

# print(score_procedure())
# return 국합, 영합, 국평균, 영평균
