## Introduction to database
* Alternatives: CSV file, text file, excel file are all flat files
* Databases make our life simpler, easier, faster, reliable, and secure
eg:Oracle,MySQL,SQL server.
### Relational & non-relational database
#### Relational database
  * A relational database stores data in structured tables with rows and columns, using a predefined schema to clearly define relationships between data points.
  * Relational databases are ideal for highly structured data with complex queries, while non-relational databases excel in handling large volumes of diverse data with rapid scalability needs.
###### Table
  * In a relational database all of our data is stored across multiple tables.
  * In relational databases data is stored across muliple tables to avoid data duplication.
  * There is a Primary Key associated with each tables.
#### Non-relational database
    A non-relatiional database stores data in various formats like documents, key-value pairs, or graphs, allowing for less structured and more dynamic data sets.
## SQL
  * SQL stands for Structured querry language.
  * SQL is not a general purpose programming langauge, it is domain specific language.
  * SQL is declarative programming langauge(Not procedural language).
#### Execution of an SQL Statement
     SQL->Parser, compiler 
         ->parser: tries to understand the query
         ->compiler: query optimizer (optimal way to execute) & generates code
         ->query executer->DB->results
### IMDB Dataset
#### Schema of a database
        - directors
            - id (primary key)
            - first_name
            - last_name
        - movies
            - id (primary key)
            - name
            - year
            - rank
        - actors
            - id (primary key)
            - first_name
            - last_name
            - gender
        roles
            - actor_id
            - movie_id
            - role
        director-genre
            - director_id
            - genre
            - prob

        movie_directors
            - director_id
            - movie_id

        movie_genre
            - movie_id
            - genre
#### Load IMDB data
    mysql -u username -p password
    CREATE DATABASE imdb;
    USE imdb;
    source /path/to/imdb.sql;
    SHOW tables;
##### USE, DESCRIBE, SHOW
##### SELECT
##### LIMIT,OFFSET
##### ORDER BY
##### DISTINCT
##### WHERE, Comparison operators, NULL
#### LOGICAL OPERATORS
##### AND, OR, NOT, ALL, ANY, BETWEEN, EXIST, IN, LIKE, SOME
#### AGGREGATE FUNCTIONS 
##### COUNT, MAX, MIN, AVG, SUM
##### GROUP BY
##### HAVING
### Order of KEYWORDS
#### G-H-O-L
     G : GROUP BY
     H : HAVING
     O : ORDER BY (hav ASC and DESC)
     L : LIMIT (has OFFSET)
### Join and Natural Join
    combine data in mutiple tables.
#### INNER JOIN Example

SELECT A.ID, A.name, B.course
FROM TableA A
INNER JOIN TableB B
ON A.ID=B.ID

#### Natural JOIN Example

SELECT *
FROM TableA
NATURAL JOIN TableB;

#### LEFT JOIN Example

SELECT A.ID, A.name, B.course
FROM TableA A
LEFT JOIN TableB B
ON A.ID=B.ID

#### RIGHT JOIN Example

SELECT A.ID, A.name, B.course
FROM TableA A
RIGHT JOIN TableB B
ON A.ID=B.ID

#### FULL OUTER JOIN Example

SELECT A.ID, A.name, B.course
FROM TableA A
FULL OUTER JOIN TableB B
ON A.ID=B.ID
##### IN, NOT IN, EXISTS, NOT EXISTS, ANY, ALL, Comparison operators
#### Operations
##### C R U D
###### C-CREATE
###### R-READ
###### U-UPDATE
###### D-DELETE
###### ALTER
###### DROP
###### TRUNCATE
