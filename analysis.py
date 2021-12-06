from connection import getConnection, commit, queryUpdate, queryUpdate2

def bestMovie():
    #get all the movieids that are being surveied
    query = "select distinct movieid from surveys;"
    movieids = queryUpdate2(query)
    if not movieids:
        raise TypeError
    #print(len(movieids))
    totalScores = []
    for record in movieids:
        #get all the surveys that are about one movie
        query = "select * from surveys where movieid = " + str(record[0]);
        surveyids = queryUpdate2(query)
        #print( surveyids)
        if not surveyids:
            raise TypeError
        movieScore = 0
        for record2 in surveyids:
            #get all the votes that are related to one survey
            surveyid = record2[0]
            query = "select * from survey_vote where surveyid = " + str(surveyid);
            survey_votes = queryUpdate2(query)[0]
            if not survey_votes:
                raise TypeError
            for record3 in survey_votes:
                query = "select * from votes where voteid = " + str(record3)
                votes = queryUpdate2(query)
                if not votes:
                    raise TypeError
                singleScore = int(votes[0][2]) + int(votes[0][3]) + int(votes[0][4])
                query = "select usertype from users where userid = " + str(votes[0][1])
                users = queryUpdate2(query)
                if not users:
                    raise TypeError
                if users[0][0] == "Hired" :
                    singleScore = singleScore * 5
                elif users[0][0] == "User":
                    singleScore = singleScore * 3
                movieScore = movieScore + singleScore
        totalScores.append((movieScore,record2[2]))
    print(totalScores)

bestMovie()
