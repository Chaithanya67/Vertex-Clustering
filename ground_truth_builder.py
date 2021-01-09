import sys
import os

def build_ground_truth(path: str) -> [str, int]:
	ground_truth = []
	path = os.path.join(path)
	files = sorted(os.listdir(path))
	assert len(files) > 0, "empty directory" 
	first_file = files[0]
	old_cluster_name = first_file[:first_file.rfind("_")]
	current_cluster = 0
	for filename in files:
		current_cluster_name = filename[:filename.rfind("_")]
		if old_cluster_name != current_cluster_name:
			current_cluster += 1
			old_cluster_name = current_cluster_name
		ground_truth.append( (filename[:filename.rfind(".")], current_cluster) ) 

	return ground_truth


def to_file(ground_truth: [str, int]):
	file = open("ground_truth.csv", "w")
	for id_item, id_cluster in ground_truth:
		file.write(id_item + ", " + str(id_cluster) + "\n")
	file.close()
	return

ground_truth = build_ground_truth(sys.argv[1])
to_file(ground_truth)