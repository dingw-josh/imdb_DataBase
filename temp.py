from connection import getConnection, commit, queryUpdate, queryUpdate2

def bestUser():
    userRecord = []
    query = "select distinct userid from comments"
    results = queryUpdate2(query)
    if not results:
        raise TypeError
    for record in results:
        query = "select count(*) from comments where userid = " + str(record[0])
        value = queryUpdate2(query)[0]
        userRecord.append((record[0], value[0]))
    print(userRecord)
    max = userRecord[0]
    for record in userRecord:
        if record[1] > max[1]:
            max = record
    query = "select * from users where userid = " + str(max[0])
    result = queryUpdate2(query)
    print("User "+ str(result[0][0])+ " " + result[0][1] + " " + result[0][2] + " commented most")

bestUser()
