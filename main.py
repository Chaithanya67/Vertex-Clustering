from core.utils import load_webpage
from core.ShingleExtractor import extract_shingle_set
from core.ShingleVectorFactory import create_shingle_vector

webpage = load_webpage("movieDB_cluster_pulito/discuss_1.html")
shingle_set = extract_shingle_set(webpage, 8)
shingle_vector = create_shingle_vector(shingle_set)
print(shingle_vector.getContent())
print(shingle_vector.getShingle().getWebpage().getName())