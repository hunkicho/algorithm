def solution(record):
    answer = []
    ment = {}
    ment["Enter"] = " 들어왔습니다."
    ment["Leave"] = " 나갔습니다."
    user = {}
    
    for i in record:
        message = i.split(" ")
        if message[0] == "Enter" or message[0] == "Change":
            user[message[1]] = message[2]
    
    for j in record:
        message = j.split(" ")
        if message[0] != "Change":
            line = user[message[1]] + "님이" + ment[message[0]]
            answer.append(line)
        
    
    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))