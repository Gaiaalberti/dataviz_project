
#importing libraries 
library(ggpol)
library(ggplot2)
library(readxl)
library(tidyverse)

#importing reduced dataset 

mc <- fig_1_

#setting the colors for each political orientation

colors<-c("right" = "blue4",
          "centre-right" = "blue2",
          "centre" = "darkseagreen", 
          "centre-left" = "darkorange",
          "left" = "brown3",
          "non-alligned" = "grey")

#creating the arc bar 
p2<-ggplot(mc) + 
  geom_arcbar(aes(shares = size , r0 = 5, r1 = 10, fill = collocation)) + 
  scale_fill_manual(values = colors) +
  
  #inserting the labels over each section of the arc
  annotate("text", 
           label=paste0(round(128/705*100),"%"),x=-7 ,y=2 ,size = 6, colour = "white") +
  annotate("text", 
           label=paste0(round(176/705*100),"%"),x=-4 ,y=6.2,size = 6, colour = "white") +
  annotate("text", 
           label=paste0(round(101/705*100),"%"),x=-0.2,y=7.2,size = 6, colour = "white") +
  annotate("text",
           label=paste0(round(216/705*100),"%"),x=5 ,y=5.5,size = 6, colour = "white") +
  annotate("text", 
           label=paste0(round(38/705*100),"%"),x=7.9 ,y=2.5 ,size = 6, colour = "white") +
  annotate("text", 
           label=paste0(round(46/705*100),"%"),x=8.5,y=0.7,size = 6, colour = "white") +

  #setting design characteristics 
  coord_fixed() +
  theme_void()+
  theme(title = element_text(size = 9),
        plot.title = element_text(hjust = 0.5),
        plot.subtitle = element_text(hjust = 0.5),
        plot.background = element_rect(fill = "#eeeeee", color = "#eeeeee"),
        legend.position = 'bottom',
        legend.direction = "horizontal",
        legend.spacing.y = unit(0.1,"cm"),
        legend.spacing.x = unit(0.1,"cm"),
        legend.key.size = unit(0.8, 'lines'),
        legend.text = element_text(margin = margin(r = 1, unit = 'cm'), size = 12),
        legend.text.align = 0)+
  annotate("text", x = 0, y = 1, label = paste0("2019-2014 \n EU Parliament "),colour = "black",size=6)+
  labs(caption = "Source: https://www.europarl.europa.eu/meps/en/full-list")+
  guides(fill=guide_legend(nrow=2,byrow=FALSE,reverse =FALSE ,title=NULL))
p2