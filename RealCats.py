from CatsClass import Cats

CatList = [
    {
     "name": 'Барон',
     "gender": "мальчик",
     "age": 2,
    },
    {
     "name": "Сэм",
     "gender": "Мальчик",
     "age": 2,
    }
]
for cat in CatList:
    cat_obj = Cats()
    cat_obj.init_from_dict(cat)
    print(f" имя: {cat_obj.name}, пол: {cat_obj.gender}, возраст: {cat_obj.age}")