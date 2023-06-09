#------------------------------------------------------
# Part of InstaCrawlR
# GitHub: https://github.com/JonasSchroeder/InstaCrawlR
# Code by Jonas Schröder
#------------------------------------------------------

library(stringr)

#Import Table and Extract Hashtags
text <- list()
htemp <- list()
htags <- data.frame()
data <- read.csv("makeuptutorial.csv", sep = ",")
data <- as.matrix(data[-1])

maxrows <- nrow(data)
for(i in 1:maxrows){
    text[i] <- as.character(data[i,4])
    htemp <- str_extract_all(text[i], "#\\S+", TRUE)

    if(ncol(htemp) != 0){
        for(j in 1:ncol(htemp)){
            htags[i,j] <- htemp[1,j]
        }  
    }
} 

#Save Hashtags as csv for Excel
write.csv(htags, "ht_unsort_makeuptutorial.csv", fileEncoding = "UTF-8")
df_htags <- as.data.frame(table(unlist(htags)))
write.csv(df_htags, "ht_sort_makeuptutorial.csv", fileEncoding = "UTF-8")