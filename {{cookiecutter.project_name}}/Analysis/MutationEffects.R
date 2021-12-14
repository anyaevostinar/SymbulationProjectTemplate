require(ggplot2)
require(scales)
install.packages("viridis")
library(viridis)
fullcubeHelix <- c("#673F03", "#891901", "#B50142", "#D506AD", "#AB08FF", "#96FFF7", "#4755FF", "#86E9FE", "#B2FCE3", "#D4FFDD", "#EFFDF0")


temp <- c("#673F03", "#7D3002", "#891901", "#A7000F", "#B50142", "#CD0778", "#D506AD", "#E401E7", "#AB08FF","#7B1DFF", "#5731FD","#5E8EFF", "#4755FF" ,"#6FC4FE", "#86E9FE", "#96FFF7", "#B2FCE3", "#BBFFDB", "#D4FFDD", "#EFFDF0")


#Line and box plot
initial_data <- read.table("munged_average.dat", h=T)
symbiont <- subset(initial_data, partner=="Sym")
symbiont <- na.omit(symbiont)
symbiont_final <-subset(symbiont, update ==10000)



ggplot(data=symbiont, aes(x=update, y=donate, group=HMR, colour=HMR)) + labs(title=("By Vertical Transmission Rate")) + ylab("Symbiont Resource Behavior Value") + xlab("Updates") + stat_summary(aes(color=HMR, fill=HMR),fun.data="mean_cl_boot", geom=c("smooth"), se=TRUE) + theme(panel.background = element_rect(fill='white', colour='black')) + theme(panel.grid.major = element_blank(), panel.grid.minor = element_blank()) + guides(fill="none") +scale_colour_manual(name="Horizontal\nTransmission\nMutation Rate",values=viridis(3)) + scale_fill_manual(values=viridis(3)) +ylim(-1,1) + facet_wrap(~VR)
#442 x 378
ggplot(data=symbiont_final, aes(x=treatment, y=donate, fill=treatment)) + geom_boxplot(alpha=0.5, outlier.size=0) + ylab("Final Symbiont Resource Behavior Value") + xlab("Treatment") + geom_jitter(height = 0, width = 0.1) + theme(panel.background = element_rect(fill='white', colour='black')) + theme(panel.grid.major = element_blank(), panel.grid.minor = element_blank()) + guides(fill=FALSE) +ylim(-1,1) + scale_fill_manual(values=viridis(3))

ggplot(data=symbiont_final, aes(x=treatment, y=donate)) + geom_violin(draw_quantiles = c(0.25, 0.5, 0.75)) + geom_jitter(height = 0, width = 0.1) + theme(panel.background = element_rect(fill='white', colour='black')) + theme(panel.grid.major = element_blank(), panel.grid.minor = element_blank()) + guides(fill=FALSE) +ylim(-1,1) +  ylab("Final Symbiont Resource Behavior Value") + xlab("Treatment")

wilcox.test(subset(symbiont_final, treatment=="VT0.3_MR0.1")$donate, subset(symbiont_final, treatment="VT0.3_MR1.0")$donate)


#Stacked Histograms
require(ggplot2)
tenhelix <- c("#891901", "#B50142", "#D506AD", "#AB08FF", "#5731FD", "#4755FF", "#86E9FE", "#B2FCE3", "#D4FFDD", "#EFFDF0")

first_try <- read.table("munged_histogram_sym.dat", h=T)

