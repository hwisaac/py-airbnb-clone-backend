# Airbnb clone backend (Python)

## library & framework

### poetry


poetry 를 통한 쟝고 설치 (현재 프로젝트의 가상환경에 django 설치)
```
poetry add django
```

설치 후 poetry.toml
```toml
[tool.poetry]
name = "airbnb-clone-backend"
version = "0.1.0"
description = ""
authors = ["hwisaac <54179672+hwisaac@users.noreply.github.com>"]
license = "MIT"
readme = "README.md"
packages = [{include = "airbnb_clone_backend"}]

[tool.poetry.dependencies]
python = "^3.11"
django = "^4.2.4"


[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"
```

poetry 로 만든 bubble(가상환경) 에 들어가기
```
poetry shell
```

>`poetry shell` 명령어는 Poetry가 관리하는 가상 환경에 쉘 접근을 제공하는 명령어입니다. Python에서는 여러 프로젝트에서 서로 다른 패키지 버전을 사용할 수 있도록 가상 환경이라는 개념을 사용합니다. 이를 통해 각 프로젝트마다 독립적인 환경을 만들어 사용할 수 있습니다. `poetry shell` 명령을 사용하면, 해당 프로젝트에 대한 가상 환경이 생성되거나 이미 존재하는 경우 해당 환경에 접속할 수 있습니다. 이 쉘 안에서 실행되는 모든 Python 프로그램은 가상 환경의 패키지를 사용하게 됩니다.

![](readMeImages/2023-08-02-11-16-16.png)

## django

### django-admin
- check
- compilemessages
- createcachetable
- dbshell
- diffsettings
- dumpdata
- flush
- inspectdb
- loaddata
- makemessages
- makemigrations
- migrate
- optimizemigration
- runserver
- sendtestemail
- shell
- showmigrations
- sqlflush
- sqlmigrate
- sqlsequencereset
- squashmigrations
- startapp
- **startproject**
- test
- testserver


현재 폴더에 프로젝트를 만든다.
```
django-admin startproject config .
```

manage.py
```py
#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

```

> 이 코드는 Django 프로젝트를 실행하기 위한 표준 명령어 실행 스크립트입니다. 이 스크립트는 명령 행에서 Django 관리 명령어들을 실행하는 데 사용됩니다. 이를테면, `python manage.py runserver`와 같은 명령어가 이 스크립트를 통해 실행됩니다.

아래는 이 코드의 주요 부분에 대한 설명입니다:

- `#!/usr/bin/env python`: 이 부분은 이 스크립트가 Python 인터프리터를 사용해 실행되어야 함을 나타내는 shebang 라인입니다. Unix와 Unix-like 시스템에서 이 스크립트는 실행 가능한 파일로 설정되어 직접 실행될 수 있습니다.
  
- `import os`, `import sys`: `os`와 `sys` 모듈을 임포트합니다. 이 모듈들은 파이썬의 표준 라이브러리로, 각각 운영 체제와 파이썬 런타임과 관련된 기능을 제공합니다.

- `def main():`: `main` 함수를 정의합니다. 이 함수는 스크립트가 실행될 때 호출되는 메인 진입점입니다.

- `os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')`: 환경 변수 `DJANGO_SETTINGS_MODULE`을 설정하며, 이 환경 변수는 Django 설정 모듈의 이름을 가리킵니다. `setdefault` 메서드는 환경 변수가 이미 설정되어 있지 않을 경우에만 값을 설정합니다.

- `from django.core.management import execute_from_command_line`: Django의 관리 명령어 실행 함수 `execute_from_command_line`을 임포트합니다.

- `try...except ImportError...`: Django 모듈을 임포트하는 데 실패하면 오류 메시지를 출력하고 스크립트를 종료합니다. 이는 Django가 설치되어 있지 않거나 파이썬 경로에 없거나, 가상 환경이 활성화되지 않았을 경우에 발생합니다.

- `execute_from_command_line(sys.argv)`: `execute_from_command_line` 함수를 호출하여 Django 관리 명령어를 실행합니다. 이 함수는 명령 행 인자들을 파라미터로 받습니다.

- `if __name__ == '__main__':`: 이 스크립트가 직접 실행되면 `main` 함수를 호출합니다. 이 스크립트가 다른 스크립트에 의해 임포트되는 경우에는 `main` 함수를 호출하지 않습니다.

> (참고) 실제 서버에 배포할 때는 서버를 실행할 때 manage.py 말고 다른 걸 사용할 것입니다.



