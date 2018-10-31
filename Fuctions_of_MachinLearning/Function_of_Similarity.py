#유사도

#1. N-gram
# s에 전달된 문자열 길이가 10이고, num이 2라면,
# res 리스트의 길이(요소의 갯수)는 얼마? 9=10-2+1

#ngram:각 문자열을 길이가 n인 문자열로 나누는 작업
def ngram(s,num):
    res=[]
    slen=len(s)-num+1 #slen?리스트 요소의 갯수
    for i in range(slen): #i는 0부터 slen-1까지
        ss=s[i:i+num]
    #s="가나다라마바사아자차"
    #    0123456789
        res.append(ss)
    # print(res)
#리턴 : ['오늘','늘','상',...]
    return res

#위 res는 diff_ngram으로 리턴됨
#diff_ngram:두 문자열간 "유사도"조사
def diff_ngram(sa,sb,num):
    a = ngram(sa,num)
    b = ngram(sb,num)
    cnt=0
    r=[]
    for i in a:
        for j in b:
            if i==j:
                cnt+=1
                r.append(i)
    return cnt / len(a), r

a="오늘 상공회의소에서 문자 비교 알고리즘을 배웠다"
b="문자간 비교하는 알고리즘을 상공회의소에서 오늘 배웠다"
#2-gram
res, word=diff_ngram(a,b,2)
print("2-gram",res, word)

#3-gram
res, word=diff_ngram(a,b,3)
print("3-gram",res, word)