neg1_9 <- cbind(subset(first_try, interval=="-1_-.9"), Interaction_Rate="-1 to -0.8 (Parasitic)")
neg9_8 <- cbind(subset(first_try, interval=="-.9_-.8"), Interaction_Rate="-1 to -0.8 (Parasitic)")
neg8_7 <- cbind(subset(first_try, interval=="-.8_-.7"), Interaction_Rate="-0.8 to -0.6 (Parasitic)")
neg7_6 <- cbind(subset(first_try, interval=="-.7_-.6"), Interaction_Rate="-0.8 to -0.6 (Parasitic)")
neg6_5 <- cbind(subset(first_try, interval=="-.6_-.5"), Interaction_Rate="-0.6 to -0.4 (Detrimental)")
neg5_4 <- cbind(subset(first_try, interval=="-.5_-.4"), Interaction_Rate="-0.6 to -0.4 (Detrimental)")
neg4_3 <- cbind(subset(first_try, interval=="-.4_-.3"), Interaction_Rate="-0.4 to -0.2 (Detrimental)")
neg3_2 <- cbind(subset(first_try, interval=="-.3_-.2"), Interaction_Rate="-0.4 to -0.2 (Detrimental)")
neg2_1 <- cbind(subset(first_try, interval=="-.2_-.1"), Interaction_Rate="-0.2 to 0 (Nearly Neutral)")
neg1_0 <- cbind(subset(first_try, interval=="-.1_0"), Interaction_Rate="-0.2 to 0 (Nearly Neutral)")
pos0_1 <- cbind(subset(first_try, interval=="0_.1"), Interaction_Rate="0 to 0.2 (Nearly Neutral)")
pos1_2 <- cbind(subset(first_try, interval==".1_.2"), Interaction_Rate="0 to 0.2 (Nearly Neutral)")
pos2_3 <- cbind(subset(first_try, interval==".2_.3"), Interaction_Rate="0.2 to 0.4 (Positive)")
pos3_4 <- cbind(subset(first_try, interval==".3_.4"), Interaction_Rate="0.2 to 0.4 (Positive)")
pos4_5 <- cbind(subset(first_try, interval==".4_.5"), Interaction_Rate="0.4 to 0.6 (Positive)")
pos5_6 <- cbind(subset(first_try, interval==".5_.6"), Interaction_Rate="0.4 to 0.6 (Positive)")
pos6_7 <- cbind(subset(first_try, interval==".6_.7"), Interaction_Rate="0.6 to 0.8 (Mutualistic)")
pos7_8 <- cbind(subset(first_try, interval==".7_.8"), Interaction_Rate="0.6 to 0.8 (Mutualistic)")
pos8_9 <- cbind(subset(first_try, interval==".8_.9"), Interaction_Rate="0.8 to 1.0 (Mutualistic)")
pos9_1 <- cbind(subset(first_try, interval==".9_1"), Interaction_Rate="0.8 to 1.0 (Mutualistic)")

combined <- rbind(neg1_9, neg9_8, neg8_7, neg7_6, neg6_5, neg5_4, neg4_3, neg3_2, neg2_1, neg1_0, pos0_1, pos1_2, pos2_3, pos3_4, pos4_5, pos5_6, pos6_7, pos7_8, pos8_9, pos9_1)


temp <- aggregate(list(count = combined$count), list(update=combined$update, treatment=combined$treatment, Interaction_Rate=combined$Interaction_Rate), sum)

ggplot(temp, aes(update, count)) + geom_area(aes(fill=Interaction_Rate), position='stack') +ylab("Count of Symbionts with Phenotype") + xlab("Evolutionary time (in updates)") +scale_fill_manual("Interaction Rate\n Phenotypes",values=tenhelix) +facet_wrap(~treatment) + theme(panel.background = element_rect(fill='light grey', colour='black')) + theme(panel.grid.major = element_blank(), panel.grid.minor = element_blank()) + guides(fill=FALSE) + guides(fill = guide_legend())

breakout <- subset(combined, treatment == "VT0.3_MR1.0")

temp <- aggregate(list(count = breakout$count), list(update=breakout$update, rep=breakout$rep, Interaction_Rate=breakout$Interaction_Rate), sum)

ggplot(temp, aes(update, count)) + geom_area(aes(fill=Interaction_Rate), position='stack') +ylab("Count of Symbionts with Phenotype") + xlab("Evolutionary time (in updates)") +scale_fill_manual("Interaction Rate\n Phenotypes",values=tenhelix) +facet_wrap(~rep) + theme(panel.background = element_rect(fill='light grey', colour='black')) + theme(panel.grid.major = element_blank(), panel.grid.minor = element_blank()) + guides(fill=FALSE) + guides(fill = guide_legend())
