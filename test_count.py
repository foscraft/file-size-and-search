import my_cl_dsse

if __name__ == "__main__":

    client = my_cl_dsse.My_cl_dsse()
    
    print(f"Dataset has {client.get_count('data')} files")
    