실행하기(터미널에 다음을 입력하면 `db.sqlite3` 파일이 생성됨과 동시에 서버가 작동한다.)
```
python manage.py runserver
``` 

![](readMeImages/2023-08-02-14-32-30.png)
![](readMeImages/2023-08-02-14-33-30.png)


> Error : <br />`You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.Run 'python manage.py migrate' to apply them.`

이 메시지는 Django에서 나오는 경고 메시지로, 데이터베이스 스키마 변경에 대한 마이그레이션(migration)을 아직 적용하지 않았음을 나타냅니다. Django에서는 데이터베이스 스키마 변경을 관리하기 위해 마이그레이션 시스템을 사용합니다. 

여기서 "18 unapplied migration(s)"라는 메시지는 현재 18개의 마이그레이션 파일이 적용되지 않았음을 의미합니다(DB state를 변경시키는 파일이 18개 있음). 'admin', 'auth', 'contenttypes', 'sessions' 등의 애플리케이션에서 변경된 데이터베이스 스키마에 대한 마이그레이션 파일이 있지만 아직 데이터베이스에 적용되지 않았습니다.

이런 상태에서는 프로젝트가 제대로 동작하지 않을 수 있습니다. 왜냐하면, Django 애플리케이션은 마이그레이션 파일에 기술된 대로 데이터베이스 스키마를 기대하기 때문입니다. 이러한 변경사항을 데이터베이스에 적용하지 않으면, 애플리케이션의 모델과 실제 데이터베이스 스키마가 일치하지 않아 오류가 발생할 수 있습니다.

따라서 이 메시지는 당신이 **`python manage.py migrate` 명령을 실행해서 마이그레이션을 적용하라**는 것을 알리는 것입니다. 이 명령은 모든 마이그레이션 파일을 순서대로 적용하여, Django 애플리케이션의 모델과 데이터베이스 스키마를 동기화합니다.

#### `python manage.py migrate` 명령을 실행

![](readMeImages/2023-08-02-14-41-06.png)

이제 `db.sqlite3` 파일을 살펴보면:

![](readMeImages/2023-08-02-14-41-54.png)


Recap
- django 는 세션,패스워드 등 모든 유저 데이터를 저장하는 곳으로 db 를 사용합니다.
- django 는 `db.sqlite3` 파일에서 `auth_user` 라는 테이블을 찾습니다.


#### `python manage.py createsuperuser` 명령을 실행 (poetry 가상환경에 있어야 한다.)

`python manage.py createsuperuser`는 Django의 명령어로, 관리자 계정을 생성하는 데 사용됩니다. Django에서는 관리자 계정을 통해 관리자 사이트를 사용할 수 있습니다.

관리자 사이트는 Django의 강력한 기능 중 하나로, 데이터베이스에 저장된 데이터를 조회, 생성, 수정, 삭제하는 인터페이스를 제공합니다. 예를 들어, 사용자 계정, 그룹, 애플리케이션의 모델 등의 데이터를 관리할 수 있습니다.

`createsuperuser` 명령을 실행하면, 먼저 사용자 이름을 입력하라는 프롬프트가 나타납니다. 그 다음에 이메일 주소와 비밀번호를 입력하라는 프롬프트가 나타납니다. 이 정보를 입력하면 관리자 계정이 생성되고, 이 계정으로 관리자 사이트에 로그인할 수 있습니다.

이 명령은 일반적으로 개발 환경에서 사용되며, 운영 환경에서는 보안상의 이유로 다른 방법을 사용해 관리자 계정을 생성하는 것이 일반적입니다.

터미널:
```
Username (leave blank to use 'hwang-isaac'): hwisaac
Email address: hwisaac0@gmail.com
Password: 123123
Password (again): 
This password is too short. It must contain at least 8 characters.
This password is too common.
This password is entirely numeric.
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.
```

이제 `/admin` 에서 로그인 하면 다음 화면을 볼 수 있습니다:
![](readMeImages/2023-08-02-14-56-28.png)

#### `python manage.py startapp houses` 명령 실행(houses 는 앱의 이름이 될 것입니다)

`houses/` 폴더가 생성됩니다.
![](readMeImages/2023-08-02-16-27-09.png)

`models.py` 에 모델*을 정의하고 admin.py 에 모델을 등록해야 합니다.

> 모델(*)은 어플리케이션에서 데이터의 모양을 describe 합니다.

> https://docs.djangoproject.com/ko/4.2/topics/db/models/

