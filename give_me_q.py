
def q_generator():
    with open('files/names.csv') as file:
        names = (file.readlines())
    
    for name in range(len(names)):
        names[name] = names[name].replace('\n','')
    return(names)