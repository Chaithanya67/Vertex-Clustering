import argparse
import csv

def parse_arguments():
    parser = argparse.ArgumentParser(description="""Evaluate clustering results. This scripts will return the 
                                                    precision, recall and F1-score of the provided clustering result""")

    parser.add_argument("--clustered", 
                        required=True, 
                        type=str,
                        help="path to the .csv file with the clustering result")

    parser.add_argument("--goldstandard", 
                        required=True,
                        type=str,
                        help="path to the .csv file with the gold standard")

    args = vars(parser.parse_args())
    '''
    Here, clustering_result.csv and gold_standard.csv 
    should be in the format object_id,cluster_id. 
    '''

    # Get paths to clustering result and gold standard
    return args["clustered"], args["goldstandard"]

def precision_recall(prediction, ground_truth):
    clustered_file = prediction
    gold_standard_file = ground_truth
    #print("\nStarting evaluate.py...")
    #print("Clustering results file:", clustered_file)
    #print("gold standard file:", gold_standard_file)

    # Get the number of clusters from the gold standard
    #---------------------------------------------------------
    gold_standard_n_clusters = 0

    all_gold_standard_clusters_list = []

    with open(gold_standard_file) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            all_gold_standard_clusters_list.append(row[1])
            
    gold_standard_clusters_list = list(set(all_gold_standard_clusters_list))
    gold_standard_n_clusters = len(gold_standard_clusters_list)

    #print("\nNumber of clusters available in the gold standard: ", gold_standard_n_clusters)


    # Get the gold standard
    #----------------------------
    gold_standard_clusters = [[] for x in range(gold_standard_n_clusters)]

    gold_standard_count = 0

    with open(gold_standard_file) as contig_clusters:
        readCSV = csv.reader(contig_clusters, delimiter=',')
        for row in readCSV:
            gold_standard_count += 1
            contig = row[0]
            bin_num = gold_standard_clusters_list.index(row[1])
            gold_standard_clusters[bin_num].append(contig)

    #print("Number of objects available in the gold standard: ", gold_standard_count)

    # Get the number of clusters from the initial clustering result
    #---------------------------------------------------------
    n_clusters = 0

    all_clusters_list = []

    with open(clustered_file) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            all_clusters_list.append(row[1])
            
    clusters_list = list(set(all_clusters_list))
    n_clusters = len(clusters_list)

    #print("Number of clusters available in the clustering result: ", n_clusters)


    # Get initial clustering result
    #----------------------------
    clusters = [[] for x in range(n_clusters)]

    clustered_count = 0
    clustered_objects = []

    with open(clustered_file) as contig_clusters:
        readCSV = csv.reader(contig_clusters, delimiter=',')
        for row in readCSV:
            clustered_count += 1
            contig = row[0]
            bin_num = clusters_list.index(row[1])
            clusters[bin_num].append(contig)
            clustered_objects.append(contig)

    #print("Number of objects available in the clustering result: ", len(clustered_objects))

    # Functions to determine precision, recall, F1-score and ARI
    #------------------------------------------------------------

    eps = 1e-3
    # Get precicion
    def getPrecision(mat, k, s, total):
        sum_k = 0
        for i in range(k):
            max_s = 0
            for j in range(s):
                if mat[i][j] > max_s:
                    max_s = mat[i][j]
            sum_k += max_s
        return sum_k/(total+eps)*100

    # Get recall
    def getRecall(mat, k, s, total, unclassified):
        sum_s = 0
        for i in range(s):
            max_k = 0
            for j in range(k):
                if mat[j][i] > max_k:
                    max_k = mat[j][i]
            sum_s += max_k
        return sum_s/(total+unclassified+eps)*100


    # Get F1-score
    def getF1(prec, recall):
        return 2*prec*recall/(prec+recall+eps)


    # Determine precision, recall, F1-score and ARI for clustering result
    #------------------------------------------------------------------

    total_clustered = 0

    clusters_species = [[0 for x in range(gold_standard_n_clusters)] for y in range(n_clusters)]

    for i in range(n_clusters):
        for j in range(gold_standard_n_clusters):
            n = 0
            for k in range(clustered_count):
                if clustered_objects[k] in clusters[i] and clustered_objects[k] in gold_standard_clusters[j]:
                    n+=1
                    total_clustered += 1
            clusters_species[i][j] = n

    #print("Number of objects available in the clustering result that are present in the gold standard:", total_clustered)

    my_precision = getPrecision(clusters_species, n_clusters, gold_standard_n_clusters, total_clustered)
    my_recall = getRecall(clusters_species, n_clusters, gold_standard_n_clusters, total_clustered, (gold_standard_count-total_clustered))
    my_f1 = getF1(my_precision, my_recall)

    '''
    print("\nEvaluation Results:")
    print("Precision =", my_precision)
    print("Recall =", my_recall)
    print("F1-score =", my_f1)

    print()
    '''
    return my_precision, my_recall, my_f1
'''
prediction, ground_truth = parse_arguments()
precision_recall(prediction, ground_truth)
'''