# 2. Basic concepts in data analysis

In this section we explore and define several key concepts in data analysis. The explanations will be brief, as the goal is to lay the conceptual foundations for the actual data analysis process. Some concepts will be reviewed in more detail later in the book.

# Libraries for this section

import pandas as pd

## Tabular data

Data comes in many shapes and sizes. However, in the context of data analysis, we usually prefer to work with **tabular data**. Put simply, **tabular data are collections of values placed in some order in a two-dimensional grid**. The horizontal dimension usually represent records, cases, or samples. The vertical dimension usually represent attributes, variables, or features.

📓  **Tabular data**: 
>Tabular data are collections of values placed in a two-dimensional grid. The horizontal dimension usually represent records, cases, or samples. The vertical dimension usually represent attributes, variables, or features.

Imagine you decide to make a survey among your friends asking how much they enjoyed each of the five [Naruto's seasons](https://en.wikipedia.org/wiki/List_of_Naruto_episodes). Let's build a table with their hypothetical responses. There is no need for you to understand the `pandas` code, just the output.

survey_data = {'Name': ["Luis", "Lulu", "Roberto"],
               'Age': [19, 32, 27],
               'Naruto-season-1': [6, 8, 8],
               'Naruto-season-2': [7, 3, 7],
               'Naruto-season-3': [7, 6, 5],
               'Naruto-season-4': [6, 9, 10],
               'Naruto-season-5': [8, 9, 9]}
tabular_data = pd.DataFrame.from_dict(survey_data)

tabular_data

As you can see, the data structure is clean and simple to understand, just like any spreadsheet. Each row represent one of your friends, and the columns represent their attributes and/or responses.

## Non tabular data

Not all data comes in tabular form. As the name suggest, any collection of values that is not arranged in a table falls into this category: image data, video data, audio data, documents, website logs, graph data, and others. 

📓  **Non tabular data**: 
> Any data format that is not structured in tabular form. Examples are: image data, video data, audio data, website logs, and graph data.

For instance, digital color images are collection of red, green, and blue (RGB) pixels. In addition, you have to consider information about their dimensionality. All together, you need five dimensions to represent an image: red, green, blue, width, and height. Hence, you can't just fit a JPEG or PNG image into a two-dimensional table. There is a kind of mathematical object called [tensor](https://en.wikipedia.org/wiki/Tensor) that can be used to represent higher-dimensional objects, yet it is beyond the scope of this book.

There are **strategies to coerce non tabular data into tabular form**. For instance, a graph with nodes and links can be tabulated as:

graph_data = {'From-node': ["alligator", "elk", "whale"],
               'To-node': ["rattlesnake", "vulture", "moose"],
               'Type-link': ["Directed", "Directed", "Directed"]}

non_tabular_data = pd.DataFrame.from_dict(graph_data)

non_tabular_data

Yet, it is not always the case you can coerce non-tabular into tabular data. Not at least in a way that makes sense from a data analysis perspective. In this book, I am primarily concerned with tabular data, reason why I won't touch the non-tabular case moving forward.

## Relational databases

Relational databases (RLDB)are closely related to tabular data. The concept of a relational database model was  introduced in 1970 by [Edgar F. Codd](https://en.wikipedia.org/wiki/Edgar_F._Codd), a researcher at IBM. 

We can think in relational databases as generalizations of tabular data objects: **as collections of data tables associated in some specific manner**, such that the user can operate on multiple tables at once. 

📓  **Relational database**: 
>Collections of data tables associated in some specific manner, such that the user can operate on multiple tables at once.

Let's say that you do an additional survey among your friends, one about their food preferences. Since The previous one was about Anime, you do not want to put all the data in the same table. What you can do is to create a new table with the data collected from the new survey, and to define a way to associate the contents from both surveys. Since "Name" is in both tables, it is the logical option to use as a "key" to link both tables. Suppose your new table looks like this:

survey_data_2 = {'Name': ["Luis", "Lulu", "Roberto"],
               'American-food': [6, 5, 9],
               'Mexican-food': [8, 9, 8],
               'Japanese-food': [9, 10, 8]}
tabular_data_2 = pd.DataFrame.from_dict(survey_data_2)

tabular_data_2

Now we can merge the tables utilizing the name as "key":

tabular_data.merge(tabular_data_2, on='Name')

The traditional way to communicate with relational databases is with [SQL](https://en.wikipedia.org/wiki/SQL) or Structured Query Language. There are many versions of SQL around, but they are all pretty similar. The `pandas` library is roughly based on SQL, and it does contain many SQL-like functions to manipulate data. In my experience, relational databases and SQL are the standard tool to deal with enterprise-level data systems, and `pandas` (and R, SPSS, and others) is most commonly used in research contexts and to prototype enterprise-level solutions. 

If you want to learn more about relational databases and data management systems, you can read the original Codd's paper [here](https://www.seas.upenn.edu/~zives/03f/cis550/codd.pdf)

## Anatomy of a data table

Tables will be the object with which we will interact the most. Sometimes is easier to remember concepts by associating them with graphical displays. Below you can find a chart with the many ways in which each section of table is called on different contexts. 

![](./images/anatomy-table.svg)

## Time series data

Fun fact: `pandas` derives its name from "**pa**nel **da**ta **s**ystem" as [its original goal](https://google-code-archive-downloads.storage.googleapis.com/v2/code.google.com/pandas/nyfpug.pdf) was developing a library to primarily manipulate such kind of data. Panel data happens to be an example of time series data as well. In simple terms, time series are **records collected sequentially over time that usually refer to the same entities** (e.g., people, cities, factories, etc). 


📓  **Time series**: 
> Records collected sequentially over time that usually refer to the same entities (e.g., people, cities, factories, etc).

Examples of time series data:

- Monthly hours of sunlight in a city
- Weekly sales for a company in a decade
- Electrical brain activity recordings during a psychological test
- Frequency of earthquakes in a country over time
- Panel survey of political preferences 

Any instance where you have repeated measures of some entity will form a time series. A key aspect of this type of data is the dependency between measurements: your political preferences this year, will likely affect your political preferences next year. 

Suppose you run a small online store and you keep records of the sales of your two main products: "stickers" and "mugs".  This is how your dataset may look in `pandas`:

time_series_data = {'date': ["2020-01-15", "2020-02-15", "2020-03-15", "2020-04-15", "2020-05-15"],
                    'total-sales': [1000, 1010, 900, 500, 550],
                    'stickers-sales': [600, 605, 500, 100, 200],
                    'mugs-sales': [400, 405, 400, 400, 350]}

time_series = pd.DataFrame.from_dict(time_series_data)

time_series

In this case, the rows represent "dates" as object of measurement, and the columns the type of sale. 

An alternative way to store time series data is by flipping the columns and rows as:

time_series.T

Now the rows represent the item and the columns the dates. What data organization scheme is better to use will depend on your problem at hand.

## Types of variables

During my education I have have the opportunity to learn how sociologists, economists, psychologists, neuroscientists, statisticians, and machine learning experts denominate variables or features. As you can imagine, they do not agree on how to name things, as they probably do not talk to each other all that much. What I learned is to better acquire a vocabulary as eclectic as possible to communicate effectively depending on context. 

In this section, I group and provide brief definitions of the most common ways to name variables according to the following criteria: (1) **the "nature" of the entity** to be measured or of **the type measurement**, (2) **their role in causal processes**. 

### According to measurement type

<style type="text/css">
.tg  {border-collapse:collapse;border-color:#aaa;border-spacing:0;}
.tg td{background-color:#fff;border-color:#aaa;border-style:solid;border-width:1px;color:#333;
  font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{background-color:#f38630;border-color:#aaa;border-style:solid;border-width:1px;color:#fff;
  font-family:Arial, sans-serif;font-size:14px;font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-za9b{background-color:#f97474;border-color:inherit;font-weight:bold;text-align:left;vertical-align:top}
.tg .tg-0pky{border-color:inherit;text-align:left;vertical-align:top}
@media screen and (max-width: 767px) {.tg {width: auto !important;}.tg col {width: auto !important;}.tg-wrap {overflow-x: auto;-webkit-overflow-scrolling: touch;}}</style>
<div class="tg-wrap"><table class="tg">
<tbody>
  <tr>
    <td class="tg-za9b">Variable type</td>
    <td class="tg-za9b">Definition</td>
    <td class="tg-za9b">Context</td>
    <td class="tg-za9b">Example</td>
  </tr>
  <tr>
    <td class="tg-0pky">Quantitative</td>
    <td class="tg-0pky">General term refering to any kind of numerical variable, either in the real numbers or in the natural numbers</td>
    <td class="tg-0pky">General</td>
    <td class="tg-0pky">Income, Years of education</td>
  </tr>
  <tr>
    <td class="tg-0pky">Numerical</td>
    <td class="tg-0pky">General term refering to any kind of numerical variable, either in the real numbers or in the natural numbers</td>
    <td class="tg-0pky">General</td>
    <td class="tg-0pky">Income, Speed</td>
  </tr>
  <tr>
    <td class="tg-0pky">Continuous</td>
    <td class="tg-0pky">Variable that can take set of real values</td>
    <td class="tg-0pky">General</td>
    <td class="tg-0pky">Money, Temperature</td>
  </tr>
  <tr>
    <td class="tg-0pky">Ordinal</td>
    <td class="tg-0pky">Variable whose values follow a meaningful order but the gaps between values cannot be quantified</td>
    <td class="tg-0pky">Mostly statistics</td>
    <td class="tg-0pky">Social class, Educational levels</td>
  </tr>
  <tr>
    <td class="tg-0pky">Interval</td>
    <td class="tg-0pky">Variable whose values follow a meaningful order and where differences betwteen values are meaningful</td>
    <td class="tg-0pky">Mostly statistics</td>
    <td class="tg-0pky">Age range, Income bracket</td>
  </tr>
  <tr>
    <td class="tg-0pky">Ratio</td>
    <td class="tg-0pky">Variable whose values follow a meaningful order and where differences betwteen values are mathematically meaningful</td>
    <td class="tg-0pky">Mostly statistics</td>
    <td class="tg-0pky">Speed, Body mass index</td>
  </tr>
  <tr>
    <td class="tg-0pky">Int</td>
    <td class="tg-0pky">Software representation of variables whose values belong to the natural numbers</td>
    <td class="tg-0pky">Programming, Machine learning</td>
    <td class="tg-0pky">Any natural number</td>
  </tr>
  <tr>
    <td class="tg-0pky">Floating point</td>
    <td class="tg-0pky">Software representation of variables whose values belong to the real numbers</td>
    <td class="tg-0pky">Programming, Machine learning</td>
    <td class="tg-0pky">Any real number</td>
  </tr>
  <tr>
    <td class="tg-0pky">Complex</td>
    <td class="tg-0pky">Software representation of variables whose values belong to the complex numbers</td>
    <td class="tg-0pky">Programming, Machine learning</td>
    <td class="tg-0pky">Any complex number</td>
  </tr>
  <tr>
    <td class="tg-0pky">Discrete</td>
    <td class="tg-0pky">Variable where gapst between numbers have the same magnitud, as in natural numbers</td>
    <td class="tg-0pky">General</td>
    <td class="tg-0pky">Population, Number of schools</td>
  </tr>
  <tr>
    <td class="tg-0pky">Qualitative</td>
    <td class="tg-0pky">General term to refert to variables whose values belong to a predefine set of categories and the where the ordering is not meaningful</td>
    <td class="tg-0pky">General</td>
    <td class="tg-0pky">Ethnicity, Nationality, True/False</td>
  </tr>
  <tr>
    <td class="tg-0pky">Categorical</td>
    <td class="tg-0pky">General term to refert to variables whose values belong to a predefine set of categories and the where the ordering is not meaningful</td>
    <td class="tg-0pky">General</td>
    <td class="tg-0pky">Ethnicity, Religion</td>
  </tr>
  <tr>
    <td class="tg-0pky">Nominal</td>
    <td class="tg-0pky">A type of categorical variable whose values belong to a predefine set of categories and the where the ordering is not meaningful</td>
    <td class="tg-0pky">Mostly statistics</td>
    <td class="tg-0pky">Nationality, Political affiliation</td>
  </tr>
  <tr>
    <td class="tg-0pky">Binary</td>
    <td class="tg-0pky">A type of categorical variable whose values are restricted to two categories and the where the ordering is not meaningful</td>
    <td class="tg-0pky">General</td>
    <td class="tg-0pky">True/False, Sold/Not sold</td>
  </tr>
  <tr>
    <td class="tg-0pky">Dummy</td>
    <td class="tg-0pky">An alternative way to refer to binary variables</td>
    <td class="tg-0pky">Mostly statistics</td>
    <td class="tg-0pky">True/False, Sold/Not sold</td>
  </tr>
</tbody>
</table></div>

### According to their role in causal processes

<style type="text/css">
.tg  {border-collapse:collapse;border-color:#aaa;border-spacing:0;}
.tg td{background-color:#fff;border-color:#aaa;border-style:solid;border-width:0px;color:#333;
  font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{background-color:#f38630;border-color:#aaa;border-style:solid;border-width:0px;color:#fff;
  font-family:Arial, sans-serif;font-size:14px;font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-6zme{background-color:#f97474;font-weight:bold;text-align:left;vertical-align:top}
.tg .tg-zzh6{background-color:#f97474;border-color:#f97474;font-weight:bold;text-align:left;vertical-align:top}
.tg .tg-0lax{text-align:left;vertical-align:top}
@media screen and (max-width: 767px) {.tg {width: auto !important;}.tg col {width: auto !important;}.tg-wrap {overflow-x: auto;-webkit-overflow-scrolling: touch;}}</style>
<div class="tg-wrap"><table class="tg">
<tbody>
  <tr>
    <td class="tg-6zme">Variable type</td>
    <td class="tg-6zme">Definition</td>
    <td class="tg-zzh6">Context</td>
    <td class="tg-6zme">Example</td>
  </tr>
  <tr>
    <td class="tg-0lax">Dependent</td>
    <td class="tg-0lax">Variable whose values depend on the values or "impact" of another variable</td>
    <td class="tg-0lax">General, Statistics</td>
    <td class="tg-0lax">Raise of temerature (dependent) in response to&nbsp;&nbsp;greenhouse gases emisions</td>
  </tr>
  <tr>
    <td class="tg-0lax">Independent</td>
    <td class="tg-0lax">Variable whose values "impact" of another variable and that are independent of any other variable in a model</td>
    <td class="tg-0lax">General, Statistics</td>
    <td class="tg-0lax">Raise of temerature (dependent) in response to&nbsp;&nbsp;greenhouse gases emisions (independent)</td>
  </tr>
  <tr>
    <td class="tg-0lax">Endogenous</td>
    <td class="tg-0lax">Variable whose values are determined outside a model. Similar to dependent variable.</td>
    <td class="tg-0lax">Econometrics</td>
    <td class="tg-0lax">Stock market prices and expectations among investors in the stock market</td>
  </tr>
  <tr>
    <td class="tg-0lax">Exogenous</td>
    <td class="tg-0lax">Variable whose values are determined inside a model. Similar to independent variable.</td>
    <td class="tg-0lax">Econometrics</td>
    <td class="tg-0lax">COVID-10 pandemic impacting the stock market</td>
  </tr>
  <tr>
    <td class="tg-0lax">Experimental</td>
    <td class="tg-0lax">Variables whose values are "exogenous" and/or "independent' and that aim to causaly impact some process</td>
    <td class="tg-0lax">Experimental research</td>
    <td class="tg-0lax">COVID-19 vaccine in a clinical trial</td>
  </tr>
  <tr>
    <td class="tg-0lax">Intervention</td>
    <td class="tg-0lax">Variables whose values are "exogenous" and/or "independent' and that aim to causaly impact some process</td>
    <td class="tg-0lax">Experimental research</td>
    <td class="tg-0lax">COVID-19 vaccine in a clinical trial</td>
  </tr>
  <tr>
    <td class="tg-0lax">Control</td>
    <td class="tg-0lax">Variable that is measured in a study but that is not the main focus of interst, usually with the purpose of eliminate its influence as a causal factor</td>
    <td class="tg-0lax">Experimental research</td>
    <td class="tg-0lax">Age and gender of participants in a clinical trial</td>
  </tr>
  <tr>
    <td class="tg-0lax">Placebo</td>
    <td class="tg-0lax">Variable intendent to not impact the primary outcome of interest in a study</td>
    <td class="tg-0lax">Experimental research, Medical research</td>
    <td class="tg-0lax">Sugar pill administered to participants in the control group</td>
  </tr>
  <tr>
    <td class="tg-0lax">Extraneous</td>
    <td class="tg-0lax">Variables that may inadvertently impact the outcome of process or experiment</td>
    <td class="tg-0lax">General</td>
    <td class="tg-0lax">Age and gender of participants in a clinical trial</td>
  </tr>
  <tr>
    <td class="tg-0lax">Confounding</td>
    <td class="tg-0lax">Variables that may inadvertently impact the outcome of process or experiment</td>
    <td class="tg-0lax">General, Statistics</td>
    <td class="tg-0lax">Age and gender of participants in a clinical trial</td>
  </tr>
  <tr>
    <td class="tg-0lax">Mediator</td>
    <td class="tg-0lax">Variable that links or intervene in the relationship between two or more variables</td>
    <td class="tg-0lax">Statistics</td>
    <td class="tg-0lax">SES as mediator of ZIP code and educational outcomes</td>
  </tr>
  <tr>
    <td class="tg-0lax">Moderator</td>
    <td class="tg-0lax">Variable that amplifies or reduces the impact of an independent variable ontro a dependent vriable</td>
    <td class="tg-0lax">Statistics</td>
    <td class="tg-0lax">Teachers (moderator) improving students learning outcomes</td>
  </tr>
</tbody>
</table></div>