[1] -	Qual o objetivo do comando cache em Spark?

R: O objetivo do comando Cache é criar persistência do RDD. Com esta persistência você pode acessar as informações sem a necessidade de executar as transformações novamente.


[2]	- O mesmo código implementado em Spark é normalmente mais rápido que a implementação equivalente em MapReduce. Por quê?

R: O mesmo código implementado em Spark é normalmente mais rápido, porque os dados são trabalhados em memória, isso evita operações de IO excessivas.


[3]	- Qual é a função do SparkContext ?

R: A função do SparkContext é conectar a aplicação ao cluster.


[4] -	Explique com suas palavras o que é Resilient Distributed Datasets (RDD).

R: São DataSets que podem ser recriados, armazenados em memória distribuídos pelo cluster, e podem ser criados pelo programa ou vir de uma fonte externa, porém jamais poderá ser alterado.


[5] -	GroupByKey é menos eficiente que reduceByKey em grandes dataset. Por quê?

R: O GroupByKey é menos eficiente que o reduceByKey, porque ele pré-agrupa os dados dentro da partição antes de enviar as tuplas para as partições. Com o groupByKey o mesmo trafegará todas as tuplas antes do reduce ser executado, com isso há um considerável custo de processamento em shuffle.


[6] -	Explique o que o código Scala abaixo faz.

val textFile = sc . textFile ( "hdfs://..." )
val counts = textFile . flatMap ( line => line . split ( " " ))
.map ( word => ( word , 1 ))
.reduceByKey ( _ + _ )
counts . saveAsTextFile ( "hdfs://..." )

R: Este programa conta palavras.
  Os passos executados são:
  1. Cria um RDD textFile a partir de um dataset no HDFS;
  2. Separa por espaço;
  3. Atribui o valor 1 para cada palavra no Map;
  4. Cria o reduce somando a quantidade de palavras;
  5. Grava o resultado no HDFS;
                     


[EXECUÇÃO DO PROGRAMA]

1. Criar uma pasta de nome "zip" e mover os arquivos NASA_access_log_Aug95.gz e NASA_access_log_Jul95.gz para dentro da pasta.

2. Executar o comando abaixo:

   $ sh nasa.sh



[QUESTÕES]

[1]	- Número de hosts únicos.

R: 137979


[2] -	O total de erros 404.

R: 20900


[3] -	Os 5 URLs que mais causaram erro 404.

R: 

 [('hoohoo.ncsa.uiuc.edu', 251), 
  ('piweba3y.prodigy.com', 157), 
  ('jbiagioni.npt.nuwc.navy.mil', 132), 
  ('piweba1y.prodigy.com', 114), 
  ('www-d4.proxy.aol.com', 91)]



[4] -	Quantidade de erros 404 por dia.

R: 

[('05/Aug/1995', 236), ('11/Aug/1995', 263), ('12/Aug/1995', 196), ('26/Aug/1995', 366), ('28/Aug/1995', 410), ('30/Aug/1995', 571), ('06/Jul/1995', 640), ('18/Jul/1995', 465), ('04/Aug/1995', 346), ('14/Aug/1995', 287), ('11/Jul/1995', 471), ('13/Jul/1995', 531), ('17/Jul/1995', 406), ('09/Aug/1995', 279), ('31/Aug/1995', 526), ('22/Jul/1995', 192), ('10/Aug/1995', 315), ('17/Aug/1995', 271), ('04/Jul/1995', 359), ('19/Jul/1995', 639), ('27/Jul/1995', 336), ('03/Aug/1995', 304), ('07/Aug/1995', 537), ('16/Aug/1995', 259), ('20/Aug/1995', 312), ('08/Jul/1995', 302), ('10/Jul/1995', 398), ('12/Jul/1995', 471), ('23/Jul/1995', 233), ('24/Jul/1995', 328), ('15/Aug/1995', 327), ('19/Aug/1995', 209), ('21/Aug/1995', 305), ('25/Aug/1995', 415), ('05/Jul/1995', 497), ('18/Aug/1995', 256), ('01/Jul/1995', 316), ('15/Jul/1995', 254), ('06/Aug/1995', 373), ('29/Aug/1995', 420), ('07/Jul/1995', 570), ('21/Jul/1995', 334), ('22/Aug/1995', 288), ('23/Aug/1995', 345), ('27/Aug/1995', 370), ('09/Jul/1995', 348), ('14/Jul/1995', 413), ('25/Jul/1995', 461), ('28/Jul/1995', 94), ('13/Aug/1995', 216), ('24/Aug/1995', 420), ('02/Jul/1995', 291), ('08/Aug/1995', 391), ('20/Jul/1995', 428), ('01/Aug/1995', 243), ('03/Jul/1995', 474), ('16/Jul/1995', 257), ('26/Jul/1995', 336)]


[5]	- O total de bytes retornados.

R: 65524314915


