


#2019       ajuste
datam<-read.csv(file.choose(),head=TRUE,sep=";")      #### leer el archivo datos1.csv     FC en reposo (todas)
dat1<-cbind(datam$fcrep,datam$edad)
dat1<-data.frame(dat1)
colnames(dat1)<-c("FCR2019","edad")
head(dat1)
dat1<-dat1[!is.na(dat1$FCR2019),]
dat1<-dat1[!is.na(dat1$edad),]
head(dat1)

##################################
library(caTools)

set.seed(123)
split= sample.split(dat1$FCR2019,SplitRatio=2/3)         ### archivo data1.csv original
training_set = subset(dat1, split==TRUE)
test_set=subset(dat1, split==FALSE)

regressor=lm(formula=FCR2019~edad, data= training_set)
summary(regressor)

# ver entrenamiento
y_pred=predict(regressor,newdata=test_set)
library(ggplot2)
ggplot()+
geom_point(aes(x=training_set$edad, y=training_set$FCR2019),colour='red')+
geom_line(aes(x=training_set$edad,y=predict(regressor,newdata=training_set)),colour='blue')
# ver estimados
ggplot()+
geom_point(aes(x=test_set$edad, y=test_set$FCR2019),colour='red')+
geom_line(aes(x=training_set$edad,y=predict(regressor,newdata=training_set)),colour='blue')


### aumentando el numero de variables dependientes    ***********
datam<-read.csv(file.choose(),head=TRUE,sep=";")      #### leer el archivo datos1.csv     FC en reposo (todas)
dat1<-cbind(datam$fcrep,datam$edad,datam$fc1,datam$fc2,datam$fc3,datam$fc4)
dat1<-data.frame(dat1)
colnames(dat1)<-c("FCR2019","edad","fcr1","fcr2","fcr3","fcr4")
head(dat1)
dat1<-dat1[!is.na(dat1$FCR2019),]
dat1<-dat1[!is.na(dat1$edad),]
dat1<-dat1[!is.na(dat1$fcr1),]
dat1<-dat1[!is.na(dat1$fcr2),]
dat1<-dat1[!is.na(dat1$fcr3),]
dat1<-dat1[!is.na(dat1$fcr4),]
head(dat1)
length(dat1$edad)


set.seed(123)
split= sample.split(dat1$FCR2019,SplitRatio=2/3)         ### archivo data1.csv original
training_set = subset(dat1, split==TRUE)
test_set=subset(dat1, split==FALSE)

regressor=lm(formula=FCR2019~., data= training_set)
summary(regressor)

y_pred=predict(regressor,newdata=test_set)

# ver entrenamiento

ggplot()+
geom_point(aes(x=training_set$edad, y=training_set$FCR2019),colour='red')+
geom_point(aes(x=training_set$edad,y=predict(regressor,newdata=training_set)),colour='blue')
# ver estimados
ggplot()+
geom_point(aes(x=test_set$edad, y=test_set$FCR2019),colour='red')+
geom_point(aes(x=training_set$edad,y=predict(regressor,newdata=training_set)),colour='blue')

### >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#2020       ajuste
datam2<-read.csv(file.choose(),head=TRUE,sep=",")      #### leer el archivo FCR2020c.csv     FC en reposo (todas)
dat2<-cbind(datam2$FCR2020,datam2$edad,datam2$peso,datam2$estatura)
dat2<-data.frame(dat2)
colnames(dat2)<-c("FCR2020","edad","peso","est")
head(dat2)
dat2<-dat2[!is.na(dat2$FCR2020),]
dat2<-dat2[!is.na(dat2$edad),]
head(dat2)


set.seed(123)
split= sample.split(dat2$FCR2020,SplitRatio=2/3)         ### archivo data1.csv original
training_set = subset(dat2, split==TRUE)
test_set=subset(dat2, split==FALSE)

regressor=lm(formula=FCR2020~. , data= training_set)
summary(regressor)


###############################################################################################################
###############################################################################################################

###############FCM
####### regression multiple
###############FCM
####### regression multiple
dat1<- read.csv(file.choose(),head=TRUE,sep=",")     #### Data2.csv

set.seed(123)
split= sample.split(dat1$fcm,SplitRatio=2/3)         ### archivo data1.csv original
training_set = subset(dat1, split==TRUE)
test_set=subset(dat1, split==FALSE)

regressor=lm(formula=fcm~edad, data= training_set)
summary(regressor)
cc <- regressor$coefficients
(eqn <- paste("Y =", paste(cc[1], paste(cc[-1], names(cc[-1]), sep=" * ", collapse=" + "), sep=" + "), "+ e"))     #### Data2.csv



y_pred=predict(regressor,newdata=test_set)

# ver entrenamiento

ggplot()+
geom_point(aes(x=training_set$edad, y=training_set$fcm),colour='red')+
geom_point(aes(x=training_set$edad,y=predict(regressor,newdata=training_set)),colour='blue')
# ver estimados
ggplot()+
geom_point(aes(x=test_set$edad, y=test_set$fcm),colour='red')+
geom_point(aes(x=training_set$edad,y=predict(regressor,newdata=training_set)),colour='blue')


#######################################################################################################################################
############# Frec cardiaca objetivo      EJEMPLO 50% de intensidad


datam<-read.csv(file.choose(),head=TRUE,sep=";")      #### leer el archivo datos1.csv     FC en reposo (todas)
dat1<-cbind(datam$fcrep,datam$edad,datam$fc1,datam$fc2,datam$fc3,datam$fc4)
dat1<-data.frame(dat1)
colnames(dat1)<-c("FCR2019","edad","fcr1","fcr2","fcr3","fcr4")
head(dat1)
dat1<-dat1[!is.na(dat1$FCR2019),]
dat1<-dat1[!is.na(dat1$edad),]
dat1<-dat1[!is.na(dat1$fcr1),]
dat1<-dat1[!is.na(dat1$fcr2),]
dat1<-dat1[!is.na(dat1$fcr3),]
dat1<-dat1[!is.na(dat1$fcr4),]
head(dat1)
length(dat1$edad)


FCR2019=c()
FCR2019=24.56 -dat1$edad * 0.17657 + dat1$fcr1 * 0.07721 - dat1$fcr2 * 0.09040 + dat1$fcr4 * 0.13927
fcr<-FCR2019


FCM2019 = 341.812499999999 - 8.31249999999998 * dat1$edad
fcm<-FCM2019

fcobj=fcr + (fcm - fcr) * 0.5 


plot(fcobj)