Django에서의 "Model"은 데이터베이스와의 상호작용을 관리하는 Python 클래스를 의미합니다. Django는 데이터베이스의 스키마를 정의하고 데이터를 저장, 수정, 검색하는 데 사용되는 ORM(Object-Relational Mapping) 기술을 제공합니다. 이 ORM은 SQL 쿼리를 직접 작성하지 않고도 데이터베이스와 상호작용할 수 있도록 도와줍니다.

Model 클래스는 Django 애플리케이션의 models.py 파일에 정의됩니다. 각 Model 클래스는 데이터베이스 테이블의 구조를 정의하고, 데이터베이스와 상호작용하는데 필요한 메서드와 속성을 가지고 있습니다.

Model 클래스의 주요 특징:

1. 클래스 변수: Model 클래스는 데이터베이스 테이블의 각 열을 클래스 변수로 표현합니다. 이러한 변수는 데이터베이스 필드와 매핑되어 데이터의 타입과 제약 조건을 정의합니다.

2. 메서드: Model 클래스는 데이터베이스와 상호작용하기 위한 다양한 메서드들을 제공합니다. 예를 들면, 객체 생성, 수정, 삭제, 데이터 검색 등의 작업을 수행하는 메서드들이 있습니다.

3. 관계 정의: Model 클래스를 사용하여 데이터베이스 테이블 간의 관계를 정의할 수 있습니다. 예를 들어, ForeignKey, OneToOneField, ManyToManyField 등을 사용하여 다른 테이블과의 관계를 설정할 수 있습니다.

Model 클래스의 정의 예시:

```python
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_date = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
```

위의 예시에서 `Author`와 `Book`은 두 개의 Django Model 클래스입니다. `Author` 클래스는 "name"과 "email" 필드를 갖고 있으며, `Book` 클래스는 "title", "publication_date", 그리고 "author" 필드를 갖고 있습니다. `author` 필드는 `Author` 클래스와의 관계를 나타내기 위해 ForeignKey를 사용하여 정의되었습니다.

Django의 Model을 사용하면 데이터베이스와의 상호작용을 추상화하고 편리하게 관리할 수 있습니다. Model 클래스를 사용하여 데이터베이스의 스키마를 정의하면, Django는 데이터베이스에 대한 복잡한 처리를 대신 처리해주므로 개발자는 데이터베이스와 직접적인 상호작용에 대해 걱정하지 않고도 애플리케이션을 개발할 수 있습니다.

<hr />

db 는 해당 모델에 대해 전혀 모르는 상황입니다. 

django 에게 파일의 존재를 알리기
`config/settings.py`
```py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'houses.apps.HousesConfig',
]
```


모델이 완성되었으면, `admin.py`에 `import` 해준다:
```py
from django.contrib import admin
from .models import House


@admin.register(House) # 이 HouseAdmin class 가 House 모델을 통제하게 한다
class HouseAdmin(admin.ModelAdmin):
    pass
```

<hr />

`migration` 을 통해 db의 모양을 변경합시다.

#### `python manage.py makemigrations` 

model 에 관한 정보를 토대로 `houses/migrations` 폴더에 파일(예:`0001_initial.py` )을 생성합니다.
#### `python manage.py migrate` : 마이그레이션을 적용합니다.

이제 `db` 가 `models.py` 가 연동되었습니다.

(model을 변경ㅏ면 makemigrations 와 migrate 를 다 해줘야 적용됩니다.)

## model

![Alt text](image.png)

> `__str__` 메서드를 재정의하면 House object 와 같은 이름을 변경할 수 있습니다.

```py
class House(models.Model):

    """Model Definition for Houses"""

    name = models.CharField(max_length=140)
    price_per_night = models.PositiveIntegerField()
    description = models.TextField()
    address = models.CharField(max_length=140)
    # https://docs.djangoproject.com/en/4.2/ref/models/fields/#default
    pats_allowed=models.BooleanField(default=True)
    def __str__(self):
        return self.name
```


## field 
필드 옵션 문서
https://docs.djangoproject.com/en/4.2/ref/models/fields/

> `admin.py` 파일을 수정합시다.

admin.py
```py
# 수정전
from django.contrib import admin
from .models import House

@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    pass
```

`list`나 `tuple` 속성을 전달해야 합니다. (`string` 은 ❌)

### list_display 속성

> admin 패널에 보이고 싶은 column 들의 list 를 적어줍니다. (실제로 존재하는 이름들이어야 함)

```py
@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "price_per_night",
        "address",
        "pets_allowed"
    ]
```

![](readMeImages/2023-08-05-13-56-17.png)

### list_filter 속성

> 어떤 column 을 기준으로 필터링 할 지를 적으면 됩니다.

