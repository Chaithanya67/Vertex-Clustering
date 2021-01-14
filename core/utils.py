from core.shingleVector import ShingleVector


# Per ora inserisco qui ciò che ancora non mi è chiaro dove mettere


def shingle_cover(shingle_vector_a, shingle_vector_b):
    assert len(shingle_vector_a) == len(shingle_vector_b), "shingle must have same length"
    for i in range(len(shingle_vector_a)):
        # None non mi convince molto per modellare "*"
        with_mask = shingle_vector_b[i] is None or shingle_vector_a[i] is None
        if shingle_vector_a[i] != shingle_vector_b[i] and not with_mask:
            return False
    return True


def find_8_masked_shingle_vectors_sorted(hashtable):
    list_8_masked_shingle_vectors = []
    hashtable = dict(sorted(hashtable.items(), key=lambda item: item[1]))
    masked_shingle_vectors = hashtable.keys()
    for masked_shingle_vector in masked_shingle_vectors:
        to_insert = True
        for value in masked_shingle_vector:
            if (value == None):
                to_insert = False
        if (to_insert):
            list_8_masked_shingle_vectors.append(masked_shingle_vector)
            
    return list_8_masked_shingle_vectors


def maximum_count_covering(hashtable, masked_shingle_vector):
    #Bruttura per inizializzare il massimo al primo shingle_vector che trovo che copre quello masked dato
    max_vector = []
    for vector in hashtable.keys():
        found = False
        if (shingle_cover(masked_shingle_vector, vector)):
            max_vector = vector
            found = True
            break
    if(not found):
        return None
    for vector in hashtable.keys():
        if(shingle_cover(masked_shingle_vector, vector) and hashtable[max_vector] < hashtable[vector]):
            max_vector = vector

    if max_vector == []:
        max_vector = tuple([None] * 8)
    return max_vector

# Crea tutti i masked_shingle_vector 6/8, 7/8, 8/8 di uno shingle_vector
def k_shingle_cover(shingle_vector, k):
    shingle_vector_content = shingle_vector.getContent()
    length = len(shingle_vector_content)
    masked_shingle_vectors = []
    if k < 6:
        print('Minimum k is 6')
    if k == 6:
        # 6/8
        for i in range(length):
            temp = []
            temp.extend(shingle_vector_content)
            temp[i] = None
            for j in range(i + 1, length):
                masked_shingle_vector = []
                masked_shingle_vector.extend(temp)
                masked_shingle_vector[j] = None
                masked_shingle_vectors.append(ShingleVector(shingle_vector.getWebpage(), masked_shingle_vector))
        # 7/8
        for i in range(length):
            masked_shingle_vector = []
            masked_shingle_vector.extend(shingle_vector_content)
            masked_shingle_vector[i] = None
            masked_shingle_vectors.append(ShingleVector(shingle_vector.getWebpage(), masked_shingle_vector))
        # 8/8
        masked_shingle_vectors.append(ShingleVector(shingle_vector.getWebpage(), shingle_vector_content))

    if k == 7:
        # 7/8
        for i in range(length):
            masked_shingle_vector = []
            masked_shingle_vector.extend(shingle_vector_content)
            masked_shingle_vector[i] = None
            masked_shingle_vectors.append(ShingleVector(shingle_vector.getWebpage(), masked_shingle_vector))
        # 8/8
        masked_shingle_vectors.append(ShingleVector(shingle_vector.getWebpage(), shingle_vector_content))
    if k == 8:
        # 8/8
        masked_shingle_vectors.append(ShingleVector(shingle_vector.getWebpage(), shingle_vector_content))
    return masked_shingle_vectors


def shingle_cover_only_6(shingle_vector):
    shingle_vector_content = shingle_vector.getContent()
    length = len(shingle_vector_content)
    masked_shingle_vectors = []
    for i in range(length):
        temp = []
        temp.extend(shingle_vector_content)
        temp[i] = None
        for j in range(i + 1, length):
            masked_shingle_vector = []
            masked_shingle_vector.extend(temp)
            masked_shingle_vector[j] = None
            masked_shingle_vectors.append(ShingleVector(shingle_vector.getWebpage(), shingle_vector_content))
    return masked_shingle_vectors


def shingle_cover_only_7(shingle_vector):
    shingle_vector_content = shingle_vector.getContent()
    length = len(shingle_vector_content)
    masked_shingle_vectors = []
    for i in range(length):
        masked_shingle_vector = []
        masked_shingle_vector.extend(shingle_vector_content)
        masked_shingle_vector[i] = None
        masked_shingle_vectors.append(ShingleVector(shingle_vector.getWebpage(), shingle_vector_content))
    return masked_shingle_vectors


class Logger:
    __instance = None
    __verbosity = 0

    @staticmethod 
    def get_instance():
        if Logger.__instance == None:
            Logger(0)
        return Logger.__instance

    def __init__(self, verbosity):
        if Logger.__instance != None:
            raise Exception("Logger is a singleton class")
        else:
            Logger.__instance = self
            Logger.__verbosity = verbosity

    # default verbosity is low level priority
    def print(self, message, verbosity = 3):
        if verbosity <= Logger.__verbosity:
            print(message)

    def set_verbosity(self, verbosity):
        Logger.__verbosity = verbosity