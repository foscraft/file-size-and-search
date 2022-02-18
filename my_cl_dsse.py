import os
import random
import json
'''
    Implementation of DSSE
'''
class My_cl_dsse:

    #creating a salt and a key/secretkey
    #Everytime the script is run, a new salt secret key is generated and copied to the key.json file
    def keygen(self):
        ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        chars = [random.choice(ALPHABET) for _ in range(35)]
        sk = "".join(chars)
    #the key is saved in a key.json file.
        with open('key.json', 'w') as f:
            json.dump(sk, f)
        return sk
     
#This fuction returns the total size of the dataset
    def size(self,path,*args,**kwargs): 
        #initialize the size
        total_size = 0
        #use the walk() method to navigate through directory tree
        for dirpath, dirnames, filenames in os.walk(path):
            for i in filenames:
                #use join to concatenate all the components of path
                f = os.path.join(dirpath, i)
                #use getsize to generate size in bytes and add it to the total size
                total_size += os.path.getsize(f)
        return total_size

#This code counts the number of files in the dataset
    def get_count(self,path,*args,**kwargs):
        count = 0
        for dirpath, dirnames, filenames in os.walk(path):
            for _ in filenames:
                count += 1
        return count

#from sys import path
#Counts the number in a data file.
    def unique_words(self,path):
        text_file = open(path, 'r')
        text = text_file.read()
        #cleaning
        text = text.lower()
        words = text.split()
        words = [word.strip('.,!;()[]') for word in words]
        words = [word.replace("'s", '') for word in words]
        #finding unique
        unique = []
        for word in words:
            if word not in unique:
                unique.append(word)
        #sort
        unique.sort()
        return len(unique)


#  def get_size(self,path, *args, **kwargs):
#         total_size = 0
#         for dirpath, dirnames, filenames in os.walk(path):
#             for f in filenames:
#                 fp = os.path.join(dirpath, f)
#             # skip if it is symbolic link
#                 if not os.path.islink(fp):
#                     total_size += os.path.getsize(fp)

#         return total_size
