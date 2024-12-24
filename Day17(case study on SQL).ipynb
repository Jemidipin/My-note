{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "WEiBwlhgYtYx"
   },
   "source": [
    "# Case Study on SQL\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 129,
   "metadata": {
    "id": "Q6xrAf0CgwyW"
   },
   "outputs": [],
   "source": [
    "import sqlite3\n",
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 131,
   "metadata": {
    "id": "YOO65TNTg7fg"
   },
   "outputs": [],
   "source": [
    "def load_imdb_database(db_path):\n",
    "  try:\n",
    "    conn = sqlite3.connect(db_path)\n",
    "    print(\"IMDB database loaded successfully.\")\n",
    "    return conn\n",
    "  except sqlite3.Error as e:\n",
    "    print(f\"Error loading IMDB database: {e}\")\n",
    "    return None"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 133,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "-0Th69XEghxi",
    "outputId": "d560fd50-0f2f-4462-a15e-46ddcb114534"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "IMDB database loaded successfully.\n",
      "Connection successful\n"
     ]
    }
   ],
   "source": [
    "db_path = \"D:\\\\ICT_DataScience\\\\case studies\\\\SQL\\\\imdb.db\"\n",
    "conn = load_imdb_database(db_path)\n",
    "\n",
    "if conn:\n",
    "  print(\"Connection successful\")\n",
    "  cursor = conn.cursor()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "OyMdDsyWakEL"
   },
   "source": [
    "## Following is the schema of the IMDB database. It lists all tables and their schemas.\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 136,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "QHglU6mobmV3",
    "outputId": "c7f47151-a58d-46aa-e34a-be12da99d498"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Database Schema:\n",
      "\n",
      "Table: Movie\n",
      "Columns:\n",
      "  - index (INTEGER), NOT NULL: False, Default: None, Primary Key: False\n",
      "  - MID (TEXT), NOT NULL: False, Default: None, Primary Key: False\n",
      "  - title (TEXT), NOT NULL: False, Default: None, Primary Key: False\n",
      "  - year (TEXT), NOT NULL: False, Default: None, Primary Key: False\n",
      "  - rating (REAL), NOT NULL: False, Default: None, Primary Key: False\n",
      "  - num_votes (INTEGER), NOT NULL: False, Default: None, Primary Key: False\n",
      "\n",
      "Table: Genre\n",
      "Columns:\n",
      "  - index (INTEGER), NOT NULL: False, Default: None, Primary Key: False\n",
      "  - Name (TEXT), NOT NULL: False, Default: None, Primary Key: False\n",
      "  - GID (INTEGER), NOT NULL: False, Default: None, Primary Key: False\n",
      "\n",
      "Table: Language\n",
      "Columns:\n",
      "  - index (INTEGER), NOT NULL: False, Default: None, Primary Key: False\n",
      "  - Name (TEXT), NOT NULL: False, Default: None, Primary Key: False\n",
      "  - LAID (INTEGER), NOT NULL: False, Default: None, Primary Key: False\n",
      "\n",
      "Table: Country\n",
      "Columns:\n",
      "  - index (INTEGER), NOT NULL: False, Default: None, Primary Key: False\n",
      "  - Name (TEXT), NOT NULL: False, Default: None, Primary Key: False\n",
      "  - CID (INTEGER), NOT NULL: False, Default: None, Primary Key: False\n",
      "\n",
      "Table: Location\n",
      "Columns:\n",
      "  - index (INTEGER), NOT NULL: False, Default: None, Primary Key: False\n",
      "  - Name (TEXT), NOT NULL: False, Default: None, Primary Key: False\n",
      "  - LID (INTEGER), NOT NULL: False, Default: None, Primary Key: False\n",
      "\n",
      "Table: M_Location\n",
      "Columns:\n",
      "  - index (INTEGER), NOT NULL: False, Default: None, Primary Key: False\n",
      "  - MID (TEXT), NOT NULL: False, Default: None, Primary Key: False\n",
      "  - LID (REAL), NOT NULL: False, Default: None, Primary Key: False\n",
      "  - ID (INTEGER), NOT NULL: False, Default: None, Primary Key: False\n",
      "\n",
      "Table: M_Country\n",
      "Columns:\n",
      "  - index (INTEGER), NOT NULL: False, Default: None, Primary Key: False\n",
      "  - MID (TEXT), NOT NULL: False, Default: None, Primary Key: False\n",
      "  - CID (REAL), NOT NULL: False, Default: None, Primary Key: False\n",
      "  - ID (INTEGER), NOT NULL: False, Default: None, Primary Key: False\n",
      "\n",
      "Table: M_Language\n",
      "Columns:\n",
      "  - index (INTEGER), NOT NULL: False, Default: None, Primary Key: False\n",
      "  - MID (TEXT), NOT NULL: False, Default: None, Primary Key: False\n",
      "  - LAID (INTEGER), NOT NULL: False, Default: None, Primary Key: False\n",
      "  - ID (INTEGER), NOT NULL: False, Default: None, Primary Key: False\n",
      "\n",
      "Table: M_Genre\n",
      "Columns:\n",
      "  - index (INTEGER), NOT NULL: False, Default: None, Primary Key: False\n",
      "  - MID (TEXT), NOT NULL: False, Default: None, Primary Key: False\n",
      "  - GID (INTEGER), NOT NULL: False, Default: None, Primary Key: False\n",
      "  - ID (INTEGER), NOT NULL: False, Default: None, Primary Key: False\n",
      "\n",
      "Table: Person\n",
      "Columns:\n",
      "  - index (INTEGER), NOT NULL: False, Default: None, Primary Key: False\n",
      "  - PID (TEXT), NOT NULL: False, Default: None, Primary Key: False\n",
      "  - Name (TEXT), NOT NULL: False, Default: None, Primary Key: False\n",
      "  - Gender (TEXT), NOT NULL: False, Default: None, Primary Key: False\n",
      "\n",
      "Table: M_Producer\n",
      "Columns:\n",
      "  - index (INTEGER), NOT NULL: False, Default: None, Primary Key: False\n",
      "  - MID (TEXT), NOT NULL: False, Default: None, Primary Key: False\n",
      "  - PID (TEXT), NOT NULL: False, Default: None, Primary Key: False\n",
      "  - ID (INTEGER), NOT NULL: False, Default: None, Primary Key: False\n",
      "\n",
      "Table: M_Director\n",
      "Columns:\n",
      "  - index (INTEGER), NOT NULL: False, Default: None, Primary Key: False\n",
      "  - MID (TEXT), NOT NULL: False, Default: None, Primary Key: False\n",
      "  - PID (TEXT), NOT NULL: False, Default: None, Primary Key: False\n",
      "  - ID (INTEGER), NOT NULL: False, Default: None, Primary Key: False\n",
      "\n",
      "Table: M_Cast\n",
      "Columns:\n",
      "  - index (INTEGER), NOT NULL: False, Default: None, Primary Key: False\n",
      "  - MID (TEXT), NOT NULL: False, Default: None, Primary Key: False\n",
      "  - PID (TEXT), NOT NULL: False, Default: None, Primary Key: False\n",
      "  - ID (INTEGER), NOT NULL: False, Default: None, Primary Key: False\n"
     ]
    }
   ],
   "source": [
    "cursor.execute(\"SELECT name FROM sqlite_master WHERE type='table';\")\n",
    "tables = cursor.fetchall()\n",
    "\n",
    "print(\"Database Schema:\")\n",
    "for table in tables:\n",
    "    table_name = table[0]\n",
    "    print(f\"\\nTable: {table_name}\")\n",
    "\n",
    "    cursor.execute(f\"PRAGMA table_info({table_name});\")\n",
    "    schema = cursor.fetchall()\n",
    "\n",
    "    print(\"Columns:\")\n",
    "    for column in schema:\n",
    "        cid, name, dtype, notnull, dflt_value, pk = column\n",
    "        print(f\"  - {name} ({dtype}), NOT NULL: {bool(notnull)}, Default: {dflt_value}, Primary Key: {bool(pk)}\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "At0HJhxwcWMV"
   },
   "source": [
    "# Write SQL queries for the following questions"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "cHeY-4I-Y1Go"
   },
   "source": [
    "## 1. Write query to list first 5 rows of Person table\n",
    "\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 140,
   "metadata": {
    "id": "yTksEs_JHuK8"
   },
   "outputs": [],
   "source": [
    "q1=\"\"\"SELECT * FROM person LIMIT 5;\"\"\"    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 142,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "19rLGemCcoak",
    "outputId": "1dd3ed98-7c73-444d-af96-ec475c553487"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n"
     ]
    }
   ],
   "source": [
    "def q1_grader(q1):\n",
    "  result = pd.read_sql_query(q1, conn)\n",
    "  return result.shape == (5, 4)\n",
    "print(q1_grader(q1))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "Cmuvp9h7dZWu"
   },
   "source": [
    "## 2. Write query to select title, year and rating from Movie table"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 145,
   "metadata": {
    "id": "g7MI-hJycPtn"
   },
   "outputs": [],
   "source": [
    "\n",
    "q2 = \"\"\"SELECT title,year,rating FROM Movie;\"\"\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 147,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "gyk9b2uvd5O6",
    "outputId": "15d217f4-f3c1-475a-b0ec-ce1c2557d113"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n"
     ]
    }
   ],
   "source": [
    "def q2_grader(q2):\n",
    "  result = pd.read_sql_query(q2, conn)\n",
    "  return result.shape == (3473, 3) and result['title'][0]=='Mowgli'\n",
    "print(q2_grader(q2))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "EvD979LNeaFm"
   },
   "source": [
    "## 3. Write query to get title of first movie in movie table sorted by year in ascending order\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 150,
   "metadata": {
    "id": "noFVuK27eczz"
   },
   "outputs": [],
   "source": [
    "q3 = \"\"\"SELECT title FROM movie ORDER BY year ASC LIMIT 1;\"\"\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 152,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "jpGuMnkveeU5",
    "outputId": "c3cdb6ab-945c-4d53-be90-3b353d536dc9"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0    True\n",
      "Name: title, dtype: bool\n"
     ]
    }
   ],
   "source": [
    "def q3_grader(q3):\n",
    "  result = pd.read_sql_query(q3, conn)\n",
    "  return result['title']=='Alam Ara'\n",
    "print(q3_grader(q3))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "ZQVPvM8qgl3k"
   },
   "source": [
    "## 4. Write query to get the very first year in which Devdas movie was released"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 155,
   "metadata": {
    "id": "DbvKV1XXgmd9"
   },
   "outputs": [],
   "source": [
    "q4 = \"\"\"SELECT year FROM movie WHERE title='Devdas' ORDER BY year LIMIT 1;\"\"\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 157,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "SJWlc4gCg6Gn",
    "outputId": "5e59c08b-09cf-405e-cd84-76e2c9f606d7"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0    True\n",
      "Name: year, dtype: bool\n"
     ]
    }
   ],
   "source": [
    "def q4_grader(q4):\n",
    "  result = pd.read_sql_query(q4, conn)\n",
    "  return result['year']=='1936'\n",
    "print(q4_grader(q4))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "sLHeXz_siuSW"
   },
   "source": [
    "## 5. Write query to get the number of movies released in 2018"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 160,
   "metadata": {
    "id": "fErMDcrFiuzw"
   },
   "outputs": [],
   "source": [
    "q5 = \"\"\"SELECT COUNT(title) FROM movie WHERE year=2018;\"\"\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 162,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "mV2gadLKi6ow",
    "outputId": "1980a205-2bbd-492f-ea81-cdca16afcfc2"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n"
     ]
    }
   ],
   "source": [
    "def q5_grader(q5):\n",
    "  result = pd.read_sql_query(q5, conn)\n",
    "  return result.iloc[0, 0] == 93\n",
    "print(q5_grader(q5))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "95Y3MGgsndph"
   },
   "source": [
    "## 6. Write query to get the title of the movie with most number of votes in 2012"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 165,
   "metadata": {
    "id": "SK-BCCy2j2tz"
   },
   "outputs": [],
   "source": [
    "q6 = \"\"\"SELECT title FROM movie WHERE year=2012 LIMIT 1;\"\"\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 167,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "1s8NPuftj6kO",
    "outputId": "c11fd94d-a38d-4a22-879f-a8caee834709"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0    True\n",
      "Name: title, dtype: bool\n"
     ]
    }
   ],
   "source": [
    "def q6_grader(q6):\n",
    "  result = pd.read_sql_query(q6, conn)\n",
    "  return result[\"title\"]==\"The Avengers\"\n",
    "print(q6_grader(q6))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "anmreTN2zRzL"
   },
   "source": [
    "## 7. Write SQL query to find all the unique movie titles released in 2018"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 170,
   "metadata": {
    "id": "T3gG0QsPzSQz"
   },
   "outputs": [],
   "source": [
    "q7 = \"\"\"SELECT DISTINCT title FROM movie WHERE year=2018;\"\"\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 172,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "ndp9snvBz0U5",
    "outputId": "1a202f78-4ec3-48ac-d81f-427d0d2527ee"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n"
     ]
    }
   ],
   "source": [
    "def q7_grader(q7):\n",
    "  result = pd.read_sql_query(q7, conn)\n",
    "  return result.shape==(93, 1)\n",
    "print(q7_grader(q7))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "TZEjK38M1Q8q"
   },
   "source": [
    "## 8. Write SQL query to get total number of movies released between 2017 (inclusive) and 2018 (inclusive)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 175,
   "metadata": {
    "id": "vXz5lPZ80j3-"
   },
   "outputs": [],
   "source": [
    "q8 = \"\"\"SELECT COUNT(title) FROM movie WHERE year BETWEEN 2017 AND 2018;\"\"\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 177,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "p9wXgEae02ZV",
    "outputId": "97f742e2-4dcf-42d6-b799-39f4bdb4890f"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n"
     ]
    }
   ],
   "source": [
    "def q8_grader(q8):\n",
    "  result = pd.read_sql_query(q8, conn)\n",
    "  return result.iloc[0, 0] == 211\n",
    "print(q8_grader(q8))\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "L7WKxoUU3Ai6"
   },
   "source": [
    "## 9. Write SQL query to find the year in which maximum number of movies released"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 180,
   "metadata": {
    "id": "fktY0SbY1qSA"
   },
   "outputs": [],
   "source": [
    "q9 = \"\"\"SELECT year, COUNT(*) FROM movie GROUP BY year ORDER BY COUNT(*) DESC LIMIT 1;\"\"\"\n",
    "      "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 182,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "yiYfQr1R13As",
    "outputId": "85900d61-2666-482a-df77-b2807c45eb58"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n"
     ]
    }
   ],
   "source": [
    "def q9_grader(q9):\n",
    "  result = pd.read_sql_query(q9, conn)\n",
    "  return result[\"year\"][0]==\"2005\"\n",
    "print(q9_grader(q9))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "dP2eLdzq7lBM"
   },
   "source": [
    "## 10. Write SQL query to find the title of the movie with rating>9.5 and number of votes > 90"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 185,
   "metadata": {
    "id": "DUCNjcQM3VG-"
   },
   "outputs": [],
   "source": [
    "q10 = \"\"\"SELECT title FROM movie WHERE rating>9.5 AND num_votes>90; \"\"\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 187,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "njqsiZo-3e6o",
    "outputId": "db8d034e-1fdf-42af-cef9-917b22995502"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n"
     ]
    }
   ],
   "source": [
    "def q10_grader(q10):\n",
    "  result = pd.read_sql_query(q10, conn)\n",
    "  return result[\"title\"][0]==\"Man on Mission Fauladi\"\n",
    "print(q10_grader(q10))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "7Ov94gw_949N"
   },
   "source": [
    "## 11. Write SQL query to find the number of movies which has the word 'Dilwale' in their title"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 190,
   "metadata": {
    "id": "9T5y3B1z8H4v"
   },
   "outputs": [],
   "source": [
    "q11 = \"\"\"SELECT COUNT(title) FROM movie WHERE title LIKE '%Dilwale%' OR '%Dilwale' OR 'Dilwale%';\"\"\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 192,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "gvtXmjaz8lfg",
    "outputId": "77fa6a10-db36-4dd7-e405-57fee7b368de"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n"
     ]
    }
   ],
   "source": [
    "def q11_grader(q11):\n",
    "  result = pd.read_sql_query(q11, conn)\n",
    "  return result.iloc[0, 0] == 4\n",
    "print(q11_grader(q11))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "5PaMaYb6AwgQ"
   },
   "source": [
    "## 12. Write nested SQL query to find the CID of country which produced most number of movies"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 195,
   "metadata": {
    "id": "Ey1GZDoG-t2n"
   },
   "outputs": [],
   "source": [
    "q12 = \"\"\"SELECT CID FROM(SELECT CID,COUNT(MID) FROM m_country GROUP BY CID ORDER BY COUNT(MID) DESC)LIMIT 1;\"\"\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 197,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "5gHU4XQO-0E-",
    "outputId": "8d929b47-bdd5-4c1d-98bd-7665060822e8"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "CID    True\n",
      "Name: 0, dtype: bool\n"
     ]
    }
   ],
   "source": [
    "def q12_grader(q12):\n",
    "  result = pd.read_sql_query(q12, conn)\n",
    "  return result.iloc[0]==2.0\n",
    "print(q12_grader(q12))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "F0E3Nw4nD7ux"
   },
   "source": [
    "## 13. Write nested SQL query to the country which produced most number of movies (use both Courty table and M_Country table)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 200,
   "metadata": {
    "id": "kJaN-L9aBY4Q"
   },
   "outputs": [],
   "source": [
    "q13 = \"\"\"SELECT name FROM Country WHERE CID = (SELECT CID FROM M_Country GROUP BY CID ORDER BY COUNT(MID) DESC LIMIT 1);\"\"\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 202,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "L8JOMcpjBqZo",
    "outputId": "e939cfbb-9357-4d81-8b3a-bf09e3d91d09"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n"
     ]
    }
   ],
   "source": [
    "def q13_grader(q13):\n",
    "  result = pd.read_sql_query(q13, conn)\n",
    "  return result.iloc[0, 0] == \"India\"\n",
    "print(q13_grader(q13))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "OHcgp0uCF003"
   },
   "source": [
    "## 14. Write SQL query to get the year and number of movies per year having number of movies per year is greater than 100"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 205,
   "metadata": {
    "id": "AmIL0LgMENl_"
   },
   "outputs": [],
   "source": [
    "q14 = \"\"\"SELECT year,COUNT(*) FROM movie GROUP BY year HAVING COUNT(*) > 100;\"\"\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 207,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "RWWaEwJtE6Uj",
    "outputId": "0ce7ac38-5728-42a7-dea2-9a756d205814"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n"
     ]
    }
   ],
   "source": [
    "def q14_grader(q14):\n",
    "  result = pd.read_sql_query(q14, conn)\n",
    "  return result.shape==(13,2)\n",
    "print(q14_grader(q14))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "LcrzqodqG-Ae"
   },
   "source": [
    "## 15. Write SQL query to get the Name and Language ID (LAID) corresponding to Malayalam language"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 210,
   "metadata": {
    "id": "mZ7EH8emGXJg"
   },
   "outputs": [],
   "source": [
    "q15 = \"\"\"SELECT name,LAID FROM Language WHERE name='Malayalam';\"\"\"\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 212,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "rVRZJXwoGcdX",
    "outputId": "3767df17-3922-4dc6-f93a-7f81764748d8"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "        Name  LAID\n",
      "0  Malayalam    19\n",
      "True\n"
     ]
    }
   ],
   "source": [
    "def q15_grader(q15):\n",
    "  result = pd.read_sql_query(q15, conn)\n",
    "  print(result)\n",
    "  return result[[\"Name\", \"LAID\"]].values.tolist() == [['Malayalam', 19]]\n",
    "print(q15_grader(q15))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "DvPnI7MDJVoT"
   },
   "source": [
    "## 16. Write SQL query to do inner join with movie table and M_Language table with MID colums"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 215,
   "metadata": {
    "id": "ZPO83_w1Hxco"
   },
   "outputs": [],
   "source": [
    "q16 = \"\"\"SELECT movie.MID, movie.title,movie.rating,movie.year,movie.num_votes, M_Language.LAID,m_Language.ID\n",
    "         FROM movie\n",
    "         INNER JOIN M_Language ON movie.MID = M_Language.MID;\"\"\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 217,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "S89KrFeQIWuv",
    "outputId": "0d34f226-589e-479a-8fc4-500d4ee43243"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "            MID          title  rating  year  num_votes  LAID    ID\n",
      "0     tt2388771         Mowgli     6.6  2018      21967     0     0\n",
      "1     tt5164214  Ocean's Eight     6.2  2018     110861     0     1\n",
      "2     tt1365519    Tomb Raider     6.4  2018     142585     0     2\n",
      "3     tt0848228   The Avengers     8.1  2012    1137529     0     3\n",
      "4     tt8239946        Tumbbad     8.5  2018       7483     1     4\n",
      "...         ...            ...     ...   ...        ...   ...   ...\n",
      "3468  tt0090611    Allah-Rakha     6.2  1986         96     2  3470\n",
      "3469  tt0106270          Anari     4.7  1993        301     2  3471\n",
      "3470  tt0852989  Come December     5.7  2006         57     2  3472\n",
      "3471  tt0375882     Kala Jigar     3.3  1939        174     2  3473\n",
      "3472  tt0375890         Kanoon     3.2  1994        103     2  3474\n",
      "\n",
      "[3473 rows x 7 columns]\n"
     ]
    }
   ],
   "source": [
    "def q16_grader(q16):\n",
    "  result = pd.read_sql_query(q16, conn)\n",
    "  return result\n",
    "print(q16_grader(q16))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "vhF0SQu5Lthd"
   },
   "source": [
    "## 17. Write SQL query to list title, year and rating of malayalam movies in the database by doing an inner join with movie table and M_Language table with MID column, also assuming language ID of malayalam movies as 19"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 220,
   "metadata": {
    "id": "yHB7KI-wKw3p"
   },
   "outputs": [],
   "source": [
    "q17 = \"\"\"SELECT title, year, rating \n",
    "         FROM(SELECT M_Language.MID, M_Language.LAID, Movie.title, Movie.year, Movie.rating \n",
    "         FROM M_Language INNER JOIN Movie ON M_Language.MID = Movie.MID) WHERE LAID=19;\"\"\" "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 222,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "Ji5W5cemLX0a",
    "outputId": "1f8d1258-02e8-4854-afe3-b9583b1e4f2b"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n"
     ]
    }
   ],
   "source": [
    "def q17_grader(q17):\n",
    "  result = pd.read_sql_query(q17, conn)\n",
    "  return result.shape==(16,3)\n",
    "print(q17_grader(q17))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 224,
   "metadata": {
    "id": "GhjTNuPwqO7z"
   },
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "'[' is not recognized as an internal or external command,\n",
      "operable program or batch file.\n"
     ]
    }
   ],
   "source": [
    "![ -f academic.db ] && rm academic.db\n",
    "\n",
    "conn = sqlite3.connect(\"academic.db\")\n",
    "cursor = conn.cursor()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "aH8Y1PS9OZyj"
   },
   "source": [
    "## 18. Write SQL query to Create a table named students with two columns id (integer type) and name (varchar type)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 105,
   "metadata": {},
   "outputs": [],
   "source": [
    "q18a =\"\"\"CREATE TABLE students(id INTEGER,name VARCHAR(50));\"\"\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 107,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "whuIWdc4OAzm",
    "outputId": "7781e943-7afe-4760-d35c-2f71dba1f615"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "None\n"
     ]
    }
   ],
   "source": [
    "def q18_grader_a(q18):\n",
    "  try:\n",
    "    cursor.execute(q18a)\n",
    "    return True\n",
    "  except:\n",
    "    pass\n",
    "\n",
    "def q18_grader_b(q19):\n",
    "  result = pd.read_sql_query(q19, conn)\n",
    "  return result.columns.tolist() == ['id', 'name']\n",
    "\n",
    "q18b = \"\"\"SELECT * FROM students;\"\"\"\n",
    "\n",
    "print(q18_grader_a(q18a) and q18_grader_b(q18b))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "-hRir0DKPa9I"
   },
   "source": [
    "## 19. Write SQL query to insert the values (1, 'Alice') into students table"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 110,
   "metadata": {},
   "outputs": [],
   "source": [
    "q19_a =\"\"\"INSERT INTO students (id,name) VALUES(1,'Alice');\"\"\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 112,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "Bwq8A_58qXS7",
    "outputId": "33c05d95-b372-4643-8be6-c6d7dd0fd3f1"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n"
     ]
    }
   ],
   "source": [
    "def q19_grader_a(q19_a):\n",
    "  try:\n",
    "    cursor.execute(q19_a)\n",
    "  except:\n",
    "    pass\n",
    "  return True\n",
    "\n",
    "def q19_grader_b(q19_b):\n",
    "  result = pd.read_sql_query(q19_b, conn)\n",
    "  return result.values.tolist() == [[1, 'Alice']]\n",
    "\n",
    "q19_b = \"SELECT * FROM students\"\n",
    "print(q19_grader_a(q19_a) and q19_grader_b(q19_b))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "PuQ4VFtwSu6x"
   },
   "source": [
    "## 20. Write SQL Query to add the following more information to students table\n",
    "\n",
    "| ID | Name    |\n",
    "|----|---------|\n",
    "| 2  | Bob     |\n",
    "| 3  | Charlie |"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 118,
   "metadata": {
    "id": "mGQrZEhKqgMo"
   },
   "outputs": [],
   "source": [
    "q20 = \"\"\"INSERT INTO students(id,name) \n",
    "         VALUES(2,'Bob'),(3,'Charlie') ;\"\"\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 120,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "FRZxVn3xTAjk",
    "outputId": "c703e93e-c823-4728-aabd-0f720815fefb"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n"
     ]
    }
   ],
   "source": [
    "def q20_grader(q20):\n",
    "  try:\n",
    "    cursor.execute(q20)\n",
    "  except:\n",
    "    pass\n",
    "  return True\n",
    "\n",
    "def q20_grader_b(q20_b):\n",
    "  result = pd.read_sql_query(q20_b, conn)\n",
    "  return result.values.tolist() == [[1, 'Alice'], [2, 'Bob'], [3, 'Charlie']]\n",
    "\n",
    "print(q20_grader(q20) and q20_grader_b(q19_b))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "id": "qYNpS7UEhKc4"
   },
   "outputs": [],
   "source": [
    "# conn.close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "id": "53tIpYUusRVC"
   },
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "colab": {
   "provenance": []
  },
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
