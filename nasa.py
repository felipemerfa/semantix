from sys import argv, exit
from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession


#Criando o contexto do Spark - conectando a aplicacao ao cluster.
conf = SparkConf().setAppName('Nasa')
sc = SparkContext(conf=conf)
spark = SparkSession.builder.getOrCreate()
spark.sparkContext.setLogLevel('ERROR')
source = "./"+argv[1]

rdd = sc.textFile(source)

###########################################
### [1] - Número de Hosts únicos
###########################################
hosts_unicos = rdd.map(lambda x: (x.split(' - - ')[0])).distinct().count()


###########################################
### [2] - Total de erros 404
###########################################

rdd_erros_404 = rdd.filter(lambda x: x[-5:] == '404 -')
total_erro_404 = rdd_erros_404.count()

###############################################
### [3] - Os 5 URLs que mais causaram erro 404
###############################################

# Filtra por ocorrências de erro 404
top_5_404_1 = rdd.filter(lambda x: x[-5:] == '404 -')
# Separa somente os HOSTs do RDD acima e atribui o valor 1 para todos os elementos
top_5_404_2 = top_5_404_1.map(lambda x: ((x.split(' - - ')[0]), 1))
# Soma todos os valores de cada elemento
top_5_404_3 = top_5_404_2.reduceByKey(lambda a, b: a + b)
# Lista os Hosts de maior incidência de erro 404 em ordem inversa, do maior para o menor
top_5_404 = top_5_404_3.takeOrdered(5, lambda x: -x[1])


###########################################
### [4] - Quantidade de erros 404 por dia
###########################################

qtde_dias_404_1 = rdd.filter(lambda x: x[-5:] == '404 -')
qtde_dias_404_2 =   qtde_dias_404_1.map(lambda x: (x[x.find("[")+1:][:11], 1))
qtde_dias_404_3 =   qtde_dias_404_2.reduceByKey(lambda a, b: a + b)


###########################################
### [5] - Total de bytes retornados
###########################################

bytes_total_1 = rdd.map(lambda x: x.split(" ")[-1])
bytes_total_2 = bytes_total_1.map(lambda x: int(x) if(x.isdigit()) else 0)
bytes_total = bytes_total_2.sum()



#################
### RESULTADO 
#################

print("    [1] - Número de Hosts únicos                 : \n"+str(hosts_unicos)+"\n")
print("    [2] - Total de erros 404                     : \n"+str(total_erro_404)+"\n")
print("    [3] - Os 5 URLs que mais causaram erro 404   : \n"+str(top_5_404)+"\n")
print("    [4] - Quantidade de erros 404 por dia        : \n"+str(qtde_dias_404_3.collect())+"\n")
print("    [5] - Total de bytes retornados              : \n"+str(bytes_total)+"\n")

print("FIM da execução")


