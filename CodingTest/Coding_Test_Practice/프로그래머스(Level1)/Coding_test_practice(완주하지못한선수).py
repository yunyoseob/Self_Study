#문제 설명
#수많은 마라톤 선수들이 마라톤에 참여하였습니다. 
# 단 한 명의 선수를 제외하고는 모든 선수가 마라톤을 완주하였습니다.
#마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 
# 완주한 선수들의 이름이 담긴 배열 completion이 주어질 때, 
# 완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성해주세요.

# 제한사항
# 마라톤 경기에 참여한 선수의 수는 1명 이상 100,000명 이하입니다.
# completion의 길이는 participant의 길이보다 1 작습니다.
# 참가자의 이름은 1개 이상 20개 이하의 알파벳 소

# 정답은 맞지만, 효율성이 떨어짐.
def soulution(participant, completion):
    answer=''
    for i in participant:
        if i in completion:
            completion.remove(i) 
        else:
            answer=''.join(i)
    return answer

participant=["marina", "josipa", "nikola", "vinko", "filipa"]
completion=["josipa", "filipa", "marina", "nikola"]


# 두 번째 풀이 방식 또한 정답은 맞으나, 시간초과
def solution(participant, completion):
    answer=''
    if len(set(participant))==len(participant):
        li=list(set(participant).difference(set(completion)))[0]        
        answer=''.join(li)
    else:
        for i in participant:
            if i in completion:
                completion.remove(i) 
            else:
                answer=''.join(i)
    return answer
            
        
soulution(participant, completion)    
        
# 세 번재 풀이방법 역시, 정확도 100%, 속도가 느림.
def solution(participant, completion):
    answer=''
    if 1<=len(participant)<=100000:
        for i in completion:
            if 1<=len(i)<=20:
                participant.remove(i)
                answer=''.join(participant[0])
    return answer
    

# 네 번째 풀이방법
def solution(participant, completion):
    participant.sort()
    completion.sort()
    for p,c in zip(participant, completion):
        if p!=c:
            return p
    return participant.pop()





























































































