# [Documentation](../../) / User


### [user.py](user.py)
><details><summary>Class `User` - Information about fields from the user 'User' section.</summary><p>
>
>* `user_id`: [int](#userpy) - _Property_ for getting the user ID.
>* `domain`: [str](#userpy) - _Property_ for getting a short page address. A string containing the short address of the page is returned (for example, andrew). If it is not assigned, "id"+user_id is returned, for example, id35828305.
>* `screen_name`: [str](#userpy) - _Property_ for getting a short page name.
>* `first_name`: [str](#userpy) - _Property_ for getting the user name.
>* `last_name`: [str](#userpy) - _Property_ for getting the user's last name.
>* `birthday`: [str](#userpy) - _Property_ for getting the user's date of birth, in the format YYYY-MM-DD.
>* `sex`: [Sex](#userpy) - _Property_ for getting the user's gender. For more information, see `person_enum.Sex`.
>* `relation`: [Relation](#userpy) - _Property_ for getting information about the marital status of the user. For more information, see `person_enum.Relation`.
>* `online`: [Online](#userpy) - _Property_ for getting information about whether the user is currently on the site.
>* `count`: [Optional](#userpy)[[Counters](#counterspy)] - _Property_ for getting information about the number of different objects from the user.
>* `occupation`: [Optional](#userpy)[[Occupation](#occupationpy)] - _Property_ for getting information about user activity.
>* `contacts`: [Optional](#userpy)[[Contacts](#contactspy)] - _Property_ for getting information about the user's contact information
>* `interests`: [Optional](#userpy)[[Interests](#interestspy)] - _Property_ for getting information about fields from the `Life position` section
>* `education`: [Optional](#userpy)[[Education](#education--educationpy)] - _Property_ for obtaining educational institutions in which the user studied.
>* `career`: [Optional](#userpy)[[List](#userpy)[[Career](#careerpy)]] - _Property_ for getting a list of schools where the user studied. Array of instances of the `School` class.
>* `military`: [Optional](#userpy)[[List](#userpy)[[Military](#militarypy)]] - _Property_ for getting information about the user's military service.
>* `life_position`: [Optional](#userpy)[[LifePosition](#lifepositionpy)] - _Property_ for getting information about fields from the `Life position` section.
>* `params`: [Optional](#userpy)[[Params](#paramspy)] - _Property_ for getting information about additional user fields.
>* `get_json()`: [json](#userpy) - This method generates a json object from the fields of the `User` class.
>* *`__convert_birthdate()`: [str](#userpy) - This private method brings the date of birth of the user received from VKontakte to the standardized form `YYYY-MM-DD`* 
>* *`__decode_sex()`: [Sex](#userpy) - This private method converts the numeric representation of the value `sex` to Enum `Sex`.*
>* *`__decode_online()`: [Online](#userpy) - This private method converts the numeric representation of the value `online` to Enum `Online`.*
>* *`__decode_relation()`: [Relation](#userpy) - This private method converts the numeric representation of the value `relation` to Enum `Relation`.*
>
></p></details>

><details><summary>Enum `Sex`</summary><p>
>
>* `NOT_SPECIFIED`
>* `FEMALE`
>* `MALE`
>
></p></details>

><details><summary>Enum `Relation`</summary><p>
>
>* `NOT_SPECIFIED`
>* `NOT_MARRIED`
>* `HAVE_FRIEND`
>* `ENGAGED`
>* `EVERYTHING_IS_COMPLICATED`
>* `ACTIVE_SEARCH`
>* `IN_LOVE`
>* `CIVIL_MARRIAGE`
> 
></p></details>

><details><summary>Enum `Online`</summary><p>
>
>* `ONLINE`
>* `NOT_ONLINE`
>
></p></details>
---
### [career.py](career.py)
><details><summary>Class `Career` - Information about fields from the user 'Career' section.</summary><p>
>
>* `group_id`: [int](#careerpy) - _Property_ for getting the community ID (if available, otherwise company).
>* `company`: [str](#careerpy) - _Property_ for getting the company name (if available, otherwise group_id).
>* `city_id`: [str](#careerpy) - Everything to get the ids of the city, city (if is available, otherwise city_name).
>* `city_name`: [str](#careerpy) - _Property_ for getting the name of the city.
>* `country_id`: [int](#careerpy) - _Property_ for getting the country ID.
>* `work_from`: [int](#careerpy) - _Property_ for getting the year of the start of work.
>* `work_until`: [int](#careerpy) - _Property_ for getting the year of completion of work.
>* `position`: [str](#careerpy) - _Property_ for getting the title of the position
>* `get_json()`: [json](#careerpy) - This method generates a json object from the fields of the `Career` class.
>
></p></details>
---
### [contacts.py](contacts.py)
><details><summary>Class `Contacts` - Information about fields from the user 'Contacts' section.</summary><p>
>
>* `site`: [str](#contactspy) - _Property_ for getting the site address specified in the profile.
>* `connections`: [Dict](#contactspy)[[str](#contactspy), [Any](#contactspy)] - _Property_ for getting data about the user's services specified in the profile, such as: skype, livejournal. A separate string field containing the user's nickname is returned for each service. For example, "skype": "username".
>* `home_town`: [str](#contactspy) - _Property_ for getting the name of the hometown.
>* `city_id`: [int](#contactspy) - _Property_ for getting the user's city ID, which can be used to get it names using the `database` `method.getCitiesById`.
>* `city_name`: [str](#contactspy) - _Property_ for getting the name of the city where the user is located.
>* `country_id`: [int](#contactspy) - _Property_ for getting the user's country ID, which can be used to get it names using the `database` `method.getCitiesById`.
>* `country_name`: [str](#contactspy) - _Property_ for getting the name of the country in which the user is located.
>* `get_json()`: [json](#contactspy) - This method generates a json object from the fields of the `Contacts` class.
>
></p></details>
---
### [counters.py](counters.py)
><details><summary>Class `Counters` - Information about the number of different objects the user has.</summary><p>
>
>* `notes`: [int](#counterspy) - _Property_ for getting the number of `notes from the user.
>* `pages`: [int](#counterspy) - _Property_ for getting the number of `subscribers from the user.
>* `audios`: [int](#counterspy) - _Property_ for getting the number of `audio recordings from the user.
>* `albums`: [int](#counterspy) - _Property_ for getting the number of `photo albums from the user.
>* `photos`: [int](#counterspy) - _Property_ for getting the number of `photos from the user.
>* `videos`: [int](#counterspy) - _Property_ for getting the number of `videos from the user.
>* `user_videos`: [int](#counterspy) - _Property_ for getting the number of `videos with user`.
>* `clips_followers`: [int](#counterspy) - _Property_ for getting the number of `clips with  user`.
>* `groups`: [int](#counterspy) - _Property_ for getting the number of community subscribers from the user.
>* `friends`: [int](#counterspy) - _Property_ for getting the number of friends a user has.
>* `followers`: [int](#counterspy) - _Property_ for getting the number of `subscribers` from the user.
>* `subscriptions`: [int](#counterspy) - _Property_ for getting the number of `subscriptions` from the user.
>* `online_friends`: [int](#counterspy) - _Property_ for getting the number of `online friends` of the user.
>* `get_json()`: [json](#counterspy) - This method generates a json object from the fields of the `Counters` class.
>
></p></details>
---
### [interests.py](interests.py)
><details><summary>Class `Interests` - Information about fields from the user 'Interests' section.</summary><p>
>
>* `about`: [str](#interestspy) - _Property_ for getting the contents of the `About me` field from the profile.
>* `status`: [str](#interestspy) - _Property_ for getting user status. Returns a string containing the `status` text located in profile under the name.
>* `activities`: [str](#interestspy) - _Property_ for getting the contents of the `Activity` field from the profile.
>* `interests`: [str](#interestspy) - _Property_ for getting the contents of the `Interests` field from the profile.
>* `music`: [str](#interestspy) - _Property_ for getting the contents of the `Favorite music` field from the profile.
>* `movies`: [str](#interestspy) - _Property_ for getting the contents of the `Favorite movies` field from the profile.
>* `tv`: [str](#interestspy) - _Property_ for getting the contents of the `Favorite TV shows` field from the profile.
>* `books`: [str](#interestspy) - _Property_ for getting the contents of the `Favorite books` field from the profile.
>* `games`: [str](#interestspy) - _Property_ for getting the contents of the `Favorite games` field from the profile.
>* `quotes`: [str](#interestspy) - _Property_ for getting the contents of the `Favorite quotes` field from the profile.
>* `get_json()`: [json](#interestspy) - This method generates a json object from the fields of the 'Interests' class.
>
></p></details>
---
### [last_seen.py](last_seen.py)
><details><summary>Class `LastSeen` - The time of the user last visit.</summary><p>
>
>* `time`: [datetime](#last_seenpy) - _Property_ for getting the number of notes from the user.
>* `platform`: [Platform](#last_seenpy) - _Property_ for getting the number of subscribers from the user.
>* `get_json()`: [json](#last_seenpy) - This method generates a json object from the fields of the 'LastSeen' class.
>* *`__convert_platform()`: [Platform](#last_seenpy) - This private method converts the numeric representation of the value `platform` to Enum `Platform`.*
>
></p></details>

><details><summary>Enum `Platform`</summary><p>
>
>* `MOBILE_SITE`
>* `IPHONE_APP`
>* `IPAD_APP`
>* `ANDROID_APP`
>* `WINPHONE_APP`
>* `WINDOWS10_APP`
>* `FULL_SITE`
>
></p></details>
---
### [lifeposition.py](lifeposition.py)
><details><summary>Class `LifePosition` - Information about fields from the user `Life position` section.</summary><p>
>
>* `political`: [Political](#lifepositionpy) - _Property_ for getting information from the `Political Preferences` field.
>* `langs`: [List](#lifepositionpy)[[str](#lifepositionpy)] - _Property_ for getting information from the `Political Preferences` field.
>* `religion`: [str](#lifepositionpy) - _Property_ for getting information from the `Worldview` field.
>* `inspired_by`: [str](#lifepositionpy) - _Property_ for getting information from the field `Sources of inspiration`.
>* `people_main`: [PeopleMain](#lifepositionpy) - _Property_ for getting information from the field `The main thing in people`.
>* `life_main`: [LifeMain](#lifepositionpy) - _Property_ for getting information from the `Main thing in life` field.
>* `smoking`: [Position](#lifepositionpy) - _Property_ for getting information from the `Smoking Attitude` field.
>* `alcohol`: [Position](#lifepositionpy) - _Property_ for getting information from the `Attitude to alcohol` field.
>* `get_json()`: [json](#lifepositionpy) - This method generates a json object from the fields of the `LifePosition` class.
>* *`__convert_political()`: [Political](#lifepositionpy) - This private method converts the numeric representation of the value `political` to Enum `Political`.*
>* *`__convert_people_main()`: [PeopleMain](#lifepositionpy) - This private method converts the numeric representation of the value `people_main` to Enum `PeopleMain`.*
>* *`__convert_life_main()`: [LifeMain](#lifepositionpy) - This private method converts the numeric representation of the value `life_main` to Enum `LifeMain`.*
>* *`__convert_position()`: [Position](#lifepositionpy) - This private method converts the numeric representation of the value `position` to Enum `Position`.*
>
></p></details>

><details><summary>Enum `Political`</summary><p>
>
>* `COMMUNIST`
>* `SOCIALIST`
>* `MODERATE`
>* `LIBERAL`
>* `CONSERVATIVE`
>* `MONARCHICAL`
>* `ULTRACONSERVATIVE`
>* `INDIFFERENT`
>* `LIBERTARIAN`
>
></p></details>

><details><summary>Enum `PeopleMain`</summary><p>
>
>* `INTELLIGENCE_AND_CREATIVITY`
>* `KINDNESS_AND_HONESTY`
>* `BEAUTY_AND_HEALTH`
>* `POWER_AND_WEALTH`
>* `COURAGE_AND_PERSEVERANCE`
>* `HUMOR_AND_LOVE_OF_LIFE`
>
></p></details>

><details><summary>Enum `LifeMain`</summary><p>
>
>* `FAMILY_AND_CHILDREN`
>* `CAREER_AND_MONEY`
>* `ENTERTAINMENT_AND_RECREATION`
>* `SCIENCE_AND_RESEARCH`
>* `IMPROVING_THE_WORLD`
>* `SELF_DEVELOPMENT`
>* `BEAUTY_AND_ART`
>* `FAME_AND_INFLUENCE`
>
></p></details>

><details><summary>Enum `Position`</summary><p>
>
>* `SHARPLY_NEGATIVE`
>* `NEGATIVE`
>* `COMPROMISE`
>* `NEUTRAL`
>* `POSITIVE`
>
></p></details>
---
### [military.py](military.py)
><details><summary>Class `Military` - Information about fields from the user 'Military' section.</summary><p>
>
>* `unit`: [str](#militarypy) - _Property_ for getting the number of a military unit.
>* `unit_id`: [int](#militarypy) - _Property_ for getting the part ID in the database.
>* `country_id`: [int](#militarypy) - _Property_ for getting the ID of the country where the part is located.
>* `military_from`: [int](#militarypy) - _Property_ for getting the year of service start.
>* `military_until`: [int](#militarypy) - _Property_ for getting the end of service year.
>* `get_json()`: [json](#militarypy) - This method generates a json object from the fields of the `Military` class.
>
></p></details>
---
### [user](user)/ [occupation.py](occupation.py)
><details><summary>Class `Occupation` - Information about the user's current occupation.</summary><p>
>
>* `id`: [int](#occupationpy) - _Property_ for getting the activity ID.
>* `name`: [str](#occupationpy) - _Property_ for getting the name of the activity.
>* `type`: [OccupationType](#occupationpy) - _Property_ for getting the type of activity.
>* `get_json()`: [json](#occupationpy) - This method generates a json object from the fields of the `Occupation` class.
>* `__convert_occupation_type()`: [OccupationType](#occupationpy) - This private method converts the numeric representation of the value `occupation_type` to Enum `Platform`.
>
></p></details>

><details><summary>Enum `OccupationType`</summary><p>
>
>* `WORK`
>* `SCHOOL`
>* `UNIVERSITY`
>
></p></details>
---
### [params.py](params.py)
><details><summary>Class `Params` - Information about fields from the user `Params` section.</summary><p>
>
>* `can_access_closed`: [bool](#paramspy)  - _Property_ for getting information about the user's ability to see the profile when is_closed = 1 (for example, he is in friends).
>* `is_closed`: [bool](#paramspy) - _Property_ for getting information about whether the user's profile is hidden by privacy settings.
>* `has_mobile`: [bool](#paramspy) - _Property_ for getting information about whether the user's mobile phone number is known.
>* `has_photo`: [bool](#paramspy) - _Property_ for getting information about whether the user has set a profile photo.
>* `is_no_index`: [bool](#paramspy) - _Property_ for getting information about whether the profile is indexed by search sites.
>* `is_trending`: [bool](#paramspy) - _Property_ for getting information about whether the profile is indexed by search sites.
>* `is_verified`: [bool](#paramspy) - _Property_ for getting information about whether the user's page has been verified.
>* `is_wall_privat`: [bool](#paramspy) - _Property_ for getting information about whether the user's page is open.
>* `timezone`: [str](#paramspy) - _Property_ for getting information about the user's time zone.
>* `last_seen`: [Optional](#paramspy)[[LastSeen](#last_seenpy)] - _Property_ for getting information about the user's last visit.
>* `get_json()`: [json](#paramspy) - This method generates a json object from the fields of the `Params` class.
>
></p></details>
---
### [education](education) / [education.py](education/education.py)
><details><summary>Class `Education` - Information about fields from the user `Education` section.</summary><p>
>
>* `schools`: [Optional](#education--educationpy)[[List](#education--educationpy)[[School](#education--schoolspy)]] - _Property_ for getting a list of schools where the user studied. Array of instances of the `School` class.
>* `universities`: [Optional](#education--educationpy)[[List](#education--educationpy)[[University](#education--universitiespy)]]  - _Property_ for getting a list of universities where the user studied. Array of instances of the `University` class.
>
></p></details>
---
### [education](education) / [schools.py](education/schools.py)
><details><summary>Class `School` - Information about fields from the user `School` section.</summary><p>
>
>* `id`: [int](#education--schoolspy) - _Property_ for getting the school ID.
>* `name`: [str](#education--schoolspy) - _Property_ for getting the name of the school.
>* `city`: [int](#education--schoolspy) - _Property_ for getting the ID of the city where the school is located.
>* `country`: [int](#education--schoolspy) - _Property_ for getting the ID of the country where the school is located.
>* `year_from`: [int](#education--schoolspy) - _Property_ for getting the year of starting school.
>* `year_to`: [int](#education--schoolspy) - _Property_ for getting the year of graduation from school.
>* `year_graduated`: [int](#education--schoolspy) - _Property_ for getting the year of graduation from school.
>* `school_class`: [str](#education--schoolspy) - _Property_ for getting a class letter.
>* `speciality`: [str](#education--schoolspy) - _Property_ for getting a class specialization at school.
>* `school_type`: [SchoolType](#education--schoolspy) - _Property_ for getting the school ID.
>* `get_json()`: [json](#education--schoolspy) - This method generates a json object from the fields of the `School` class.
>* *`__convert_school_type()`: [SchoolType](#education--schoolspy) - This private method converts the numeric representation of the value `school_type` to Enum `SchoolType`.*
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
### [education](education) / [universities.py](education/universities.py)
><details><summary>Class `University` - Information about fields from the user `University` section.</summary><p>
>
>* `id`: [int](#education--universitiespy) - _Property_ for getting the university ID.
>* `name`: [str](#education--universitiespy) - _Property_ for getting the name of the university.
>* `city`: [int](#education--universitiespy) - _Property_ for getting the ID of the city where the university is located.
>* `country`: [int](#education--universitiespy) - _Property_ for obtaining the ID of the country in which the university is located.
>* `faculty_id`: [int](#education--universitiespy) - _Property_ for getting the faculty ID.
>* `faculty_name`: [str](#education--universitiespy) - _Property_ for getting the name of the faculty.
>* `chair_id`: [int](#education--universitiespy) - _Property_ for getting the department ID.
>* `chair_name`: [str](#education--universitiespy) - _Property_ for getting the name of the department.
>* `graduation`: [int](#education--universitiespy) - _Property_ for getting the end year.
>* `education_form`: [str](#education--universitiespy) - _Property_ for obtaining a form of training.
>* `education_status`: [str](#education--universitiespy) - _Property_ for getting the training status.
>* `get_json()`: [json](#education--universitiespy) - This method generates a json object from the fields of the `School` class.
>
></p></details>