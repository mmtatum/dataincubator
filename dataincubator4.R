library(xlsx)
library(dplyr)
library(ggplot2)

data<-read.xlsx('Downloads/1112PerkinsCDR.xlsx',1,startRow=7, stringsAsFactors=FALSE)
data<-data[3:nrow(data)-1,]

comm_college_index<-c()
state_college_index<-c()

for (i in 1:nrow(data)){
if (length(grep('Community College', data$Institution.Name[i], value=TRUE)) > 0){
    comm_college_index=append(i,comm_college_index)
    }}
    
for (i in 1:nrow(data)){
if (length(grep('State', data$Institution.Name[i], value=TRUE)) > 0){
    state_college_index=append(i,state_college_index)
    }}
    
state_coll_df<-data[state_college_index,]
comm_coll_df<-data[comm_college_index,]
other_coll_df<-data[-c(state_college_index,comm_college_index),]

other_coll_grp<-group_by(other_coll_df,ST)
other_grp_df<-summarise(other_coll_grp,sum(as.numeric(Total.Principal.Outstanding.On.Loans.in.Default....240.Days)))
names(other_grp_df)<-c('State', 'Days_Late_240_Total')
other_grp_df$Days_Late_240_Percent_Total<-
    other_grp_df$Days_Late_240_Total/
    sum(as.numeric(data$Total.Principal.Outstanding.On.Loans.in.Default....240.Days))*100
other_grp_df$Days_Late_240_Percent_Group<-
    other_grp_df$Days_Late_240_Total/
    sum(as.numeric(other_grp_df$Days_Late_240_Total))*100
other_grp_df$Category<-'Other'

state_coll_grp<-group_by(state_coll_df,ST)
state_grp_df<-summarise(state_coll_grp,sum(as.numeric(Total.Principal.Outstanding.On.Loans.in.Default....240.Days)))
names(state_grp_df)<-c('State', 'Days_Late_240_Total')
state_grp_df$Days_Late_240_Percent_Total<-
    state_grp_df$Days_Late_240_Total/
    sum(as.numeric(data$Total.Principal.Outstanding.On.Loans.in.Default....240.Days))*100
state_grp_df$Days_Late_240_Percent_Group<-
    state_grp_df$Days_Late_240_Total/
    sum(as.numeric(state_grp_df$Days_Late_240_Total))*100
state_grp_df$Category<-'State College'
    
comm_coll_grp<-group_by(comm_coll_df,ST)
comm_grp_df<-summarise(comm_coll_grp,sum(as.numeric(Total.Principal.Outstanding.On.Loans.in.Default....240.Days)))
names(comm_grp_df)<-c('State', 'Days_Late_240_Total')
comm_grp_df$Days_Late_240_Percent_Total<-
    comm_grp_df$Days_Late_240_Total/
    sum(as.numeric(data$Total.Principal.Outstanding.On.Loans.in.Default....240.Days))*100
comm_grp_df$Days_Late_240_Percent_Group<-
    comm_grp_df$Days_Late_240_Total/
    sum(as.numeric(comm_grp_df$Days_Late_240_Total))*100
comm_grp_df$Category<-'Community College'

df<-rbind(other_grp_df,rbind(state_grp_df,comm_grp_df))

g=ggplot(df,aes(State,Days_Late_240_Percent_Group, group=Category, color=Category))
print(g+geom_line()+scale_y_log10()+xlab('State') + ylab('% of People > 240 Days Late') + ggtitle("Delinquencies > 240 Days Relative to the Total Principle of the Delinquent Loans of the Group by State "))
print(g+geom_line()+scale_y_log10()+xlab('State') + ylab('% of People > 240 Days Late') + ggtitle("Delinquencies > 240 Days Relative to the Total Principle of the Delinquent Loans of the Group by State ")+facet_grid(~Category))

g2=ggplot(df,aes(State,Days_Late_240_Percent_Total, group=Category, color=Category))
print(g2+geom_line()+scale_y_log10()+xlab('State') + ylab('% of People > 240 Days Late') + ggtitle("Delinquencies > 240 Days Relative to the Total Principle of the Delinquent Loans over all States by State "))

g3=ggplot(data,aes(Institution.Name,Total.Principal.Outstanding.On.Loans.in.Default....240.Days)
print(g3+geom_point()+scale_y_log10()+xlab('Institution')+ ylab('Total Principle')+ ggtitle('Total Principle of Delinquencies > 240 Days vs Institution'))