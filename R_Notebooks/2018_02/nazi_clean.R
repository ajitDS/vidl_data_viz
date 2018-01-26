# Clean data --- 
names(nazi)[1] <- "religion"
names(nazi)[2] <- "cohort"
names(nazi)[3] <- "residence"
names(nazi)[4] <- "gender"
names(nazi)[5] <- "membership"
names(nazi)[6] <- "count"
nazi$religion = gsub("1", "Protestant", nazi$religion)
nazi$religion = gsub("2", "Catholic", nazi$religion)
nazi$religion = gsub("3", "None", nazi$religion)
nazi$cohort = gsub("1", "Empire", nazi$cohort)
nazi$cohort = gsub("2", "Late Empire", nazi$cohort)
nazi$cohort = gsub("3", "Early Weimar", nazi$cohort)
nazi$cohort = gsub("4", "Late Weimar", nazi$cohort)
nazi$cohort = gsub("5", "Third Reich", nazi$cohort)
nazi$residence = gsub("1", "rural", nazi$residence)
nazi$residence = gsub("2", "suburban", nazi$residence)
nazi$gender = gsub("1", "male", nazi$gender)
nazi$gender = gsub("2", "female", nazi$gender)
nazi$membership = gsub("1", "yes", nazi$membership)
nazi$membership = gsub("0", "no", nazi$membership)
