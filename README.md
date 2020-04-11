# Django Project: Chapter & Verse - REST-API Branch

## Project links
* [Repository](https://github.com/myraileen/GA-SEI-Script/tree/django_rest_api)
* [Deployment]()

## Overview
This branch is a version of my Djgango Project implemented as a REST-API using the Django's rest-framework. 

login user = scriptuser, password = djangoapi

#### Data Models

   * Three non-user models: this project implements 'Book', `Chapter` and `Verse` models with full CRUD on each. 
   * Full CRUD available on each model (login required for post, put, delete)

   * _POST is NOT working on chapter and verse, however... would like feedback here for how to fix the pk required field... see unsolved section below._

---

### Models
#### Chapter
| Fields | type | FK relationship |
| --- | :---: | :---: |
| book   | text | on `Book` |
| chapter_num | int |   |
| chapter | text |  |
| description | text |    |
| image_url | text|    |

### Verse
| Fields | type | FK relationship |
| --- | :---: | :---: |
| chapter   | text | on `Chapter` |
| verse_num | int |   |
| verse | text |  |
| image_url | text|    |

### Book (post-MVP)
| Fields | type | FK relationship |
| --- | :---: | :---: |
| version   | text |  |
| book_num | int |   |
| book | text |  |
| description | text |    |
| image_url | text|    |

### Unsolved Stretch Features/Stories
* stretch: learn more abouty serializers to create 'smart' urls using data values instead of the pk.
* unsolved: the chapter and verse inserts are NOT working... missing book_id pk (I tried adding it manually in the POST call, but that also failed).

### Installation requirements
* pip3
  - virtualenv
  - django
  - psycopg2-binary
  - djangorestframework

### Credits/References 
* GA-SEI Lessons