```py
list_filter = [
    "price_per_night",
    "pets_allowed"
]
```
![](readMeImages/2023-08-05-14-51-44.png)


### search_fields 속성

> 어떤 column 에 대해 검색할지 정합니다.

```py
search_fields = [
    "address" # address__startswith 라고 하면 시작하는 단어로 검색합니다
]
```


## User 관리

django 는 기본적으로 관리자패널(http://127.0.0.1:8000/admin/)과 User 에 대한 것들을 제공해줍니다.(http://127.0.0.1:8000/admin/auth/user/)
이 것들을 어떻게 사용해야 할까요?
커스터마이징하려면 어떻게 해야 할까요?

**옵션1**
- django 가 제공하는 user 를 이용해서 profile 모델을 만들고, Profile은 user에 추가하고 싶은 커스텀들을 가지도록 만듭니다.

**옵션2**
- [user 모델을 아예 새로 custom 한다](https://docs.djangoproject.com/en/4.2/topics/auth/customizing/#substituting-a-custom-user-model)

> 기본으로 제공되는 user 모델만으로 충분하더라도 custom model 을 만들어서 대체하는것을 추천합니다.


## vscode 가 django 를 찾지 못하는 경우
> vscode 에서 django 에 노란색 밑줄이 그어진 현상을 해결하는 방법

![](readMeImages/2023-08-07-22-16-01.png)

문제원인
django 는 가상환경에 설치되어 있습니다. 그러나, pylance 는 컴퓨터에서 django 를 찾기 때문에 찾을 수가 없습니다.

문제해결
poetry 의 가상환경의


## python 포매터 추천: Formatter black

## users app 을 만들자
> Django 의 user 를 상속받는 우리만의 user



```
poetry shell
```

```
python manage.py runserver
```

users 앱 생성하기
```
python manage.py startapp users
```

### user 를 상속받아서 만들기
```py
from django.db import models
from django.contrib.auth.models import AbstractUser

# 새로운 user 모델을 만들 경우
"""
class User(models.Model):
    pass
"""

# 상속 받아서 user 모델을 만들 경우
class User(AbstractUser):
    pass
```


#### settings.py 설정

> django 에 user model 을 사용하겠다고 알려줘야 합니다.

`config/settings.py` 에 다음을 추가:

```py
# Auth
AUTH_USER_MODEL = "users.User"
```

`INSTALLED_APPS` 배열에도 `'users.apps.UsersConfig'` 추가

```py
# Application definition
CUSTOM_APPS = [
    "hoses.apps.HousesConfig",
    
]
SYSTEM_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

INSTALLED_APPS = CUSTOM_APPS + SYSTEM_APPS

```

#### 만약 프로젝트 중간에 user 를 시작한 경우

프로젝트 도중 기존에 user 모델을 사용해서 사용자를 만들어서 사용하고 있다면, 새로운 user 모델을 만들수가 없습니다.

이런 경우, 우선 서버를 종료하고
1. `db.sqlite3` 파일을 삭제해서 db의 모든 유저를 제거하고, migrations 폴더의 migration 들을 (앞에 숫자붙은 파일들) 도 삭제합니다.
2. `python manage.py makemigrations` 실행
3. `python manage.py migrate` 실행
4. `python manage.py runserver` 서버를 재시작합니다.

`python manage.py createsuperuser` 관리자 계정도 생성

> Note : 만약에 다음과 같이 default 값을 전해주지 않은 `is_host` 필드가 있는 채로 migrate 를 시도한다면 에러가 발생합니다

```py
class User(AbstractUser):
    first_name = models.CharField(max_length=150, editable=False)
    last_name = models.CharField(max_length=150, editable=False)
    name = models.CharField(max_length=150, editable=False)
    is_host = models.BooleanField()
```

```
It is impossible to add a non-nullable field 'is_host' to user without specifying a default. This is because the database needs something to populate existing rows.
Please select a fix:
 1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
 2) Quit and manually define a default value in models.py.
Select an option: 
```
- non-nullable 필드인 `is_host` 필드에 default value 없이 모델에 추가하는 것은 불가능합니다.(데이터베이스는 기존 rows 에 입력 시킬 데이터가 필요하기 때문. 이미 생성해둔 슈퍼유저가 `is_host=null` 인 데이터를 가지기 때문 )
    1. 해결1: 지금 1회성 디폴트값을 제공한다
    2. 해결2: 직접 models.py 파일에 default value 를 정의해준다.
    3. 해결3: nullable 이도록 `is_host = models.BooleanField(null=True)` 로 수정합니다.
