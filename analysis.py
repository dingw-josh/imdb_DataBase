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

    totalScores.sort(key=lambda y: y[0])
    #print(totalScores[len(totalScores) - 1])
    #
    query = "select * from movies where id = " + str(totalScores[0][1])
    result = queryUpdate2(query)
    print("The movie \"" + str(result[0][1]) + "\" in year " + str(result[0][2]) + " has the best score " + str(totalScores[0][0]))



def movie_with_most_review():
    movie_record = []
    query = "select distinct movieid from reviews;"

    movieids = queryUpdate2(query)
    if not movieids:
        raise TypeError
    for record in movieids:
        query = "select count(*) from reviews where movieid = " + str(record[0])
        value = queryUpdate2(query)[0]
        movie_record.append((record[0], value[0]))
    max = movie_record[0]
    for record in movie_record :
        if record[1] > max[1]:
            max = record
    query = "select * from movies where id = " + str(max[0])
    result = queryUpdate2(query)
    print("The Movie \""+ result[0][1] + "\" in year " + str(result[0][2]) + " has the highest number of reviews.")

bestMovie()
movie_with_most_review()

def popularMovie():

    surveyRecord =[]
    query = "select distinct movieid from surveys;"
    movieids = queryUpdate2(query)
    if not movieids:
        raise TypeError
    for record in movieids:
        query = "select count(*) from surveys where movieid = " + str(record[0])
        value = queryUpdate2(query)[0]
        surveyRecord.append((record[0],value[0]))
    # print(surveyRecord)
    max = surveyRecord[0]
    for record in surveyRecord:
        if record[1] > max[1]:
            max = record
    query = "select * from movies where id = " + str(max[0])
    result = queryUpdate2(query)
    print("Movie \"" + result[0][1] + "\" surveyed most")

popularMovie()


