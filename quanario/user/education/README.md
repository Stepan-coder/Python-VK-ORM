# [Documentation](../../) / [User](../) / Education

### [education.py](education.py)
><details><summary>Class `Education` - Information about fields from the user `Education` section.</summary><p>
>
>* `schools`: [Optional](#educationpy)[[List](#educationpy)[[School](#schoolspy)]] - _Property_ for getting a list of schools where the user studied. Array of instances of the `School` class.
>* `universities`: [Optional](#educationpy)[[List](#educationpy)[[University](#universitiespy)]]  - _Property_ for getting a list of universities where the user studied. Array of instances of the `University` class.
>
></p></details>
---
### [schools.py](schools.py)
><details><summary>Class `School` - Information about fields from the user `School` section.</summary><p>
>
>* `id`: [int](#schoolspy) - _Property_ for getting the school ID.
>* `name`: [str](#schoolspy) - _Property_ for getting the name of the school.
>* `city`: [int](#schoolspy) - _Property_ for getting the ID of the city where the school is located.
>* `country`: [int](#schoolspy) - _Property_ for getting the ID of the country where the school is located.
>* `year_from`: [int](#schoolspy) - _Property_ for getting the year of starting school.
>* `year_to`: [int](#schoolspy) - _Property_ for getting the year of graduation from school.
>* `year_graduated`: [int](#schoolspy) - _Property_ for getting the year of graduation from school.
>* `school_class`: [str](#schoolspy) - _Property_ for getting a class letter.
>* `speciality`: [str](#schoolspy) - _Property_ for getting a class specialization at school.
>* `school_type`: [SchoolType](#schoolspy) - _Property_ for getting the school ID.
>* `get_json()`: [json](#schoolspy) - This method generates a json object from the fields of the `School` class.
>* *`__convert_school_type()`: [SchoolType](#schoolspy) - This private method converts the numeric representation of the value `school_type` to Enum `SchoolType`.*
>
></p></details>

><details><summary>Enum `SchoolType`</summary><p>
>
>* `SCHOOL` 
>* `GYMNASIUM`
>* `LYCEUM`
>* `BOARDING_SCHOOL`
>* `EVENING_SCHOOL` 
>* `MUSIC_SCHOOL`
>* `SPORTS_SCHOOL`
>* `ART_SCHOOL`
>* `COLLAGE`
>* `PROFESSIONAL_LYCEUM`
>* `TECHNICAL_SCHOOL`
>* `VOCATIONAL_SCHOOL`
>* `UCHILISHE`
>* `SCHOOL_OF_ARTS`
>
></p></details>
---
### [universities.py](universities.py)
><details><summary>Class `University` - Information about fields from the user `University` section.</summary><p>
>
>* `id`: [int](#universitiespy) - _Property_ for getting the university ID.
>* `name`: [str](#universitiespy) - _Property_ for getting the name of the university.
>* `city`: [int](#universitiespy) - _Property_ for getting the ID of the city where the university is located.
>* `country`: [int](#universitiespy) - _Property_ for obtaining the ID of the country in which the university is located.
>* `faculty_id`: [int](#universitiespy) - _Property_ for getting the faculty ID.
>* `faculty_name`: [str](#universitiespy) - _Property_ for getting the name of the faculty.
>* `chair_id`: [int](#universitiespy) - _Property_ for getting the department ID.
>* `chair_name`: [str](#universitiespy) - _Property_ for getting the name of the department.
>* `graduation`: [int](#universitiespy) - _Property_ for getting the end year.
>* `education_form`: [str](#universitiespy) - _Property_ for obtaining a form of training.
>* `education_status`: [str](#universitiespy) - _Property_ for getting the training status.
>* `get_json()`: [json](#universitiespy) - This method generates a json object from the fields of the `School` class.
>
></p></details>