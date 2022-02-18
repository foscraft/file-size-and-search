import my_cl_dsse

if __name__ == "__main__":

    client = my_cl_dsse.My_cl_dsse()

    print(f"Number of unique words : {client.unique_words('data/300.txt')}")