

################################################################################################################
## leer datos FCR de 2019
datam<-read.csv(file.choose(),head=TRUE,sep=";")      #### leer el archivo FCR2019.csv     FC en reposo (todas)
attach(datam)
x<-datam$FCR2019
x<-x[!is.na(x)]    #### borrar los NA del vector

t1<-table(x, cut(x,breaks=quantile(x, probs=seq(0,1, by=0.25), na.rm=TRUE),include.lowest=TRUE))
## cuartiles de la muestra
print(t1)

## suma de frecuencias por cuartiles
print(apply(t1,2,sum))


## diagrama de dispersión de los datos en reposo
plot(x,main="fcrep 2019",xlab="Cantidad de mediciones",ylab="frecuencias cardiacas",col=rgb(0.4,0.4,0.8,0.6),pch=16 , cex=1)



################################################################################################################
## leer datos FCR de 2020
datam<-read.csv(file.choose(),head=TRUE,sep=";")      #### leer el archivo FCR2020.csv     FC en reposo (todas)
attach(datam)
x2<-datam$FCR2020
x2<-x2[!is.na(x2)]    #### borrar los NA del vector

t1<-table(x2, cut(x2,breaks=quantile(x2, probs=seq(0,1, by=0.25), na.rm=TRUE),include.lowest=TRUE))
## cuartiles de la muestra
print(t1)

## suma de frecuencias por cuartiles
print(apply(t1,2,sum))


## diagrama de dispersión de los datos en reposo
plot(x2,main="fcrep 2020",xlab="Cantidad de mediciones",ylab="frecuencias cardiacas",col=rgb(0.4,0.4,0.8,0.6),pch=16 , cex=1)

##################################################################################################################

## Para el caso 2019 numero de clusters
library(factoextra)
library(NbClust)

###https://www.rdocumentation.org/packages/NbClust/versions/1.0/topics/NbClust
NbClust(x, distance = "euclidean", min.nc=2, max.nc=6, method = "complete", index = "all", alphaBeale = 0.1)

## Para el caso 2020 numero de clusters
#library(factoextra)
#library(NbClust)

###https://www.rdocumentation.org/packages/NbClust/versions/1.0/topics/NbClust
NbClust(x2, distance = "euclidean", min.nc=2, max.nc=6, method = "complete", index = "all", alphaBeale = 0.1)

#################################################################################################################


#### usando clusters            para 2019 FCR

//cl<-NbClust(x, distance = "minkowski", min.nc = 4, max.nc = 6,method = "complete", index = "duda")
cl<-NbClust(x, distance = "euclidean", min.nc=2, max.nc=6, method = "complete", index = "all", alphaBeale = 0.1)
plot(x,col=cl$Best.partition)

#### usando clusters            para 2020 FCR

//cl2<-NbClust(x2, distance = "minkowski", min.nc = 4, max.nc = 6,method = "complete", index = "duda")
cl2<-NbClust(x2, distance = "euclidean", min.nc=3, max.nc=6, method = "complete", index = "all", alphaBeale = 0.1)
plot(x2,col=cl2$Best.partition)

#####################################################################################################

##### Tomar los clusters centrales, con mas información en promedio : cluster 1 y 3.
               
### separar los grupos (clusteres)   FCR 2019
ag<-c()
d<-cbind(x,cl$Best.partition)        ## asignar FCR con su cluster
## cuantos datos tiene cada cluster
s1=0.0
s2=0.0
s3=0.0
s4=0.0
for (i in 1:length(x)){
    if(d[i,2]==1) s1=s1+1
    if(d[i,2]==2) s2=s2+1
    if(d[i,2]==3) s3=s3+1
    if(d[i,2]==4) s4=s4+1
    }

cat(" Cluster 1: ",s1,"\n")
cat(" Cluster 2: ",s2,"\n")
cat(" Cluster 3: ",s3,"\n")
cat(" Cluster 4: ",s4,"\n")
####################
for (i in 1:length(x)){
    if(d[i,2]==1 || d[i,2]==3) ag=c(ag,d[i,1])
    }
summary(ag)      # identificar caracteristicas de estos dos clusters
ls<-max(ag)
li<-min(ag)

cat("Cortes en : ",li,"  ",ls,"\n")
plot(ag)

##### Tomar los clusters centrales, con mas información en promedio : cluster 1 y 3.
               
### separar los grupos (clusteres)   FCR 2020
ag2<-c()
d2<-cbind(x2,cl2$Best.partition)
## cuantos datos tiene cada cluster
s1=0.0
s2=0.0
s3=0.0
s4=0.0
for (i in 1:length(x2)){
    if(d2[i,2]==1) s1=s1+1
    if(d2[i,2]==2) s2=s2+1
    if(d2[i,2]==3) s3=s3+1
    if(d2[i,2]==4) s4=s4+1
    }

cat(" Cluster 1: ",s1,"\n")             # la selección del cluster no es por cantidad máxima de información
cat(" Cluster 2: ",s2,"\n")             # es por hubicación visual central en la grafica de dispersion
cat(" Cluster 3: ",s3,"\n")
cat(" Cluster 4: ",s4,"\n")
####################
for (i in 1:length(x2)){
    if(d2[i,2]==1 || d2[i,2]==2) ag2=c(ag2,d2[i,1])
    }
summary(ag2)      # identificar caracteristicas de estos dos clusters
ls<-max(ag2)
li<-min(ag2)

cat("Cortes en : ",li,"  ",ls,"\n")
plot(ag2)


###################################################################################################

library(boot)

# Create a function to take a resample of the values, 
# and then calculate the mean
boot_mean <- function(original_vector, resample_vector) {
    mean(original_vector[resample_vector])
}


# R is number of replications                       FCR2019
mean_results <- boot(ag, boot_mean, R = 10000)     ### de todas las FCR de los clusters 1 y 3

# Load broom to get a tidy dataframe as output.
library(broom)
tidy(mean_results)

# Calculate the confidence intervals
boot.ci(mean_results)

##############################
# R is number of replications                       FCR2020
mean_results <- boot(ag2, boot_mean, R = 10000)     ### de todas las FCR de los clusters 1 y 3

# Load broom to get a tidy dataframe as output.
library(broom)
tidy(mean_results)

# Calculate the confidence intervals
boot.ci(mean_results)

####################################################################################################







