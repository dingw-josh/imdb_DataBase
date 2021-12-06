#import createUser
import os
# from multiprocessing import Pool
# global count
#
# ids = [1,2,3,4,5,6,7,8]
# def runUsers(id):
#     os.system("python3 createUser.py " +str(id))
#
# def pool_func():
#     p = Pool(8)
#     p.map(runUsers,ids)
#
# if __name__ == '__main__':
#     pool_func()
from random import randrange
import subprocess
from connection import getConnection, commit, queryUpdate, queryUpdate2

query = "select userid from users order by random() limit 100;"
results = queryUpdate2(query)
# for record in results:
#     for i in range(1,10):
#         if record == results[i][0]:
#             print("YES")

for lp in range(100):
    subprocess.call(['python3', 'createUser.py' , str(results[lp][0])])

os.system('python3 IntegrityCheck.py')
os.system('python3 analysis.py')
