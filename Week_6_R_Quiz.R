Dataset <- 
  read.table("C:/Users/jare/SkyDrive/WorkDocs/CUNY/Data_Analytics/Data_Programming/Week 6/pizza-store-data.csv",
             header=TRUE, sep=",", na.strings="NA", dec=".", strip.white=TRUE)

head(Dataset)
names(Dataset) #Prints out the column names (Identifies the column)
#prints out the the type of data contained in each column

class(Dataset[,1])
class(Dataset[,2])
class(Dataset[,3])
class(Dataset[,4])


#Prints the summary
summary(Dataset)


