library(shiny)
library(ggmap)
# Define UI for application that draws a histogram
# ui.R

shinyUI(fluidPage(
  titlePanel("CityScapes"),
  sidebarLayout(
    sidebarPanel(
      h2('Operation'),
      h5('Choose your city and adjust the sliders 
         to see your matches'),
        # Number of cities to return
        sliderInput("integer", "Comparisons:",
                    min=1, max=10, value=5),
        
        # Decimal interval with step value
        sliderInput("decimal", "Cost of Living:",
                    min = 0, max = 1, value = 0.5, step= 0.1),
        
        # Specification of range within an interval
        sliderInput("range", "Walking Score:",
                    min = 500, max = 4000, value = c(200,500)),
        
        # Provide a custom currency format for value display,
        # with basic animation
        sliderInput("format", "Some other metric:",
                    min = 0, max = 10000, value = 0, step = 2500,
                    pre = "$", sep = ",", animate=TRUE),
        
        # Animation with custom interval (in ms) to control speed,
        # plus looping
        sliderInput("animation", "2010 - 2015:", 1, 6, 5,
                    step = 1, animate=
                      animationOptions(interval=5000, loop=TRUE))
    ),
    mainPanel(
      h1('Find Your Next Place'),
      img(src="skyline.jpg", height = 600, width = 600),
      p("Today's remote worker can go weeks or months without visiting the home office.
          Evaluate cities by teh metrics important to you, and Find a place you love.
          "),
      h2(strong("The days of spending more to live less are over. Let's find your next place."))
    )
  )
))

# CitySource is a resource for today's digital nomad. 
#We value both our time and freedom.  There is no longer 
# a reason to sacrifice livability or savings to have access to the nations best jobs. 
# such as density, average income, number of startups, cost of housing, and dozens more.
# Evaluate cities by  the metrics important to you, and Find your next place.
# , where your money will go further.  