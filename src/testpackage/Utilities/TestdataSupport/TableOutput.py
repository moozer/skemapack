'''
Created on May 27, 2011

@author: morten
'''

from Datatypes.ActivityData import ActivityData

IterableObject = [
    ActivityData( LessonsList = {40: 6, 41: 8, 43: 10, 39: 4}, 
                Course = 'Subject H1', Teacher = 'Teacher 7', Class = '1. Sem A Elektronik'),
    ActivityData( LessonsList = {1: 4, 2: 4, 3: 4, 44: 4, 45: 4, 46: 4, 47: 4, 48: 4, 49: 4, 50: 4}, 
                Course = 'Subject L1', Teacher = 'Teacher 7', Class = '1. Sem A Elektronik'),
                ]
ObjectAsTextile = '''|. Class|. Teacher|. Course|38|39|40|41|42|43|44|45|46|47|48|49|50|51|52|
|. 1. Sem A Elektronik|. Teacher 7|. Subject H1||4|6|8||10||||||||||
|. 1. Sem A Elektronik|. Teacher 7|. Subject L1|||||||4|4|4|4|4|4|4|||
'''
ObjectAsHtml = '\t<table>\n\t\t<tr>\n\t\t\t<td>Class</td>\n\t\t\t<td>Teacher</td>\n\t\t\t<td>Course</td>\n\t\t\t<td>38</td>\n\t\t\t<td>39</td>\n\t\t\t<td>40</td>\n\t\t\t<td>41</td>\n\t\t\t<td>42</td>\n\t\t\t<td>43</td>\n\t\t\t<td>44</td>\n\t\t\t<td>45</td>\n\t\t\t<td>46</td>\n\t\t\t<td>47</td>\n\t\t\t<td>48</td>\n\t\t\t<td>49</td>\n\t\t\t<td>50</td>\n\t\t\t<td>51</td>\n\t\t\t<td>52</td>\n\t\t</tr>\n\t\t<tr>\n\t\t\t<td>1. Sem A Elektronik</td>\n\t\t\t<td>Teacher 7</td>\n\t\t\t<td>Subject H1</td>\n\t\t\t<td></td>\n\t\t\t<td>4</td>\n\t\t\t<td>6</td>\n\t\t\t<td>8</td>\n\t\t\t<td></td>\n\t\t\t<td>10</td>\n\t\t\t<td></td>\n\t\t\t<td></td>\n\t\t\t<td></td>\n\t\t\t<td></td>\n\t\t\t<td></td>\n\t\t\t<td></td>\n\t\t\t<td></td>\n\t\t\t<td></td>\n\t\t\t<td></td>\n\t\t</tr>\n\t\t<tr>\n\t\t\t<td>1. Sem A Elektronik</td>\n\t\t\t<td>Teacher 7</td>\n\t\t\t<td>Subject L1</td>\n\t\t\t<td></td>\n\t\t\t<td></td>\n\t\t\t<td></td>\n\t\t\t<td></td>\n\t\t\t<td></td>\n\t\t\t<td></td>\n\t\t\t<td>4</td>\n\t\t\t<td>4</td>\n\t\t\t<td>4</td>\n\t\t\t<td>4</td>\n\t\t\t<td>4</td>\n\t\t\t<td>4</td>\n\t\t\t<td>4</td>\n\t\t\t<td></td>\n\t\t\t<td></td>\n\t\t</tr>\n\t</table>'

ObjectAsTextileNoHeader = '''|. 1. Sem A Elektronik|. Teacher 7|. Subject H1||4|6|8||10||||||||||
|. 1. Sem A Elektronik|. Teacher 7|. Subject L1|||||||4|4|4|4|4|4|4|||
'''
ObjectAsTextileColumnSum = '''|. Class|. Teacher|. Course|38|39|40|41|42|43|44|45|46|47|48|49|50|51|52|
|. 1. Sem A Elektronik|. Teacher 7|. Subject H1||4|6|8||10||||||||||
|. 1. Sem A Elektronik|. Teacher 7|. Subject L1|||||||4|4|4|4|4|4|4|||
| Sum ||||4|6|8||10|4|4|4|4|4|4|4|||
'''

ObjectAsTextileRowSum = '''|. Class|. Teacher|. Course|38|39|40|41|42|43|44|45|46|47|48|49|50|51|52|. Sum|
|. 1. Sem A Elektronik|. Teacher 7|. Subject H1||4|6|8||10||||||||||28|
|. 1. Sem A Elektronik|. Teacher 7|. Subject L1|||||||4|4|4|4|4|4|4|||28|
'''
ObjectAsTextileRowAndColumnSum = '''|. Class|. Teacher|. Course|38|39|40|41|42|43|44|45|46|47|48|49|50|51|52|. Sum|
|. 1. Sem A Elektronik|. Teacher 7|. Subject H1||4|6|8||10||||||||||28|
|. 1. Sem A Elektronik|. Teacher 7|. Subject L1|||||||4|4|4|4|4|4|4|||28|
| Sum ||||4|6|8||10|4|4|4|4|4|4|4||| 56.0|
'''

IterableObjectEasy = [
    ActivityData( LessonsList = {1: 1000}, Course = 'Subject H1', 
                Teacher = 'Teacher 7', Class = '1. Sem A Elektronik'),
                ]

ObjectAsTextilePreparation = '''|. Class|. Teacher|. Course|-4|-3|-2|-1|0|1|2|3|. Sum|
|. 1. Sem A Elektronik|. Teacher 7|. Subject H1||||||1000|||1000|
| Sum ||||||||1000||| 1000.0|
| Lessons (hours) |||||||| 750|||750.0|
| Preparation ||| 175| 175| 175| 175| 175| 175||| 1050|
| Sum |||175.0|175.0|175.0|175.0|175.0|925.0||| 1800.0|
'''

IterableObjectExtra1 = [
    ActivityData( LessonsList = {41: 4, 42: 4, 43: 4}, Course = 'Vacation', Teacher = 'Teacher 7', Class = '' )
                ]

ObjectAsTextileExtra1 = '''|. Class|. Teacher|. Course|38|39|40|41|42|43|44|45|46|47|48|49|50|51|52|
|. 1. Sem A Elektronik|. Teacher 7|. Subject H1||4|6|8||10||||||||||
|. 1. Sem A Elektronik|. Teacher 7|. Subject L1|||||||4|4|4|4|4|4|4|||
|. |. Teacher 7|. Vacation||||4|4|4||||||||||
'''
WeeksInObject = range(38,53)
