from rdflib import Graph, Literal, Namespace, RDF, URIRef
from rdflib.namespace import XSD

syspath = '/home/wyf/autoAlign/AutoAlign'
inputdatapath = syspath+'/data/DY-NB-current'
outputdatapath = syspath+'/data/DY-NB-current-up'
# 创建一个新的RDF图
g = Graph()

# 读取原始数据集
input_file = inputdatapath+"/dbp_yagot.ttl"
g.parse(input_file, format="turtle")

# 创建一个新的数据集用于存储属性三元组
output_file = outputdatapath+"/dbp_yago_up0.ttl"

# 定义用于筛选属性三元组的谓词集合
intersection_predicates = ['http://www.w3.org/2000/01/rdf-schema#label','http://dbpedia.org/ontology/birthDate']

# 迭代原始数据集中的三元组
for subject, predicate, obj in g:
    # 检查是否谓词在intersection_predicates中
    if predicate in intersection_predicates:
        # 将三元组添加到新的数据集中
        g.add((subject, predicate, obj))

# 保存新的数据集到文件中
g.serialize(destination=output_file, format="turtle")

print(f"属性三元组已提取并保存到 {output_file}")

intersection_predicates = ['http://www.w3.org/2000/01/rdf-schema#label','http://dbpedia.org/ontology/birthDate','http://yago-knowledge.org/ontology/birthDate','http://xmlns.com/foaf/0.1/gender','http://xmlns.com/foaf/0.1/surname','http://xmlns.com/foaf/0.1/givenName','http://dbpedia.org/ontology/birthYear','http://dbpedia.org/ontology/height','http://dbpedia.org/ontology/Person/height','http://yago-knowledge.org/ontology/birthYear','http://yago-knowledge.org/ontology/height','http://yago-knowledge.org/ontology/Person/height','http://www.w3.org/2003/01/geo/wgs84_pos#long','http://www.w3.org/2003/01/geo/wgs84_pos#lat','http://dbpedia.org/ontology/populationTotal','http://dbpedia.org/ontology/deathDate','http://dbpedia.org/ontology/deathYear','http://dbpedia.org/ontology/alias','http://dbpedia.org/ontology/PopulatedPlace/populationDensity''http://yago-knowledge.org/ontology/populationTotal','http://yago-knowledge.org/ontology/deathDate','http://yago-knowledge.org/ontology/deathYear','http://yago-knowledge.org/ontology/alias','http://yago-knowledge.org/ontology/PopulatedPlace/populationDensity']
