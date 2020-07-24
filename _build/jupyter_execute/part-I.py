# Introduction to data analysis with Python

## Table of contents

- [What is data analysis](#what-is-data-analysis)
- [Data analysis with Python](#data-analysis-with-python)
- [The Python data analysis toolbox](#the-python-data-analysis-toolbox)
    - [NumPy](#numpy)
    - [Pandas](#pandas)
    - [SciPy](#scipy)
    - [Statsmodels](#PyMC3)
    - [Scikit-Learn](#scikit-learn)
    - [Matplotlib](#matplotlib)
    - [Seaborn](#seaborn)
    - [Altair](#altair)
    - [Bokeh](#bokeh)
- [Prerequisites](#prerequisites)
    - [Basic Python programming](#basic-python-programming)
    - [Basic linear algebra ideas](#basic-linear-algebra-ideas)
- [Basic concepts in data analysis](#basic-concepts-in-data-analysis)
    - [Tabular data](#tabular-data)
    - [Non tabular data](#non-tabular-data)
    - [Relational databases](#relational-databases)
    - [Anatomy of a data table](#anatomy-of-a-data-table)
    - [Time series data](#time-series-data)

## What is data analysis

Data analysis is a endeavor with fuzzy boundaries. Some people constrain data analysis to exploratory data analysis and data visualization. Others include hypothesis testing and statistical inference. And some even incorporate machine learning techniques like dimensionality reduction and clustering. 

Here is what, according to John W. Tukey in "[The Future of Data Analysis](https://projecteuclid.org/download/pdf_1/euclid.aoms/1177704711)", one of the leading figures in data analysis and statistics in the XX century, can be included as part of the data analysis process: 

```
"Procedures for analyzing data, techniques for interpreting the results of such procedures, ways of planning the gathering of data to make its analysis easier, more precise or more accurate, and all the machinery and results of (mathematical) statistics which apply to analyzing data."
```

I personally agree with Tukey. In my 10 years of experience analysis data, I have done such wide variety of things to obtain an answer to a question that I cannot constrain the data analysis process to a fixed subset of techniques. Because, in my view, the heart of data analysis is precisely that: **to utilize a plethora of computational, mathematical, and visualization techniques, to answer meaningful questions based on data**. 

Data analysis is often associated with a subset of roles in the Data Science space: data visualization specialists, business analysts, quantitative analysts, and a few others. Yet, the true i that **there is no endeavor in Data Science that does not rely in data analysis to some extent**. Machine learning researchers, machine learning engineers, data architects, big data engineers, social science researchers, biological science researchers, and pretty much any professional working with data, will need to ingest, clean, transform, explore, visualize, and interrogate data at one point or another.

Following Tukey line of reasoning, data analysis must be regarded as a foundational skill for any professional and/or researcher that relies on data to accomplish its goals.


## Data analysis with Python

Due to the association of data analysis with roles as business analyst and quantitative analysts, Python is sometimes regarded as a secondary tool, with programming languages as R, Scala, SAS, or SPSS, as primary tools instead. From that perspective, it is fair to ask why to spend time learning Python for data analysis instead of R and SPSS. I have several answers for that coming from different angles:

1. You probably need to learn more than one programming language as every language has their own strengths and weaknesses. Adding Python to your toolbox will just make you a better analysis. 
2. I hear you: "There is just so much time in a day. I cannot learn them all!". Let's say you have time for learning a single programming language. Why Python?: (1) It's free, (2) It's easy to learn and use, (3) It has a large and constantly growing ecosystem of libraries to accomplish any data analysis task you may face, (4) It's in high demand. 
3. In addition to offering all the necessary tools for what is traditionally considered data analysis, Python is a the leader in the field of machine learning and artificial intelligence, which can expand your toolbox and skills even further.

The above does not mean you will never need to utilize other programming languages for some task, you probably will, yet Python offers a solid base from which to approach all your data analysis challenges.

## The Python data analysis toolbox

The Python data science and scientific computing ecosystem is vast. The [NUMFOCUS Foundation](https://numfocus.org/) aggregates and support [several projects](https://numfocus.org/sponsored-projects) in the field, so it's a good place to start and pay attention to.

I do not pretend to cover all the libraries out there, just because they are too many. Instead,  I'll briefly mention a selection of the most popular and the ones you probably will utilize the most.

### NumPy

It is no exaggeration to say that [NumPy](https://numpy.org/) is at the core of the entire scientific computing Python ecosystem, both as a standalone package for numerical computation and as the engine behind most data science packages.

NumPy is a package for array-like or matrix-like high-performance computation. Its “engine” is written in C, meaning that NumPy utilized “in the background” pre-compiled C code to perform computations.

Although it is not our  main tool, we will use NumPy at different parts of the data analysis process. 

An alternative to NumPy is [Xarray](http://xarray.pydata.org/en/stable/), which introduces labels to multidimensional arrays. 

### Pandas


Given its versatility and easy to use interface, [pandas](https://pandas.pydata.org/) has become one of the main tools in the data analysis toolkit. In the Python ecosystem, it is regarded as the **main data wrangling library by far**. In short, pandas provides objects and methods to: **ingest, clean, transform, explore, and output datasets from all sizes**. It can easily take care of datasets in order of millions of datapoints or several gigabytes, replacing -to some extent- the need for "big data" solutions like [Hadoop](https://hadoop.apache.org/) or [Spark](https://spark.apache.org/). 


The pandas library reach its full potential when used in tandem with libraries like NumPy, Scipy, Matplotlib, and others. In this sense, pandas is "at the core" of the data analysis process, reason why we will devote more time to pandas than to any other library in this course.

### SciPy

[SciPy](https://www.scipy.org/) is both a library and ecosystem. Here we refer to the [SciPy library](https://www.scipy.org/scipylib/index.html). The goal of Scipy is to provide several easy to use objects and methods for numerical computation, optimization, linear algebra, and statistics. 

### Statsmodels

For a long time, people working in statistical analysis could not find a Python-based user-friendly solution for statistics, so they mainly utilized R, SPSS, SAS, and other programming languages. 


The [Statsmodels](https://www.statsmodels.org/stable/index.html) package takes care of such a need by providing a series of classes and methods for statistical modeling, ranging from basic hypothesis testing to complex linear mixed effects models. Its interface is based on R, making it easy to adopt for R users. 

### PyMC3

In recent years Bayesian statistics have been adopted as an alternative to traditional frequentist statistics. PyMC3 is a Python based library for Bayesian statistical modeling and probabilistic machine learning. I do not plan to cover Bayesian statistics in this course, yet it is useful know such a library exist.

### Scikit-Learn

[Sckit-learn](https://scikit-learn.org/stable/) it is a library for machine learning and predictive analytics, and one of the most popular libraries in the data science ecosystem. Even though this is not a machine learning course, we will make use of sckit-learn from time to time as it offers several convenient functions for common data analysis tasks like clustering and dimensionality reduction.

### Matplotlib

Python has a strong data visualization ecosystem, and [Matplotlib](https://matplotlib.org/) is at the center of it. It is the most mature, stable, flexible, and versatile data visualization library in Python. Although it is designed with 2-dimensional graphics in mind, it can also handle 3-dimensional and interactive graphics. It follows a -mostly- imperative interface, meaning the user has to explicitly declare most details of the chart which makes it a bit verbose at times. 

Matplotlib, and the rest of the Python data science stack, became famous when [the first images of a black hole](https://www.blog.pythonlibrary.org/2019/04/11/python-used-to-take-photo-of-black-hole/) were produced with this library.

### Seaborn

[Seaborn](https://seaborn.pydata.org/) was developed as a high-level interface for Matplotlib with the aim to simplify chart creation for common tasks. Charts that take a couple of dozens of lines in Matplotlib may be produced with one or two lines in Seaborn. The trade off offered by Seaborn is less control regarding the display and aesthetics, for a simpler to use interface for fast development.

### Altair

[Altair](https://altair-viz.github.io/) is another data visualization library for Python, probably the younger from the lot. What distinguishes Altair from other libraries is its "declarative approach" to statistical graphics, based on the so-called [grammar of graphics](https://rb.gy/yb78qp). With Matplotlib you focus in the "how" to put things in place, whereas with Altair you focus in the "what". 

Altair is primarily aimed to work with tabular data, particularly with the pandas DataFrame object. The logic behind Altair is to utilize a elegant and consistent syntax that combines a series of graphical primitives with a series of graphical combinatorial rules. Altair trade off is similar to Seaborn: less control for simplicity and fast development.

I personally like utilizing Altair as I believe the mental model that provides is exceptionally good, so I will Altair cover in this course rather than Seaborn. 

### Bokeh

Python also provide libraries for web-based interactive data visualization. All those cool interactive charts you find online in the places websites the New York Times can be created with Libraries like [Bokeh](https://docs.bokeh.org/en/latest/index.html). Bokeh provides an elegant and concise interface for interactive graphics, and can easily handle large or streaming datasets online. 

An alternative to Bokeh is [Plotly](https://plotly.com/), which has the advantage of working with multiple programming languages. 

## Prerequisites

Some people start their data analysis learning path with little more than high-school level mathematics and end up being highly successful. For the purposes of this courses, in addition to high-school level mathematics, I assume yo know the following: (1) Basic Python, (2) Basic linear algebra ideas.

In general, I would say you need more than basic python and basic linear algebra to become a data analyst, but since I don't plan to cover statistical inference of any kind, that should be enough. If you plan to do applied statistics, you ideally want to learn linear algebra, calculus, probability theory, and experimental and quasi-experimental research methods. And that may take a year or two. 

### Basic Python programming

Regarding Python, I will assume you are familiar with:

- Variables
- Imports and prints
- Basic Python syntax
- Data types: string, int, float, bool, and complex
- Containers: lists, dictionaries, sets, and tuples
- Functions and Lambda functions 
- Control flow: for loops and while loops; if, elif and else statements
- Operators:
    - arithmetic operators (+, -, etc)
    - assignment operators (=, += -=, etc)
    - comparison operators (>, ==, <, etc)
    - logical operators (and, or, not)
    - membership operators(in, not it) 

That should be enough. If you are not familiar with Python basics, there are many courses out there that will teach you all you need to know if a couple of hours or days. For instance, [here](https://www.youtube.com/playlist?list=PL-osiE80TeTskrapNbzXhwoFUiLCjGgY7), [here](https://automatetheboringstuff.com/), [here](https://developers.google.com/edu/python/), and [here](https://www.youtube.com/watch?v=rfscVS0vtbw). 

### Basic linear algebra ideas

Regarding basic linear algebra, it is good to be familiar with the following ideas:
- Vectors
- Matrices
- Coordinate space
- Linear combinations

Now, more than learning basic linear algebra, it is important to get used to the idea of thinking in terms of manipulating, transforming, and combining vectors that live in some abstract coordinate space. I did write a linear algebra course which goes very deep in the subject that you can find [here](https://pabloinsente.github.io/intro-linear-algebra). I recommend simply searching for the concepts I mentioned before and read about it. Wikipedia it's also a perfectly fine source when you are in doubt about any concept.

## Basic concepts in data analysis

In this section we explore and define several key concepts in data analysis. the explanations will be brief, as the main is to set up the stage for the actual data analysis process. Some concepts will be reviewed in more detail later in the book.

# Libraries for this section

import pandas as pd

### Tabular data

Data comes in many shapes and sizes. However, in the context of data analysis, we usually prefer to work with **tabular data**. Put simply, **tabular data are collections of values placed in some order in a two-dimensional grid**. The horizontal dimension usually represent records, cases, or samples. The vertical dimension usually represent attributes, variables, or features.

📓  **Tabular data**: 
```
Tabular data are collections of values placed in a two-dimensional grid. The horizontal dimension usually represent records, cases, or samples. The vertical dimension usually represent attributes, variables, or features.
```

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

### Non tabular data

Not all data comes in tabular form. As the name suggest, any collection of values that is not arranged in a table falls into this category: image data, video data, audio data, documents, website logs, graph data, and others. 

📓  **Non tabular data**: 
```
Any data format that is not structured in tabular form. Examples are: image data, video data, audio data, website logs, and graph data.
```

For instance, digital color images are collection of red, green, and blue (RGB) pixels. In addition, you have to consider information about their dimensionality. All together, you need five dimensions to represent an image: red, green, blue, width, and height. Hence, you can't just fit a JPEG or PNG image into a table.

There are **strategies to coerce non tabular data into tabular form**. For instance, a graph with nodes and links can be tabulated as:

graph_data = {'From-node': ["alligator", "elk", "whale"],
               'To-node': ["rattlesnake", "vulture", "moose"],
               'Type-link': ["Directed", "Directed", "Directed"]}

non_tabular_data = pd.DataFrame.from_dict(graph_data)

non_tabular_data

Yet, it is not always the case you can coerce non-tabular into tabular data. Not at least in a way that makes sense from a data analysis perspective. In his book I am mostly concerned with tabular data, reason why I won't touch the non-tabular case moving forward.

### Relational databases

Relational databases (RLDB)are closely related to tabular data. The concept of a relational database model was  introduced in 1970 by [Edgar F. Codd](https://en.wikipedia.org/wiki/Edgar_F._Codd), a researcher at IBM. 

We can think in relational databases as generalizations of tabular data objects: as collections of data tables associated in some specific manner, such that the user can operate on multiple tables at once. 

📓  **Relational database**: 
```
Collections of data tables associated in some specific manner, such that the user can operate on multiple tables at once.
```

Let's say that you do an additional survey among your friends, one about their food preferences. Since The previous one was about Anime, you do not want to put all the data in the same table. What you can do is to create a new table with the data collected from the new survey, and to define a way to associate the contents from both surveys. Since "Name" is in both tables, it is the logical option to use as a "key" to link both tables. Suppose your new table looks like this:

survey_data_2 = {'Name': ["Luis", "Lulu", "Roberto"],
               'American-food': [6, 5, 9],
               'Mexican-food': [8, 9, 8],
               'Japanese-food': [9, 10, 8]}
tabular_data_2 = pd.DataFrame.from_dict(survey_data_2)

tabular_data_2

Now we can merge the data as needed utilizing the name as "key" as:

tabular_data.merge(tabular_data_2, on='Name')

The traditional way to communicate with relational databases is with [SQL](https://en.wikipedia.org/wiki/SQL) or Structured Query Language. There are many versions of SQL around, but they are all pretty similar. The `pandas` library is roughly based on SQL, and it does contain many SQL-like functions to manipulate data. In my experience, relational databases and SQL are the standard tool to deal with enterprise-level data systems, and `pandas` (and R, SPSS, and others) is most commonly used in research contexts and to prototype enterprise-level solutions. 

If you want to learn more about relational databases and data management systems, you can read the original Codd's paper [here](https://www.seas.upenn.edu/~zives/03f/cis550/codd.pdf)

### Anatomy of a data table

Tables will be the object with which we will interact the most. Sometimes is easier to remember concepts by associating them with graphical displays. Below you can find a chart with the many ways in which each section of table is called on different contexts. 

<img src="images/anatomy-table.svg" >

### Time series data

Fun fact: `pandas` derives its name from "**pa**nel **da**ta **s**ystem" as [its original goal](https://google-code-archive-downloads.storage.googleapis.com/v2/code.google.com/pandas/nyfpug.pdf) was developing a library to primarily manipulate such kind of data. Panel data happens to be an example of time series data as well. In simple terms, time series are **records collected sequentially over time that usually refer to the same entities** (e.g., people, cities, factories, etc). 


📓  **Time series**: 
```
Records collected sequentially over time that usually refer to the same entities (e.g., people, cities, factories, etc).
```

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

In this section I group and provide brief definitions of the most common ways to name variables according to the following criteria: (1) the "nature" of the entity to be measured or of the measurement itself, (2) their role in causal processes. 




Continuous, quantitative, numerical, floating point, integer, interval, ratio, discrete
Ordinal, ranked, ordered 
Categorical, nominal, binary, dummy, time, qualitative 

Dependent and independent 
Endogenous, exogenous
Experimental/intervention and control/placebo


Extraneous variables, confounding variables 

