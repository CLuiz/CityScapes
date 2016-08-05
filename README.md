# CityScapes

(This document is a work in progress)

Cityscapes is an application created to assist remote workers with choosing the correct city for their needs.  

I grew up in Cleveland.  A recent Economist article called my home town 'The Silicon Valley of the second industrial revolution'.  At that time the city had a vibrant capital market and led the country in a variety of industries, largely due to Nelson Rockefeller's founding of Standard Oil.

By 1950 the city had grown to over 900,000 people and was a cultural center along the great lakes.  As of 2015 the population of Cleveland sits at just over 380,000, and is second only to Detroit in year over year shrinkage of major US cities.

I have long pondered the fate of Cleveland.  The remnants of past glory surrounded me in my youth, crumbling monuments to a time when things were better. Cleveland has one of the finest Orchestras in the world, an international recognized art museum, and is home to playhouse square, the second largest performing arts center in the US.

Cleveland is now undergoing major changes effected to save the city.  It is trying to attract millennials and educated creatives to carve a place for itself in our digital world.  But what is required to change the fate of a city so long in decline?  

Fellow rustbelt city Pittsburgh has made some dramatic changes over the past twenty years, but still struggles to compete with the US's second tech centers. The city's most visible export is Carnegie Mellon staff to the major tech companies on the coasts.  

As the advent of remote work grows, we will be less and less bound to the cities in which our careers are based.  This will open up the opportunity to work in a high-demand, high-pay market while allowing the pursuit of a life in a less expensive locale.

This ever-expanding, well educated, and well paid remote workforce will need assistance in finding the best place for them to live according to the metrics important to them. Cityscapes is designed to fill this market void.


Cityscapes will be constructed and deployed over several stages.

Stage 1: Development of a minimum viable product.

    Phase 1: Data Pipelining. - Complete
        Build acquisition scripts for the following data sources:
            - US Census (API and scraper)
            - US Bureau of Economic Affairs (scraper)
            - Meetup (API)
            - Numbeo (scraper)
            - Biggest US Cities (scraper)
            - RJ Metrics (scraper + OCR)
            - Walkingscore (scraper)
            - Bureau of Transportation Statisitics (scraper)
            - Quandl (API)
            - Priceonomics (scraper)
        Work Product: Data in csv format

    Phase 2:  Munging and Merging - Complete
        Clean and Merge Data Gathered from Phase 1 Efforts:
            - Clean and merge the datasets one by one
            - Identify areas of data sparsity
            - Subset data to a dense form
        Work Product: Dense dataframe suitable for EDA & modeling


    Phase 3: EDA and Modeling - Complete
        EDA & preliminary modeling:
            - Apply unsupervised clustering methods to dense data set
            - Explore trends across 2010 - present time frame
            - Identify additional data types/sources to add in future phases
        Work Product: Rough models, visualizations, and target data for       future work

    Phase 4: Application Development and Deployment - Complete
        Build and Deploy Shiny Application
            - Port data to R and run kmeans and hierarchical clustering algorithms
            - Produce Dendrograms and 2d PCA viz for presentation
            - Build Shiny backbone application and add primary feature set
            - Deploy Shiny Application to Shinyapps.io for demo
        Work Product: Demonstrable Shiny Application

    Phase 5: Stage 1 Wrap Up and Retrospective - Complete
        Present Findings and Demo Application
            - Findings and application demonstrated on Aug 4th 2016 at Galvanize
            - Next steps outlined

Stage 2: Further Development and Refining of the Application:

    Phase 1: Addition of data identified in S1P3 - Current
        - Crime data
        - Yelp data
        - More detailed weather data
        - Additional economic data from Quandl and ...
    Work Product: Data pipelined, munged, and integrated into master dataframe

    Phase 2: Application Improvement & Re-Framing:
        -
