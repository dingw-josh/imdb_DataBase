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

subprocess.call(['python3', 'createUser.py', str(1)])
