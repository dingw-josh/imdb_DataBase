from connection import getConnection, commit, queryUpdate, queryUpdate2

def bestMovie():
    query = "select distinct movieid from surveys;"
    movieids = queryUpdate2(query)
    if not movieids:
        raise TypeError
    print(len(results))
    totalScores = []
    for record in movieids:
        query = "select * from surveys where moiveid = " + str(record[0]);
        surveyids = queryUpdate2(query)
        if not surveyids:
            raise TypeError
        for record2 in surveyids:
            query = "select * from survey_vote where movieid = " + str(record2[0]);
            survey_votes = queryUpdate2(query)
            movieScore = 0
            if not survey_votes:
                raise TypeError
            for record3 in survey_votes:
                query = "select * from votes where voteid = " + str(record3[1])
                votes = queryUpdate2(query)
                if not votes:
                    raise TypeError
                singleScore = int(votes[2]) + int(votes[3]) + int(votes[4])
                query = "select usertype from users where userid = " + votes[1]
                users = queryUpdate2(query)
                if not users:
                    raise TypeError
                if users[0][0] == "Hired" :
                    singleScore = singleScore * 5
                elif users[0][0] == "User":
                    singleScore = singleScore * 3
                movieScore = movieScore + singleScore
            totalScores.append((movieScore,record2[0]))

bestMovie()
