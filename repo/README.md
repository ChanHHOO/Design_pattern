# 목표
Django 애플리케이션의 기본 뼈대를 제공한다. Two Scoops of Django 책을 참고로 작성하였다.

cookiecutter를 올바로 활용하려면 다소 많은 배경지식을 필요로 해서 간단한 템플릿을 만들고자 한다.

가장 기본이 되는 내용으로 구성하고 --template 옵션으로 새 프로젝트를 간단히 시작할 수 있도록 한다.

# 프로젝트의 생성과 실행
## Django 설치
pip 패키지로 Django를 설치한다.

```
pip install Django
```

## 프로젝트의 생성
```django-admin.py``` 명령어로 저장소에서 다운로드해서 프로젝트를 생성한다. ```startproject```로 프로젝트를 시작하지 않는다.

```
django-admin.py startproject --template https://gitlab.com/mairoo/django-quickstarter/repository/archive.zip repo
```
## secret.py 파일 생성 및 수정
```
cp conf/settings/secret.py.txt conf/settings/secret.py
```

```conf/settings/secret.py.txt``` 파일을 복사해서 데이터베이스 연결 등 알맞은 설정값으로 변경한다.

실행환경에 따라서  설정 파일과 요구사항 파일을 분류한다.

* 개발자 컴퓨터 설정: ```conf/settings/local.py``` 및 ```requirements/local.txt```
* 스테이징 서버 설정: ```conf/settings/staging.py``` 및 ```requirements/staging.txt```
* 운영 서버 설정: ```conf/settings/production.py``` 및 ```requirements/production.txt``` 

## 프로젝트 실행

서버 실행을 하려면 설정 모듈을 정확히 지정해야 한다.

* 명령행 옵션으로 지정: ```--settings=conf.settings.local```
* 환경변수로 지정: ```DJANGO_SETTINGS_MODULE=conf.settings.local```

아래와 같이 명령행 옵션으로 테스트 서버를 구동할 수 있다.

```
manage.py runserver --settings=conf.settings.local
```

위 예시의 ```local```이 아닌 ```production```, ```staging``` 등으로 구체적인 설정 파일을 지정할 수 있다.

만약 아무런 옵션도 지정하지 않는다면 ```production``` 설정으로 간주한다.

# Djagno-Quickstarter 설명

## 템플릿 구조

굳이 저장소 루트와 프로젝트 루트 단계를 나눌 필요는 없을 것 같아 저장소(repo)-설정(conf) 2단계 구조로 정의한다.

다만 다른 프로젝트와 구별할 수 있도록 프로젝트 이름으로 최상위 디렉토리의 이름을 짓는다.

```
<프로젝트_이름>/
    repo/
        conf/
            settings/
                base.py
                local.py
                production.py
        manage.py
        properties.ini
    venv/
    run/
        uwsgi.ini
        uwsgi.sock
        gunicorn.sock
    logs/
        access.log
        error.log
        uwsgi.log
    ssl/
```

```프로젝트_이름``` 최상위 디렉토리의 하위 디렉토리 5개의 의미는 다음과 같다.

* ```repo```: 저장소 루트 디렉토리이면서 동시에 프로젝트 루트가 된다.
* ```venv```: 종속성 분리를 제공하기 위한 독립된 가상환경 virtualenv 디렉토리이다.
* ```run```: uWSGI 서버 배포시 소켓이 저장되는 디렉토리이다. ```manage.py runserver```로 서버를 구동한다면 불필요하다.
* ```logs```: uWSGI 서버 로그 및 nginx 로그 등이 저장되는 디렉토리이다.
* ```ssl```: SSL 서버 운영을 위해 여러 공개키/비공개키 등을 저장하는 디렉토리이다.

```repo```, ```venv```, ```run```, ```logs```, ```ssl``` 디렉토리 모두 이름을 약속해서 다른 Django 프로젝트를 개발하더라도 쉽게 구조를 파악할 수 있도록 같은 이름으로 일관성을 유지한다.

## 로컬, 스테이징, 운영 환경 설정의 분류

1. 환경마다 다른 공개적인 설정
    * ```local.py```: 개발자 컴퓨터 설정
    * ```staging.py```: 스테이징 서버 설정
    * ```production.py```: 운영 서버 설정
1. 모든 환경에서 동일한 공개적인 설정
    * ```base.py``` 파일을 만들고 이를 구체적인 ```local.py```, ```staging,py```, ```production.py``` 등에서 임포트한다.
1. 환경마다 다른 비공개적인 설정
    * ```local.py```, ```staging.py```, ```production.py``` 등으로 파일을 나누고 설정값은 ```secret.py``` 파일로 정의한다.
1. 모든 환경에서 동일한 비공개적인 설정
    * ```base.py``` 파일을 만들고 설정값은 ```secret.py``` 파일로 정의하고 구체적인 ```local.py```, ```staging.py```, ```production.py``` 등에서 임포트한다.

공개적인 설정은 저장소에 커밋 관리되고 비공개적인 설정은 ```secret.py``` 파일에 저장하여 저장소에 공개되지 않도록 한다. 현재 ```.gitignore``` 파일에 등록되어 있다.

## ```secret.py``` 파일

* ```secret.py.txt``` 파일을 복사해 만든다.
* 실행환경에 따라 달라질 수 있으면서 다른 서버에 공개되면 안 되는 데이터를 저장한다.
* 비밀번호와 암호키 등을 포함하고 있으므로 절대 공개 저장소에 커밋하면 안 된다.

## 커스텀 User 모델
```django.contrib.auth.models.AbstractBaseUser``` 클래스를 상속한 사용자 정의 User 모델을 사용한다.

Django 사용자 모델 중 가장 자유도가 높은 방법으로 프로젝트 시작에 결정하지 않고 중간에 변경하려면 큰 어려움이 있다.

## 이메일 인증 2단계 가입 절차
django-registration 라이브러리를 이용하여 회원 가입 후 이메일 인증을 해야 로그인 가능하다.